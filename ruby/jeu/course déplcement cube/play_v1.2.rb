require 'Gosu'

class Game_window < Gosu::Window

    def initialize
        # paramètre fentre
        super(Gosu.screen_width, Gosu.screen_height)    # initialze écran
        self.caption = "Ma Fenêtre"                     # titre
        self.resizable = true                           # redimensionnables
        self.update_interval = 1                        # intervalle de mise à jour en milliseconde

        # images
        @img_play = Game_image.new("image/play.png", Gosu.screen_width / 2, Gosu.screen_height / 2, 0.3, 0.3, 0)    # bouton play
        @img_souris = Game_image.new("image/pointer_bleu.png", self.mouse_x / 2, self.mouse_y / 2, 1, 1, 10)        # curseur souris
        @niv_1 = Case_niveau.new("1")
        @niv_2 = Case_niveau.new("2")
        @niv_3 = Case_niveau.new("3")

    end

    def update

        @img_souris.positionX = self.mouse_x    # repositionement de la souris
        @img_souris.positionY = self.mouse_y    # repositionement de la souris
        @img_souris.scaleX = 1.8 if @img_play.scaleX < 1.8 && @clique_gauche   # si je clique grossire X
        @img_souris.scaleY = 1.8 if @img_play.scaleY < 1.8 && @clique_gauche   # si je clique grossire Y
        @img_souris.scaleX = 1 if @img_play.scaleX != 1 && !@clique_gauche      # si je clique pas taille d'origine X
        @img_souris.scaleY = 1 if @img_play.scaleY != 1 && !@clique_gauche      # si je clique pas taille d'origine Y

        if @img_play.dessiner

            @img_play.positionX = self.width / 2    # repositionement au centre lors du redimentionement de l'écran
            @img_play.positionY = self.height / 2   # repositionement au centre lors du redimentionement de l'écran
            
            @img_play.scaleX += 0.005 if @img_play.scaleX < 0.34 && @img_play.survole(mouse_x, mouse_y) # si je survole grossire X
            @img_play.scaleY += 0.005 if @img_play.scaleY < 0.34 && @img_play.survole(mouse_x, mouse_y) # si je survole grossire Y
            @img_play.scaleX = 0.3 if @img_play.scaleX != 0.3 && !@img_play.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine X
            @img_play.scaleY = 0.3 if @img_play.scaleY != 0.3 && !@img_play.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine Y

            
            if @img_play.clique  # si bouton cliquer ne plus dessiner
                @img_play.dessiner = false 
                @niv_1.dessiner = true
                @niv_2.dessiner = true
                @niv_3.dessiner = true
            end
        
        end

        if @niv_1.dessiner

            @niv_1.scaleX += 0.01 if @niv_1.scaleX < 1.2 && @niv_1.survole(mouse_x, mouse_y) # si je survole grossire X
            @niv_1.scaleY += 0.01 if @niv_1.scaleY < 1.2 && @niv_1.survole(mouse_x, mouse_y) # si je survole grossire Y
            @niv_1.scaleX = 1 if @niv_1.scaleX != 1 && !@niv_1.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine X
            @niv_1.scaleY = 1 if @niv_1.scaleY != 1 && !@niv_1.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine Y

            @niv_2.scaleX += 0.01 if @niv_2.scaleX < 1.2 && @niv_2.survole(mouse_x, mouse_y) # si je survole grossire X
            @niv_2.scaleY += 0.01 if @niv_2.scaleY < 1.2 && @niv_2.survole(mouse_x, mouse_y) # si je survole grossire Y
            @niv_2.scaleX = 1 if @niv_2.scaleX != 1 && !@niv_2.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine X
            @niv_2.scaleY = 1 if @niv_2.scaleY != 1 && !@niv_2.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine Y

            @niv_3.scaleX += 0.01 if @niv_3.scaleX < 1.2 && @niv_3.survole(mouse_x, mouse_y) # si je survole grossire X
            @niv_3.scaleY += 0.01 if @niv_3.scaleY < 1.2 && @niv_3.survole(mouse_x, mouse_y) # si je survole grossire Y
            @niv_3.scaleX = 1 if @niv_3.scaleX != 1 && !@niv_3.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine X
            @niv_3.scaleY = 1 if @niv_3.scaleY != 1 && !@niv_3.survole(mouse_x, mouse_y)   # si je survole pas taille d'origine Y

        end
        
        

        

    end

    def draw # dessine

        @img_play.draw
        @img_souris.draw
        @niv_1.draw
        @niv_2.draw
        @niv_3.draw

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
end


class Game_image

    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY, :dessiner, :clique, :presse

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


class Case_niveau

    attr_accessor :positionX, :positionY, :width, :height, :scaleX, :scaleY, :dessiner

    def initialize(texte)

        @width_defaut   = 100
        @height_defaut  = 100
        @positionX = 50 + (50 + @width_defaut) * (texte.to_i-1)
        @positionY = 50
        @width     = @width_defaut
        @height    = @height_defaut
        @couleur_carre = Gosu::Color::WHITE
        @couleur_texte = Gosu::Color::BLACK
        @dessiner = false
        @scaleX = 1
        @scaleY = 1
        @texte = texte
        @num_niv = Gosu::Font.new(@height_defaut)

    end

    def draw()
        Gosu::draw_rect(@positionX, @positionY, @width, @height, @couleur_carre, 0, mode = :default) if @dessiner
        @num_niv.draw_text(@texte, ((@width - @num_niv.text_width(@texte, @scaleX))/2)+@positionX, @positionY, 1, @scaleX, @scaleY, @couleur_texte, mode = :default) if @dessiner
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