require 'Gosu'

class Game < Gosu::Window

    def initialize
      super(Gosu.screen_width, Gosu.screen_height)
      self.caption = "Ma Fenêtre"                   # titre
      self.fullscreen = false                       # plaine écran
      self.borderless = false                       # sans bordure
      puts self.height                              # hauteur
      puts self.width                               # largeur
      puts self.mouse_x                             # souris x
      puts self.mouse_y                             # souris y
      self.resizable = true                         # redimensionnables 
      self.update_interval = 1                      # L'intervalle entre les appels à mise à jour, en millisecondes.
      @x = 1

    end
  
    def update                                      # Cette méthode est appelée une fois update_interval millisecondes pendant que la fenêtre est affichée
        # puts self.mouse_x
        # puts self.mouse_y
        # puts self.height
        # puts self.width 
    end

    def button_down(id)                             # Cette méthode est appelée avant update si un bouton est enfoncé pendant que la fenêtre est focalisée.
        case id
        when Gosu::KB_ESCAPE
          close # Ferme la fenêtre
        when Gosu::KB_A..Gosu::KB_Z
          puts "bouton pressé #{Gosu.button_id_to_char(id)}"
        else
            puts id
        end
    end

    def button_up(id)   # Cette méthode est appelée avant update si un bouton est relâché alors que la fenêtre est focalisée.
        case id
        when Gosu::KB_A..Gosu::KB_Z
          puts "bouton relevé #{Gosu.button_id_to_char(id)}"
        else
            puts id
        end
    end

    def draw     # Cette méthode est appelée après chaque mise à jour et chaque fois que le système d'exploitation souhaite que la fenêtre se repeigne.
        self.draw_rect(100, 500, 100, 100, Gosu::Color::RED)

    end
    
    def drop(filename)            # Appelé lorsqu'un fichier est déposé dans la fenêtre.
        puts filename
    end

    def gamepad_connected(index)    # manette connecté 
        puts index
    end
    
    def gamepad_disconnected(index) # manette déconnecter
        puts index
    end

    def lose_focus                    # sortie de la fenetre
        puts "reviens dans la fenêtre!"
    end

    def needs_cursor?                   # affichage de la souris
        false
    end

    def needs_redraw?                   # dessin
        true
    end


end

game = Game.new
game.show