module Bot exposing (..)

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
        [ h2 (h2Styles model.titre) [text "Bot veille"]
        , span (liendocStyles model.titre) [ a [target "_blank", href "https://github.com/johanvadenne/Bot-veille-discord"] [ img (List.concat [imgStyles model.titre, [src "./assets/images/johan.png"]]) [] ]]
        , p (pStyles model.titre) [text "Son objectif principal est de nous tenir informé des dernières actualités en informatique (ou autre domaine)."]
        , p (pStyles model.titre) [text "Ce bot est configuré pour surveiller plusieurs sites web spécifiques, et lorsqu'il détecte une nouvelle actualité, il la diffuse dans trois canaux distincts :"]
        , p (pStyles model.titre) [text "tout d'abord, dans le canal dédié au site, ensuite dans le canal correspondant à la catégorie de l'actualité, et enfin dans un canal où toutes les actualités sont répertoriées."]
        , a (List.concat [pStyles model.titre, acolorStyles model.titre , [target "_blank", href "https://github.com/johanvadenne/Bot-veille-discord"]]) [ text "lien ici" ]
        , h2 (h2Styles model.titre) [text "Mes sources"]
        , span [] 
        [ ul [] 
        [ li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.lemondeinformatique.fr/"]]) [text "lemondeinformatique"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.clubic.com/"]]) [text "clubic"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.usine-digitale.fr/"]]) [text "usine-digitale"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.zdnet.fr/"]]) [text "zdnet"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.nextinpact.com/"]]) [text "nextinpact"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.generation-nt.com/"]]) [text "generation-nt"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.lesnumeriques.com/"]]) [text "lesnumeriques"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.numerama.com/"]]) [text "numerama"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.fredzone.org/"]]) [text "fredzone"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.presse-citron.net/"]]) [text "presse-citron"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.ginjfo.com/"]]) [text "ginjfo"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://vonguru.fr/"]]) [text "vonguru"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.journaldugeek.com/"]]) [text "journaldugeek"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.tomsguide.fr/"]]) [text "tomsguide"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://leclaireur.fnac.com/"]]) [text "fnac"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.01net.com/"]]) [text "01net"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://korben.info/"]]) [text "korben"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.cowcotland.com/"]]) [text "cowcotland"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.futura-sciences.com/"]]) [text "futura-sciences"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://techdows.com/"]]) [text "techdows"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.tomshardware.fr/"]]) [text "tomshardware"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://journalducoin.com/"]]) [text "journalducoin"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://overclocking.com/"]]) [text "overclocking"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.maison-et-domotique.com/"]]) [text "maison-et-domotique"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.minimachines.net/"]]) [text "minimachines"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://3dvf.com/"]]) [text "3dvf"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.cachem.fr/"]]) [text "cachem"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.touslesdrivers.com/"]]) [text "touslesdrivers"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.lesmobiles.com/"]]) [text "lesmobiles"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.mac4ever.com/"]]) [text "mac4ever"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.macg.co/"]]) [text "macg"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.frandroid.com/"]]) [text "frandroid"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://macbidouille.com/"]]) [text "macbidouille"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.iphon.fr/"]]) [text "iphon"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.toolinux.com/"]]) [text "toolinux"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.tablette-tactile.net/"]]) [text "tablette-tactile"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://linuxfr.org/"]]) [text "linuxfr"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.universfreebox.com/"]]) [text "universfreebox"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.monwindows.com/"]]) [text "monwindows"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.lemagit.fr/"]]) [text "lemagit"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.usinenouvelle.com/"]]) [text "usinenouvelle"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.silicon.fr/"]]) [text "silicon"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.lebigdata.fr/"]]) [text "lebigdata"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.larevuedudigital.com/"]]) [text "larevuedudigital"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.programmez.com/"]]) [text "programmez"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.legalis.net/"]]) [text "legalis"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.zataz.com/"]]) [text "zataz"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.gamekult.com/"]]) [text "gamekult"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.xbox-gamer.net/"]]) [text "xbox-gamer"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.psmag.fr/"]]) [text "psmag"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.jeuxvideo.com/"]]) [text "jeuxvideo"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.p-nintendo.com/"]]) [text "p-nintendo"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.gameblog.fr/"]]) [text "gameblog"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.factornews.com/"]]) [text "factornews"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.jeuxonline.info/"]]) [text "jeuxonline"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.hdnumerique.com/"]]) [text "hdnumerique"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.allocine.fr/"]]) [text "allocine"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.avcesar.com/"]]) [text "avcesar"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.premiere.fr/"]]) [text "premiere"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "https://www.ecranlarge.com/"]]) [text "ecranlarge"]]
        , li (liStyles model.titre) [a (List.concat [acolorStyles model.titre, [target "_blank", href "http://www.journaldujapon.com/"]]) [text "journaldujapon"]]
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
    , style "color" "#2BD6B4" ]

liStyles : String -> List (Attribute Msg)
liStyles titre =
    [ style "font-size" "200%"
    , style "margin-left" "37%"
    , style "color" "#2BD6B4" ]

-- MAIN

main =
    Browser.sandbox { init = init, update = update, view = view }
