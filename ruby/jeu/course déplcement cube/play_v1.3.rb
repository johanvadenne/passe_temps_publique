require 'Gosu'

class Fenetre < Gosu::Window

    def initialize
        # paramètre fentre
        super(Gosu.screen_width, Gosu.screen_height)    # initialze écran
        self.caption = "Ma Fenêtre"                     # titre
        self.resizable = true                           # redimensionnables
        self.update_interval = 1                        # intervalle de mise à jour en milliseconde
        
        # images
        @img_play = Image.new("image/play.png", self, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.3, 0.3, 0, "centre")    # bouton play
        @img_souris = Image.new("image/pointer_bleu.png", self, self.mouse_x / 2, self.mouse_y / 2, 1, 1, 10, "mouse")        # curseur souris
    end

    def update
        
        @img_souris.positionX = self.mouse_x    # repositionement de la souris
        @img_souris.positionY = self.mouse_y    # repositionement de la souris

        @img_play.ancrer

        @img_play.scale_agmente(0.005, 0.34) if @img_play.scale < 0.34 && @img_play.survole # si je survole grossire
        @img_play.scale_egale(0.3) if @img_play.scale != 0.3 && !@img_play.survole # si je survole grossire

    end

    def draw # dessine

        @img_play.dessiner
        @img_souris.dessiner

    end

    def needs_cursor? # visiualiser le curseur
        false
    end

    def button_down(id) # récupère le bouton presser
        if id == Gosu::MS_LEFT
            @clique_gauche = true
            @img_play.presse = true if @img_play.survole
        end
    end

    def button_up(id) # récupère le bouton relever
        if id == Gosu::MS_LEFT
            @clique_gauche = false
            @img_play.afficher = false if @img_play.presse == true && @img_play.survole
        end
    end

    def scale_agmente(valeur_ajoute, valeur_limite)

        @scaleX += valeur_ajoute if @scaleX < valeur_limite
        @scaleY += valeur_ajoute if @scaleY < valeur_limite

    end
end

class Image
    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY, :z_index, :afficher, :presse
  
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
      @presse = false
  
    end
  
    def dessiner
        @image.draw(@positionX, @positionY, @z_index, @scaleX, @scaleY) if @afficher
    end

    def positionX=(valeur)
        @positionX = valeur - @width/2
    end

    def positionY=(valeur)
        @positionY = valeur - @height/2
    end

    def scaleX=(valeur)
        modification_scaleX(valeur)
    end

    def modification_scaleX(valeur)
        @scaleX = valeur
        ancien_width = @width
        @width = @width_defaut * @scaleX
        @positionX = (@positionX+ancien_width/2) - @width/2
    end

    def scaleY=(valeur)
        modification_scaleY(valeur)
    end

    def modification_scaleY(valeur)
        @scaleY = valeur
        ancien_height = @height
        @height = @height_defaut * @scaleY
        @positionY = (@positionY+ancien_height/2) - @height/2
    end
  
    def ancrer
        nom_ancrage = ["centrer" ,"droite" ,"gauche" ,"haut" ,"haut_gauche" ,"haut_droite" ,"bas_droite" ,"bas_gauche" ,"bas", "mouse"]
        if @ancrage in nom_ancrage
            send(@ancrage)
        else
            puts @ancrage+" n'existe pas!"
        end
    end
  
    def centre
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

    def scale
        return @scaleX
    end

    def scale_agmente(valeur_ajout, valeur_limite)
        modification_scaleX(@scaleX += valeur_ajout) if @scaleX < valeur_limite
        modification_scaleY(@scaleY += valeur_ajout) if @scaleY < valeur_limite
    end

    def scale_egale(valeur)
        modification_scaleX(@scaleX = valeur)
        modification_scaleY(@scaleY = valeur)
    end
  
end

class Case_niveau

end

class Type_de_jeu

end


type_de_jeu = ["lettre aléatoire","phrase aléatoire"]

fenetre_game = Fenetre.new()
fenetre_game.show