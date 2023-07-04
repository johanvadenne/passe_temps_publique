require 'Gosu'

class Game < Gosu::Window

  def initialize
    super(Gosu.screen_width, Gosu.screen_height)
    @image_play = Gosu::Image.new("image/play.png")
    @pointer_image = Gosu::Image.new("image/pointer.png")
    @image_play_info = ImageInfo.new(@image_play, Gosu.screen_width / 2, Gosu.screen_height / 2, 0.3, 0.3)
  end

  def update
    if survole(@image_play_info)
      grossissement(@image_play_info)
    end
  end

  def draw
    @image_play.draw(@image_play_info.positionX - @image_play_info.width/2, @image_play_info.positionY - @image_play_info.height/2, 0, @image_play_info.scaleX, @image_play_info.scaleY)
    @pointer_image.draw(mouse_x, mouse_y, 0)
  end

  def needs_cursor?
    false
  end

  def survole(objet)
    if mouse_x >= objet.positionX && mouse_y >= objet.positionY && mouse_x <= objet.positionX + objet.width && mouse_y <= objet.positionY + objet.height
      return true
    end
    return false
  end

  def grossissement(objet)
    objet.scaleX+=0.1
    objet.scaleY+=0.1 
    objet.width = objet.width * objet.scaleX
    objet.height = objet.height * objet.scaleY
  end
end

class ImageInfo
  attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY

  def initialize(image, positionX, positionY, scaleX, scaleY)
    @positionX = positionX
    @positionY = positionY
    @width = image.width * scaleX
    @height = image.height * scaleY
    @scaleX = scaleX
    @scaleY = scaleY
  end
end

fenetre = Game.new
fenetre.show
