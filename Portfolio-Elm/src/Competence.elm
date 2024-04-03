module Competence exposing (..)

import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (onClick)


-- MODEL

type alias Model =
    { titre : String
    }

init : Model
init =
    { titre = "Johan Vadenne" }

-- UPDATE

type Msg
    = NoOp
    | Navigate String

update : Msg -> Model -> Model
update msg model =
    case msg of
        NoOp ->
            model

        Navigate _ ->
            model



-- VIEW

view : Model -> Html Msg
view model =
    div (styles model)
    [ h1 (titleStyles model.titre) [ text model.titre ]
    , header (headerStyles model.titre)
    [ a (List.concat [lienStyles model.titre, bouton1Styles model.titre, [href "Main.elm"]]) [ text "Home" ]
    , a (List.concat [lienStyles model.titre, bouton2Styles model.titre, [href "Qui.elm"]]) [ text "Qui je suis?" ]
    , a (List.concat [lienStyles model.titre, bouton3Styles model.titre, [href "Veille.elm"]]) [ text "Ma veille" ]
    , a (List.concat [lienStyles model.titre, bouton4Styles model.titre, [href "Projet.elm"]]) [ text "Mes projets" ]
    , a (List.concat [lienStyles model.titre, bouton5Styles model.titre, [href "Competence.elm"]]) [ text "Mes compétences" ]
    ]
    , section (sectionStyles model.titre) 
    [ div (colonnecompStyles model.titre) 
    [ div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Langage"]
    , ul [] 
    [ li (liStyles model.titre) [text "HTML"]
    , li (liStyles model.titre) [text "CSS"]
    , li (liStyles model.titre) [text "JS"]
    , li (liStyles model.titre) [text "JSON"]
    , li (liStyles model.titre) [text "NODE JS"]
    , li (liStyles model.titre) [text "MARKDOWN"]
    , li (liStyles model.titre) [text "PYHTON"]
    , li (liStyles model.titre) [text "RUBY"]
    , li (liStyles model.titre) [text "BASH"]
    , li (liStyles model.titre) [text "ELM"]
    , li (liStyles model.titre) [text "WINDEV"]
    , li (liStyles model.titre) [text "JAVA"]
    , li (liStyles model.titre) [text "KOTLIN"]
    , li (liStyles model.titre) [text "LUA"]
    , li (liStyles model.titre) [text "YML"]
    , li (liStyles model.titre) [text "TWIG"]
    , li (liStyles model.titre) [text "C#"]
    , li (liStyles model.titre) [text "C++"]
    , li (liStyles model.titre) [text "C"]
    , li (liStyles model.titre) [text "RUST"]
    , li (liStyles model.titre) [text "SQL"]
    , li (liStyles model.titre) [text "Assembleur"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Sécurité"]
    , ul [] 
    [ li (liStyles model.titre) [text "Clé SSH"]
    , li (liStyles model.titre) [text "Injection SQL - Requête préparée"]
    , li (liStyles model.titre) [text "Sauvegarde"]
    , li (liStyles model.titre) [text "Hachage et chiffrement de données"]
    , li (liStyles model.titre) [text "Gestion des utilisateurs"]
    , li (liStyles model.titre) [text "alerte"]
    , li (liStyles model.titre) [text "Oauth"]
    , li (liStyles model.titre) [text "Démarche de conformité au RGPD"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Autre"]
    , ul [] 
    [ li (liStyles model.titre) [text "3D"]
    , li (liStyles model.titre) [text "Montage vidéo"]
    , li (liStyles model.titre) [text "Retouche photo"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Qualité"]
    , ul [] 
    [ li (liStyles model.titre) [text "Passionné"]
    , li (liStyles model.titre) [text "Travail d'équipe"]
    , li (liStyles model.titre) [text "Autonome"]
    , li (liStyles model.titre) [text "Adaptation"]
    , li (liStyles model.titre) [text "Curieux"]
    , li (liStyles model.titre) [text "Organisé"]
    ]
    ]
    ]
    , div (colonnecompStyles model.titre) 
    [ div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Outils"]
    , ul [] 
    [ li (liStyles model.titre) [text "Nginx"]
    , li (liStyles model.titre) [text "Apache2"]
    , li (liStyles model.titre) [text "MariaDB"]
    , li (liStyles model.titre) [text "phpmyadmin"]
    , li (liStyles model.titre) [text "XAMPP & WAMP"]
    , li (liStyles model.titre) [text "Symfony"]
    , li (liStyles model.titre) [text "Visual Studio & Visual Studio Code"]
    , li (liStyles model.titre) [text "WordPress"]
    , li (liStyles model.titre) [text "Grafana"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Logiciel"]
    , ul [] 
    [ li (liStyles model.titre) [text "GitHub"]
    , li (liStyles model.titre) [text "Visual Studio"]
    , li (liStyles model.titre) [text "Visual Studio Code"]
    , li (liStyles model.titre) [text "SSMS"]
    , li (liStyles model.titre) [text "dbForge"]
    , li (liStyles model.titre) [text "Unity"]
    , li (liStyles model.titre) [text "PostMan"]
    , li (liStyles model.titre) [text "Cisco Packet Tracer"]
    , li (liStyles model.titre) [text "Wireshark"]
    , li (liStyles model.titre) [text "Virtual Box"]
    , li (liStyles model.titre) [text "WSL"]
    , li (liStyles model.titre) [text "Wondershare EdrawMax"]
    , li (liStyles model.titre) [text "Miro"]
    , li (liStyles model.titre) [text "Blender"]
    , li (liStyles model.titre) [text "Gimp"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Mise en place et développement"]
    , ul [] 
    [ li (liStyles model.titre) [text "API"]
    , li (liStyles model.titre) [text "base de donnée"]
    , li (liStyles model.titre) [text "Mise en place et configuration de switch, commutateur, borne WIFI"]
    , li (liStyles model.titre) [text "Déploiment GitHub"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "OS"]
    , ul [] 
    [ li (liStyles model.titre) [text "Windows"]
    , li (liStyles model.titre) [text "Linux"]
    , li (liStyles model.titre) [text "Androïd"]
    , li (liStyles model.titre) [text "Adaptation"]
    , li (liStyles model.titre) [text "Curieux"]
    , li (liStyles model.titre) [text "Organisé"]
    ]
    ]
    , div (colonneStyles model.titre) 
    [ h2 (h2Styles model.titre) [text "Navigateur"]
    , ul [] 
    [ li (liStyles model.titre) [text "Chrome"]
    , li (liStyles model.titre) [text "FireFox"]
    , li (liStyles model.titre) [text "WaterFox"]
    , li (liStyles model.titre) [text "Opera"]
    , li (liStyles model.titre) [text "SideKick"]
    , li (liStyles model.titre) [text "Brave"]
    , li (liStyles model.titre) [text "Edge"]
    , li (liStyles model.titre) [text "Visual Studio & Visual Studio Code"]
    , li (liStyles model.titre) [text "WordPress"]
    , li (liStyles model.titre) [text "GitHub"]
    ]
    ]
    ]
    ]
    ]

-- STYLES

styles : Model -> List (Attribute Msg)
styles model =
    [ style "background" "#2c3e50"
    , style "min-height" "100vh"
    ]

titleStyles : String -> List (Attribute Msg)
titleStyles titre =
    [ style "text-align" "center"
    , style "margin" "0"
    , style "padding" "20px 0 20px"
    , style "font-size" "600%"
    , style "color" "#ecf0f1"
    , style "text-shadow" "2px 2px 4px #000000"
    ]

headerStyles : String -> List (Attribute Msg)
headerStyles titre =
    [ style "width" "100%"
    , style "display" "flex"
    , style "justify-content" "center"
    ]

lienStyles : String -> List (Attribute Msg)
lienStyles titre =
    [ style "font-size" "200%"
    , style "color" "white"
    , style "text-decoration" "none"
    , style "margin" "1%"
    , style "padding" "1%"
    , style "border-radius" "15px"
    ]

bouton1Styles : String -> List (Attribute Msg)
bouton1Styles titre =
    [ style "background-color" "rgb(133, 92, 143)"]

bouton2Styles : String -> List (Attribute Msg)
bouton2Styles titre =
    [ style "background-color" "rgb(92, 95, 143)"]

bouton3Styles : String -> List (Attribute Msg)
bouton3Styles titre =
    [ style "background-color" "rgb(92, 135, 143)"]

bouton4Styles : String -> List (Attribute Msg)
bouton4Styles titre =
    [ style "background-color" "rgb(92, 143, 103)"]

bouton5Styles : String -> List (Attribute Msg)
bouton5Styles titre =
    [ style "background-color" "rgb(143, 140, 92)"]

sectionStyles : String -> List (Attribute Msg)
sectionStyles titre =
    [ style "display" "flex"
    , style "justify-content" "center"
    , style "flex-wrap" "wrap"
    ]

divStyles : String -> List (Attribute Msg)
divStyles titre =
    [ style "margin-top" "1%"
    , style "padding" "2%"
    , style "width" "70%"
    , style "color" "white"
    , style "background-color" "#1d2935"
    , style "border" "3px white solid"
    , style "border-radius" "20px"
    ]

h2Styles : String -> List (Attribute Msg)
h2Styles titre =
    [ style "text-align" "center"
    , style "font-size" "400%"
    , style "color" "#ecf0f1"
    , style "text-shadow" "2px 2px 4px #000000"
    ]

pStyles : String -> List (Attribute Msg)
pStyles titre =
    [ style "font-size" "150%" ]

imgStyles : String -> List (Attribute Msg)
imgStyles titre =
    [  style "width" "15vh"
    ,  style "border-radius" "10px" ]

liendocStyles : String -> List (Attribute Msg)
liendocStyles titre =
    [ style "display" "flex"
    , style "justify-content" "space-evenly" ]

colonneStyles : String -> List (Attribute Msg)
colonneStyles titre =
    [ style "background-color" "#1d2935"
    , style "border" "3px white solid"
    , style "border-radius" "20px"
    , style "margin" "2%"
    , style "margin-top" "5%"]


colonnecompStyles : String -> List (Attribute Msg)
colonnecompStyles titre =
    [ style "display" "inline-block"
    , style "width" "40%"
    , style "height" "0%"]

liStyles : String -> List (Attribute Msg)
liStyles titre =
    [ style "font-size" "150%"
    , style "margin-left" "30%"
    , style "color" "#2BD6B4" ]

-- MAIN

main =
    Browser.sandbox { init = init, update = update, view = view }