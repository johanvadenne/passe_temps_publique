require "Gosu"

class Game_window < Gosu::Window
  def initialize
    super(Gosu.screen_width, Gosu.screen_height)
    self.caption = "Ma Fenêtre"
    self.resizable = true
    self.update_interval = 1

    @images = []

    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "centrer")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "droite")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "gauche")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "haut")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "haut_gauche")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "haut_droite")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "bas_droite")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "bas_gauche")
    @images << Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.1, 0.1, 0, "bas")
  end

  def update
    @images.each do |image|
      image.ancrer
      image.afficher = false if image.survole
    end
  end

  def draw
    @images.each do |image|
      image.dessiner
    end
  end
end

class Image
  attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY, :z_index, :afficher

  def initialize(lien, fenetre, positionX, positionY, scaleX, scaleY, z_index, ancrage)
    @image = Gosu::Image.new(lien)
    @image_lien = lien
    @fenetre = fenetre
    @scaleX = scaleX
    @scaleY = scaleY
    @width_defaut = @image.width
    @height_defaut = @image.height
    @width = @width_defaut * scaleX
    @height = @height_defaut * scaleY
    @positionX = positionX - @width / 2
    @positionY = positionY - @height / 2
    @z_index = z_index
    @ancrage = ancrage
    @gauche = @fenetre.width - @positionX
    @bas = @fenetre.height - @positionY
    @haut = @positionY - @height/2
    @afficher = true

  end

  def dessiner
    @image.draw(@positionX, @positionY, @z_index, @scaleX, @scaleY) if @afficher
  end

  def ancrer
    nom_ancrage = ["centrer" ,"droite" ,"gauche" ,"haut" ,"haut_gauche" ,"haut_droite" ,"bas_droite" ,"bas_gauche" ,"bas"]
    if @ancrage in nom_ancrage
      send(@ancrage)
    end
  end

  def centrer
    @positionX = @fenetre.width / 2 - @width / 2
    @positionY = @fenetre.height / 2 - @height / 2
  end

  def gauche
    @positionY = @fenetre.height / 2 - @height / 2
  end

  def haut_gauche
    @positionY = @haut
  end

  def droite
    @positionX = (@fenetre.width - @gauche)
    @positionY = @fenetre.height / 2 - @height / 2
  end

  def haut_droite
    @positionX = (@fenetre.width - @gauche)
    @positionY = @haut
  end

  def haut
    @positionX = @fenetre.width / 2 - @width / 2
    @positionY = @haut
  end

  def bas
    @positionX = @fenetre.width / 2 - @width / 2
    @positionY = (@fenetre.height - @bas) + @height / 2
  end

  def bas_droite
    @positionX = (@fenetre.width - @gauche)
    @positionY = (@fenetre.height - @bas) + @height / 2
  end

  def bas_gauche
    @positionY = (@fenetre.height - @bas) + @height / 2
  end

  def survole

    x = @fenetre.mouse_x
    y = @fenetre.mouse_y

    if x > @positionX && x < @positionX + @width && y > @positionY && y < @positionY + @height
        return true
    else
        return false
    end
  end

end

fenetre = Game_window.new
fenetre.show
