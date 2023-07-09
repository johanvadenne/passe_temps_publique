require 'Gosu'

class Fenetre < Gosu::Window

    def initialize
        # paramètre fentre
        super(Gosu.screen_width, Gosu.screen_height)    # initialze écran
        self.caption = "Ma Fenêtre"                     # titre
        self.resizable = true                           # redimensionnables
        self.update_interval = 1                        # intervalle de mise à jour en milliseconde
        
        # images
        @img_play = Image.new("image/play.png", Gosu.screen_width / 2, Gosu.screen_height / 2, 0.3, 0.3, 0)    # bouton play
        @img_souris = Image.new("image/pointer_bleu.png", self.mouse_x / 2, self.mouse_y / 2, 1, 1, 10)        # curseur souris
    end

    def update
        
        @img_souris.positionX = self.mouse_x    # repositionement de la souris
        @img_souris.positionY = self.mouse_y    # repositionement de la souris

        @img_play.positionX = self.width / 2    # repositionement au centre lors du redimentionement de l'écran
        @img_play.positionY = self.height / 2   # repositionement au centre lors du redimentionement de l'écran
        @img_play.scale_agmente(@img_play, 0.005, 0.34) if @img_play.scale < 0.34 && @img_play.survole(mouse_x, mouse_y) # si je survole grossire

    end

    def draw # dessine

        @img_play.draw
        @img_souris.draw

    end

    def needs_cursor? # visiualiser le curseur
        false
    end

    def button_down(id) # récupère le bouton presser
        if id == Gosu::MS_LEFT
            @clique_gauche = true
            @img_play.presse = true if @img_play.survole(mouse_x, mouse_y)
        end
    end

    def button_up(id) # récupère le bouton relever
        if id == Gosu::MS_LEFT
            @clique_gauche = false
            @img_play.clique = true if @img_play.presse == true && @img_play.survole(mouse_x, mouse_y)
        end
    end

    def scale_agmente(image, valeur_ajoute, valeur_limite)

        image.scaleX += valeur_ajoute if @scaleX < valeur_limite
        image.scaleY += valeur_ajoute if @scaleY < valeur_limite

    end

end

class Image < Gosu::Image

    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY, :dessiner, :clique, :presse, :opacity

    def initialize(lien, positionX, positionY, scaleX, scaleY, z_index)
        @image          = Gosu::Image.new(lien)
        @scaleX         = scaleX
        @scaleY         = scaleY
        @width_defaut   = @image.width
        @height_defaut  = @image.height
        @width          = @width_defaut * @scaleX
        @height         = @height_defaut * @scaleY
        @positionX      = positionX - @width/2
        @positionY      = positionY - @height/2
        @z_index        = z_index
        @dessiner       = true
        @pressed        = false    
        @clique         = false

    end

    def draw()
        @image.draw(@positionX, @positionY, @z_index, @scaleX, @scaleY) if @dessiner
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

    def scale()

        if @scaleX < @scaleY
            return @scaleX
        else
            return @scaleY
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

    def opacity(a)
        @image.from_blob(width, height, rgba = "\0\0\0\5" * (width * height))
    end

end

class Case_niveau

end

class Type_de_jeu

end


type_de_jeu = ["abc","abcABC","abcABC123","abcABC123&%!","personalisé"]

fenetre_game = Fenetre.new()
fenetre_game.show