require 'Gosu'

class Game_window < Gosu::Window

    def initialize
        super(Gosu.screen_width, Gosu.screen_height)    # initialze écran
        self.caption = "Ma Fenêtre"                     # titre
        self.resizable = true                           # redimensionnables
        self.update_interval = 1
        @mouse_down = false

        @img_btn_play = Game_image.new("image/play.png", Gosu.screen_width / 2, Gosu.screen_height / 2, 0.3, 0.3, "image")
        @img_souris = Game_image.new("image/pointer_bleu.png", self.mouse_x / 2, self.mouse_y / 2, 1, 1, "souris")
    end

    def update
        @img_souris.positionX = self.mouse_x
        @img_souris.positionY = self.mouse_y

        if @img_btn_play.survole(self.mouse_x, self.mouse_y)
            @img_souris.image = "image/pointer_rose.png" if @img_souris.image = "image/pointer_bleu.png"
            @img_souris.scaleX = 0.8 if @img_souris.scaleX != 0.8 && @mouse_down
            @img_souris.scaleY = 0.8 if @img_souris.scaleY != 0.8 && @mouse_down
            @img_souris.scaleX = 0.5 if @img_souris.scaleX != 0.5 && !@mouse_down
            @img_souris.scaleY = 0.5 if @img_souris.scaleY != 0.5 && !@mouse_down
            @img_btn_play.scaleX += 0.02 if @img_btn_play.scaleX < 0.38
            @img_btn_play.scaleY += 0.02 if @img_btn_play.scaleY < 0.38

        else
            @img_souris.image = "image/pointer_bleu.png" if @img_souris.image = "image/pointer_rose.png"
            @img_souris.scaleX = 1 if @img_btn_play.scaleX != 1
            @img_souris.scaleY = 1 if @img_btn_play.scaleY != 1
            @img_btn_play.scaleX -= 0.01 if @img_btn_play.scaleX > 0.3
            @img_btn_play.scaleY -= 0.01 if @img_btn_play.scaleY > 0.3
        end

    end

    def draw
        @img_btn_play.draw
        @img_souris.draw
    end

    def needs_cursor?
        false
    end

    def button_down(id)
        if id == Gosu::MS_LEFT
            @mouse_down = true
        end
    end

    def button_up(id)
        if id == Gosu::MS_LEFT
            @mouse_down = false
        end
    end
end


class Game_image

    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY

    def initialize(lien, positionX, positionY, scaleX, scaleY, nom)
        @nom = nom
        @image = Gosu::Image.new(lien)
        @scaleX = scaleX
        @scaleY = scaleY
        @width = @image.width * @scaleX
        @height = @image.height * @scaleY
        @positionX_defaut = positionX
        @positionY_defaut = positionY
        @positionX = positionX - @width/2
        @positionY = positionY - @height/2
        @frame = 0
        @frame_initialiser = false
    end

    def draw()
        @image.draw(@positionX, @positionY, 0, @scaleX, @scaleY)
    end

    def positionX=(value)
        @positionX = value - @width
    end

    def positionY=(value)
        @positionY = value - @height
    end

    def scaleX=(value)
        case @nom
        when "souris"
            @scaleX = value
            ancien_width = @width
            @width = @image.width * @scaleX/2
            @positionX = (@positionX + ancien_width/2) - @width/2
        when "image"
            @scaleX = value
            @width = @image.width * @scaleX
            @positionX = @positionX_defaut - @width/2
        end
    end

    def scaleY=(value)
        case @nom
        when "souris"
            @scaleY = value
            ancien_height = @height
            @height = @image.height * @scaleY/2
            @positionY = (@positionY + ancien_height/2) - @height/2
        
        when "image"
            @scaleY = value
            @height = @image.height * @scaleY
            @positionY = @positionY_defaut - @height/2
        end
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

end

fenetre_game = Game_window.new
fenetre_game.show