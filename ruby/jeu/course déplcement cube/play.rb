require 'Gosu'

class Game < Gosu::Window

    def initialize
      super(Gosu.screen_width, Gosu.screen_height)
      @font = Gosu::Font.new(self, Gosu::default_font_name, 20)
    end

    def draw
        sizeX = 300
        sizeY = 100
        positionX = Gosu.screen_width/2 - sizeX/2
        positionY = Gosu.screen_height/2 - sizeY/2
        draw_rect(positionX, positionY, sizeX, sizeY, Gosu::Color::WHITE, z = 0, mode = :default)

        
        sizeX = 3
        sizeY = 3
        positionX = Gosu.screen_width/2 - sizeX/2
        positionY = Gosu.screen_height/2 - sizeY/2
        txt_play = "Play"
        @font.draw(txt_play, positionX, positionY, 1, sizeX, sizeY, Gosu::Color::BLACK)
    end
end

fenetre = Game.new
fenetre.show