module Projet exposing (..)

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
        [ div (divStyles model.titre) 
        [ h2 (h2Styles model.titre) [text "Mes projets"]
        , span (List.concat [liendocStyles model.titre, projetStyles model.titre]) 
        [ a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "BugSafari" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "BOT veille informatique " ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "API" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "blague joke API" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "pokedex viewer" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "Super Simon" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "blender" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "les frelots" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "tirage randome" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "Pikmin Parking Map" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "Destination Culture" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "où est la station spatiale internationale ISS" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "Flash Badge" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "mes petits passe temps" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "WINDEV" ]
        , a (List.concat [acolorStyles model.titre, [href "#"]]) [ text "AdminTypeDevis" ]
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
    , style "font-size" "450%"
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

acolorStyles : String -> List (Attribute Msg)
acolorStyles titre =
    [ style "text-decoration" "none"
    , style "color" "#2BD6B4"
    , style "width" "28%"
    , style "text-align" "center"
    , style "padding" "2%" ]

liStyles : String -> List (Attribute Msg)
liStyles titre =
    [ style "font-size" "200%"
    , style "margin-left" "37%"
    , style "color" "#2BD6B4" ]

projetStyles : String -> List (Attribute Msg)
projetStyles titre =
    [ style "font-size" "200%"
    , style "color" "#2bc2d6"
    , style "display" "flex"
    , style "justify-content" "space-around"
    , style "align-items" "center"
    , style "flex-wrap" "wrap"]

-- MAIN

main =
    Browser.sandbox { init = init, update = update, view = view }
