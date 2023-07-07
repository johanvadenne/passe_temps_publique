require 'Gosu'

class Game_window < Gosu::Window

    def initialize
        # paramètre fentre
        super(Gosu.screen_width, Gosu.screen_height)    # initialze écran
        self.caption = "Ma Fenêtre"                     # titre
        self.resizable = true                           # redimensionnables
        self.update_interval = 1                        # intervalle de mise à jour en milliseconde

        # images
        @img_play = Game_image.new("image/play.png", Gosu.screen_width / 2, Gosu.screen_height / 2, 0.3, 0.3)
        @img_souris = Game_image.new("image/pointer_bleu.png", self.mouse_x / 2, self.mouse_y / 2, 1, 1)

    end

    def update



        @img_souris.positionX = self.mouse_x
        @img_souris.positionY = self.mouse_y
        
        @img_play.scaleX += 0.01 if @img_play.scaleX != 0.34 && @img_play.survole(mouse_x, mouse_y)
        @img_play.scaleY += 0.01 if @img_play.scaleY != 0.34 && @img_play.survole(mouse_x, mouse_y)
        @img_play.scaleX = 0.3 if @img_play.scaleX != 0.3 && !@img_play.survole(mouse_x, mouse_y)
        @img_play.scaleY = 0.3 if @img_play.scaleY != 0.3 && !@img_play.survole(mouse_x, mouse_y)
        
        @img_souris.scaleX = 1.8 if @img_play.scaleX != 1.8 && @clique_gauche
        @img_souris.scaleY = 1.8 if @img_play.scaleY != 1.8 && @clique_gauche
        @img_souris.scaleX = 1 if @img_play.scaleX != 1 && !@clique_gauche
        @img_souris.scaleY = 1 if @img_play.scaleY != 1 && !@clique_gauche

        

    end

    def draw

        @img_play.draw
        @img_souris.draw

    end

    def needs_cursor?
        false
    end

    def button_down(id)
        if id == Gosu::MS_LEFT
            @clique_gauche = true
        end
    end

    def button_up(id)
        if id == Gosu::MS_LEFT
            @clique_gauche = false
        end
    end
end


class Game_image

    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY

    def initialize(lien, positionX, positionY, scaleX, scaleY)
        @image          = Gosu::Image.new(lien)
        @scaleX         = scaleX
        @scaleY         = scaleY
        @width_defaut   = @image.width
        @height_defaut  = @image.height
        @width          = @width_defaut * @scaleX
        @height         = @height_defaut * @scaleY
        @positionX      = positionX - @width/2
        @positionY      = positionY - @height/2
        @dessiner       = true
    end

    def draw()
        @image.draw(@positionX, @positionY, 0, @scaleX, @scaleY) if @dessiner
    end

    def positionX=(value)
        @positionX = value - @width/2
    end

    def positionY=(value)
        @positionY = value - @height/2
    end

    def scaleX=(value)
        @scaleX = value
        ancien_width = @width
        @width = @width_defaut * @scaleX
        @positionX = (@positionX+ancien_width/2) - @width/2
    end

    def scaleY=(value)
        @scaleY = value
        ancien_height = @height
        @height = @height_defaut * @scaleY
        @positionY = (@positionY+ancien_height/2) - @height/2
    end

    def image=(value)
        @image = Gosu::Image.new(value)
    end

    def survole(x, y)
        if x > @positionX && x < @positionX + @width && y > @positionY && y < @positionY + @height
            return true
        else
            return false
        end
    end

    def opacity(a)
        @image.from_blob(width, height, rgba = "\0\0\0\5" * (width * height))
    end

    def log()
        puts @scaleX
        puts @scaleY
        puts @width_defaut
        puts @height_defaut
        puts @width
        puts @height
        puts @positionX
        puts @positionY
    end

end

fenetre_game = Game_window.new
fenetre_game.show