require "Gosu"

class Game_window < Gosu::Window

    def initialize
        # paramètre fentre
        super(Gosu.screen_width, Gosu.screen_height)    # initialze écran
        self.caption = "Ma Fenêtre"                     # titre
        self.resizable = true                           # redimensionnables
        self.update_interval = 1                        # intervalle de mise à jour en milliseconde

        @image = Image.new("image/play.png",Gosu.screen_width/2, Gosu.screen_height/2, 0.3, 0.3, 0, "center")
    end

    def draw
        @image.dessiner()
    end

end

class Image

    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY, :z_index

    def initialize(lien, positionX, positionY, scaleX, scaleY, z_index, ancrage)
        super(lien)
        @image_lien     = lien
        @scaleX         = scaleX
        @scaleY         = scaleY
        @width_defaut   = Gosu.width
        @height_defaut  = Gosu.height
        @width          = @width_defaut * scaleX
        @height         = @height_defaut * scaleY
        @positionX      = positionX - @width / 2
        @positionY      = positionY - @height / 2
        @z_index        = z_index
        @ancrage        = ancrage
    end

    def dessiner
        @image.draw(@positionX, @positionY, @z_index, @scaleX, @scaleY)
    end

    def ancrer()
        
    end
end

fenetre = Game_window.new
fenetre.show()