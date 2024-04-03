
module Main exposing (..)

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
    ]


-- STYLES

styles : Model -> List (Attribute Msg)
styles model =
    [ style "background" "#2c3e50"
    , style "height" "100vh"
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


-- MAIN

main =
    Browser.sandbox { init = init, update = update, view = view }
