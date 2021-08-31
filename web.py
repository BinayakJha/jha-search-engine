from re import S
import pandas
from logging import PlaceHolder
from numpy.lib.function_base import place
import requests
import urllib
import pandas as pd
from requests.api import get
from requests_html import HTML
from requests_html import HTMLSession
import streamlit as st
import people_also_ask

st.set_page_config(page_title="Jha Browser")
st.markdown("""
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)
# css
st.markdown("""
<style>@import url('@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
*{overflow-y:hidden;font-family: 'Poppins', sans-serif;}
body {
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}
.css-1u0jg5e {visibility: hidden;}
</style>""", unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stConnectionStatus{visibility: hidden;}
            .viewerBadge_container__1QSob {visibility: hidden !important;}
            svg .css-xq1lnh-EmotionIconBase  {visibility: hidden !important;}
            .css-o9wq0b {visibility: hidden !important;}
            .css-31hhpn {visibility: hidden !important;}
             body { overflow-x:hidden;overflow-y:hidden; }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# images
st.markdown("""
<div class='images1'>
</div>
<div class='images2'>
</div>
<div class='images3'>
</div>
<!--bottom images-->
<div class='bottom_images1'>
</div>
<div class='bottom_images2'>
</div>
<div class='bottom_images3'>
</div>
<style>
.images1{
    position: absolute;
    width: 187px;
    height: 187px;
    left: 927px;
    top: -219px;
    background: url('https://thumbs.dreamstime.com/b/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg'), #C4C4C4;
    border: 7px solid #FFFFFF;
    border-radius: 8px;
}
.images2{
    width: 241px;
    height: 241px;
    left: 1359px;
    top: 67px;
    margin:-134px 67.5vw;
    background: url('https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg'), #C4C4C4;
    border: 7px solid #FFFFFF;
    border-radius: 8px; 
}
.images3{
    position: absolute;
    width: 70px;
    height: 70px;
    background: url('https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg'), #C4C4C4;
    border: 9px solid #FFFFFF;
    border-radius: 8px;
    margin:98px 78.5vw 0 72.5vw;
}
.bottom_images1{
    position: absolute;
    width: 123px;
    height: 123px;
    left: -61px;
    top: 706px;
    background: url('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'), #C4C4C4;
    border: 9px solid #FFFFFF;
    border-radius: 8px;
    margin:-216px -222px;
    z-index: 1;
}
.bottom_images2{
    position: absolute;
    width: 347px;
    height: 347px;
    left: -86px;
    top: 768px;
    background: url('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'), #C4C4C4;
    border-radius: 8px;
    margin:-200px -320px;
}
.bottom_images3{
    position: absolute;
    width: 79px;
    height: 79px;
    left: -61px;
    top: 830px;
    background: url('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'), #C4C4C4;
    border: 9px solid #FFFFFF;
    border-radius: 8px;
    margin:-190px -20px;
}
@media screen and (min-width:1580px) {
    .images1 {
    position: absolute;
    width: 187px;
    height: 187px;
    left: 1022px;
    top: -219px;
    background: url(https://thumbs.dreamstime.com/b/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg), #C4C4C4;
    border: 7px solid #FFFFFF;
    border-radius: 8px;
    }
}   
@media screen and (min-width:2560px) {
    .images1 {
    position: absolute;
    width: 187px;
    height: 187px;
    left: 1504px;
    top: -219px;
    background: url(https://thumbs.dreamstime.com/b/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg), #C4C4C4;
    border: 7px solid #FFFFFF;
    border-radius: 8px;
}
    .images3 {
        position: absolute;
        width: 70px;
        height: 70px;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: 78px 64.5vw 0px 64.5vw;
    }
 .images2 {
    width: 241px;
    height: 241px;
    left: 1356px;
    top: 67px;
    margin: -119px 61.5vw;
    background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
    border: 7px solid #FFFFFF;
    border-radius: 8px;
}
.bottom_images1 {
        position: absolute;
        width: 123px;
        height: 123px;
        left: -521px;
        top: 1278px;
        background: url(https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: -216px -222px;
        z-index: 1;
    }
.bottom_images2 {
        position: absolute;
        width: 347px;
        left: -567px;
        top: 1357px;
        background: url(https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg), #C4C4C4;
        border-radius: 8px;
        margin: -200px -320px;
    }
.bottom_images3 {
        position: absolute;
        width: 79px;
        height: 79px;
        left: -541px;
        top: 1472px;
        background: url(https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: -190px -20px;
    }
}

</style>""", unsafe_allow_html=True)

# <p style='text-align:center;font-size:1.3em;'>Fast, Secure, Full privacy control to the user, Non tracking Browser</p><p  style='text-align:center;margin-bottom:-2px;font-size:1.1em;'>Search Here!!</p>
placeholder = st.markdown("<h1 style='text-align: center;justify-content:center;margin-top:-60px;font-size:96px !important;letter-spacing: -0.02em !important;font-weight: 600 !important;' id = 'heading'>Jha Browser</h1><p></p>", unsafe_allow_html=True)


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)



query = st.text_input("",)
# replace spaces with +
query = query.replace(" ", "+")
button = """
    <style>
.st-df {
    padding: 10px;
}

.st-cn {
    padding: 20px;
    border-radius: 5px;
    background-color: #ee7274 !important;
    font-size: 1.2em;
    font-family: 'Poppins', sans-serif;
}

.stCheckbox span {
    visibility: hidden;
}


.css-1ubkpyc {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
}

.css-lybem {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
    border: 1px solid red;
    box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
}

.css-qbe2hs {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
    border: 1px solid red;
}

.css-n19jqu:hover {
    background: #ee7274 !important;
    color: black !important;
}

.css-n19jqu {
    margin: 34px 41.5%;
    padding: 19px 58px !important;
    border: 1px solid red;
    box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
    background: #ee7274 !important;
    color: white;
}

.st-br {
    border: 1px solid grey;
    border-bottom-color: grey;
    padding: 8px !important
}

.st-bc {
    padding: 8px !important;
    background: transparent
}

.st-go {
    background: transparent !important;
}

.st-bs {
    background: transparent !important;
}

.st-bx {
    background: transparent !important;
}

.st-bu {
    background: transparent !important;
}

.st-cz {
    background: transparent !important;
}

.st-cl {
    padding: 8px !important;
}

.st-bg {
    padding: 8px !important;
}

.st-bv {
    background: transparent !important;
}


#heading {
    height: 144px;
    left: 550px;
    top: 386px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 600;
    font-size: 96px;
    line-height: 185px;
    letter-spacing: -0.02em;
}

.stButton {
    margin: 0px !important;
}

.css-1ko0gb7 {
    margin: 0px 0px 1rem !important;
}

.css-hi6a2p {
    max-width: 1000px !important;
    padding: 2.5rem 1.5rem 6rem !important;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
b,
i {
    color: black !important;
    font-family: 'Poppins', sans-serif !important;
}

.css-ip91b3 {
    width: 20.5rem !important;
}

.css-pday0i {
    width: 21.5rem !important;
    background: white !important;
    margin: 10px 10px;
    border-radius: 5px;
}
.css-wot580{
    margin:6px 6px;
}
}
a {
    color: #1a0dab !important;
    text-decoration: none !important;
}

.css-hi6a2p {
    flex: 1 1 0%;
    width: 100%;
    padding: 2.5rem 1rem 6rem;
    max-width: 730px;
    margin: 53px;
    border-radius: 5px;
}

hr {
    margin: 1em 3px;
    padding: 0px;
    color: inherit;
    background-color: transparent;
    border-top: none;
    border-right: none;
    border-left: none;
    border-image: initial;
    border-bottom: 21px solid #f0f5f7 !important;
    margin: 12px -32px;
    border-radius: 5px;
}

.css-feqc82 {
    position: relative;
    width: 584px;
    justify-content: center;
    left: 188px;
    top: 34px;
}

.css-1bi8zkq {
    width: 518px;
    margin: 7vh 0vw 0 4vw !important;
}

@media screen and (max-width: 530px) {
    .css-n19jqu {
        margin: 0 22.5% !important;
    }
}

.css-1v3fvcr {
    overflow-x: hidden;
    overflow-y: hidden;
}

.stCheckbox label {
    position: absolute;
    width: 69px;
    height: 69px;
    left: 1001px;
    top: 105px;
    border-radius: 10px;
    border: 1px solid #151515;
}

/* # mobile responsive  */
@media screen and (min-width: 1290px) {
    .stCheckbox label {
        left: 993px;
        top: 45px;
    }
}

.st-bu {
    background: transparent !important;
}

.stCheckbox span {
    position: absolute;
}

.css-1djdyxw {
    margin: 19px 14px !important;
    font-size: 48px;
    color: #ffffff;
    font-family:system-ui;
}
.css-vuszbj {
    margin-bottom: 0px !important;
    height: 0px !important;
}
@media screen and (max-width: 313px) {
    .css-n19jqu {
    margin: 16px 6.5% !important;
    }
    .st-bg {
    padding: 6px !important;
    }
    #heading {
        margin-top: -19px !important;
        font-size: 36px !important;
    }
    .images2 {
        width: 232px;
        height: 241px;
        left: 1359px;
        top: 67px;
        margin: -242px 67.5vw;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 7px solid #FFFFFF;
        border-radius: 8px;
    }

    .images3 {
        position: absolute;
        width: 70px;
        height: 70px;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: 125px 75.5vw 0 60.5vw;
    }
}
@media screen and (min-width:314px) and (max-width: 405px) {
    #heading{
        margin-top: -19px !important;
        font-size: 45px !important
    }
    .css-n19jqu {
    margin: 16px 18.5% !important;
    }
     .images2 {
        width: 232px;
        height: 241px;
        left: 1359px;
        top: 67px;
        margin: -242px 67.5vw;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 7px solid #FFFFFF;
        border-radius: 8px;
    }

    .images3 {
        position: absolute;
        width: 70px;
        height: 70px;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: 125px 75.5vw 0 60.5vw;
    }
}  
@media screen and (min-width: 435px) and (max-width: 500px) { 
    #heading{
        margin-top: -19px !important;
        font-size: 61px !important
    }
}
  
@media screen and (min-width: 406px) and (max-width: 531px) {
    #heading{
        margin-top: -19px !important;
        font-size: 55px !important;
}
@media screen and (max-width: 530px) {
    .css-n19jqu {
        margin: 15px 22.5% !important;
    }
}

@media screen and (min-width: 767px) {
    #heading {
        margin-top: -19px !important;
        font-size: 66px !important;
    }
    .stButton{
        margin:-35px 6px !important;
    }
}

    .css-n19jqu {
        margin: 34px 36.5% !important;
        padding: 19px 58px !important;
        border: 1px solid red;
        box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
        background: #ee7274 !important;
        color: white;
    }

    .images2 {
        width: 232px;
        height: 241px;
        left: 1359px;
        top: 67px;
        margin: -242px 67.5vw;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 7px solid #FFFFFF;
        border-radius: 8px;
    }

    .images3 {
        position: absolute;
        width: 70px;
        height: 70px;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: 125px 75.5vw 0 60.5vw;
    }
}
@media screen and (min-width: 1920px)  and (max-width: 2500px) {
    .images1 {
        position: absolute;
        width: 187px;
        height: 187px;
        left: 1210px;
        top: -219px;
        background: url(https://thumbs.dreamstime.com/b/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg), #C4C4C4;
        border: 7px solid #FFFFFF;
        border-radius: 8px;
    }

    .images2 {
        width: 241px;
        height: 241px;
        left: 1359px;
        top: 67px;
        margin: -134px 67.5vw;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 7px solid #FFFFFF;
        border-radius: 8px;
    }

    .images3 {
        position: absolute;
        width: 70px;
        height: 70px;
        background: url(https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: 98px 78.5vw 0 72.5vw;
    }

    .bottom_images1 {
        position: absolute;
        width: 123px;
        height: 123px;
        left: -179px;
        top: 933px;
        background: url(https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: -216px -222px;
        z-index: 1;
    }

    .bottom_images2 {
        position: absolute;
        width: 347px;
        height: 347px;
        left: -207px;
        top: 992px;
        background: url(https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg), #C4C4C4;
        border-radius: 8px;
        margin: -200px -320px;
    }

    .bottom_images3 {
        position: absolute;
        width: 79px;
        height: 79px;
        left: -188px;
        top: 1088px;
        background: url(https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg), #C4C4C4;
        border: 9px solid #FFFFFF;
        border-radius: 8px;
        margin: -190px -20px;
    }

    #heading {
        margin-top: 142px !important;
    }
}
    </style>
    """
st.markdown(button, unsafe_allow_html=True)
st.markdown(''' 
<style>
@media screen and (min-width: 768px) and (max-width: 999px) {
    .images1 {
        left: 430px !important;
        top: -240px !important;
    }
    .images2 {
        margin:-197px 67.5vw !important;
    }
    .images3 {
        margin:127px 78.5vw 0 78.5vw !important;
    }
    #heading {
        font-size: 70px !important;
        margin-top: -46px !important;
    }
    .css-n19jqu {
        margin: -24px 38.5% !important;
    }
}
@media screen and (min-width: 1001px) and (max-width: 1200px) {
    .css-n19jqu {
        margin: 14px ​40.5% !important;
    }
    .images2 {
        margin:-211px 75.5vw !important;
    }
}

@media screen and (min-width: 2560px) {
    .stCheckbox label {
        left: 1129px;
        top: 176px;
    }
    .css-n19jqu {
        margin: 65px 41.5% !important;
    }

    .css-feqc82 {
        top: 51px !important;
    }

    #heading {
        margin-top: 250px !important;

    }
}
</style>
''', unsafe_allow_html=True)
st.button("Search")
changer = st.checkbox("◐")
if changer == True:
    st.markdown("""
            <style>
    .st-em {background-color: rgb(14 14 14) !important;}
    span{color: #ffffff !important;}        
    .st-ef {fill: rgb(255, 255, 255) !important;}
    .css-1djdyxw {
    margin: 19px 14px !important;
    font-size: 48px;
    color: #ffffff;
    transform: scale3d(1.5, 1.5, 1.5);
}

.stCheckbox label {
    border: 1px solid #151515;
}

.css-1h8rjc8 {
    background: #131313 !important;
}

.st-df {
    padding: 10px;
}

.st-cn {
    padding: 20px 0px;
    border-radius: 5px;
    background-color: #ee7274 !important;
    font-size: 1.2em;
    font-family: 'Poppins', sans-serif;
}

.css-1ubkpyc {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
}

.css-lybem {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
    border: 1px solid red;
    box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
}

.css-qbe2hs {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
    border: 1px solid red;
}

.css-n19jqu:hover {
    background: #ee7274 !important;
    color: white !important;
}

.css-n19jqu {
    margin: 34px 41.5%;
    padding: 19px 58px !important;
    border: 1px solid red;
    box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
    background: #ee7274 !important;
    color: black;
}

.st-br {
    padding: 8px !important;
    border: 1px solid #25282E;
}

.st-bc {
    padding: 8px !important;
    background: #0D0D0D;
    color: white;
}

.st-go {
    background: #0D0D0D !important;
    color: white;
}

.st-bs {
    background: #0D0D0D !important;
    color: white;
}

.st-bx {
    background: #0D0D0D !important;
    color: white;
}

.st-cl {
    padding: 8px !important;
}

.st-bg {
    padding: 8px !important;
}

.st-bv {
    background: #0D0D0D !important;
    border:none;
}

#heading {
    height: 144px;
    left: 550px;
    top: 386px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 600;
    font-size: 96px;
    line-height: 185px;
    letter-spacing: -0.02em;
}

.stButton {
    margin: 0px !important;
}

.css-1ko0gb7 {
    margin: 0px 0px 1rem !important;
}

.css-hi6a2p {
    max-width: 1000px !important;
    padding: 2.5rem 1.5rem 6rem !important;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
b,
i {
    color: #FFFFFF !important;
    font-family: 'Poppins', sans-serif !important;
}

.css-ip91b3 {
    width: 22rem !important;
}

.css-pday0i {
    width: 21.5rem !important;
    background: #242731 !important;
}

a {
    color: #6da7ff !important;
    text-decoration: none;
}

.css-hi6a2p {
    flex: 1 1 0%;
    width: 100%;
    padding: 2.5rem 1rem 6rem;
    max-width: 730px;
    margin: 53px;
    border-radius: 5px;
}

hr {
    margin: 1em 3px;
    padding: 0px;
    color: inherit;
    background-color: transparent;
    border-top: none;
    border-right: none;
    border-left: none;
    border-image: initial;
    border-bottom: 21px solid #131313 !important;
    margin: 12px -32px;
    border-radius: 5px;
}

.css-feqc82 {
    position: relative;
    width: 584px;
    justify-content: center;
    left: 188px;
    top: 34px;
}

.css-1bi8zkq {
    width: 518px;
    margin: 7vh 0vw 0 4vw !important;
}

@media screen and (max-width: 530px) {
    .css-n19jqu {
        margin: 0 22.5% !important;
    }
}

.css-1v3fvcr {
    overflow-x: hidden;
    overflow-y: hidden;
}

.images1 {
    position: absolute;
    width: 187px;
    height: 187px;
    left: 927px;
    top: -219px;
    background: url('https://thumbs.dreamstime.com/b/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg'), #C4C4C4;
    border: 7px solid #131313;
    border-radius: 8px;
}

.images2 {
    width: 241px;
    height: 241px;
    left: 1359px;
    top: 67px;
    margin: -134px 67.5vw;
    background: url('https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg'), #C4C4C4;
    border: 7px solid #131313;
    border-radius: 8px;
}

.images3 {
    position: absolute;
    width: 70px;
    height: 70px;
    background: url('https://st.depositphotos.com/1428083/2946/i/600/depositphotos_29460297-stock-photo-bird-cage.jpg'), #C4C4C4;
    border: 9px solid #131313;
    border-radius: 8px;
    margin: 98px 78.5vw 0 72.5vw;
}

.bottom_images1 {
    position: absolute;
    width: 123px;
    height: 123px;
    left: -61px;
    top: 706px;
    background: url('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'), #C4C4C4;
    border: 9px solid #131313;
    border-radius: 8px;
    margin: -216px -222px;
    z-index: 1;
}

.bottom_images2 {
    position: absolute;
    width: 347px;
    height: 347px;
    left: -86px;
    top: 768px;
    background: url('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'), #C4C4C4;
    border-radius: 8px;
    margin: -200px -320px;
}

.bottom_images3 {
    position: absolute;
    width: 79px;
    height: 79px;
    left: -61px;
    top: 830px;
    background: url('https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg'), #C4C4C4;
    border: 9px solid #131313;
    border-radius: 8px;
    margin: -190px -20px;
}
</style>""", unsafe_allow_html=True)

# while changing the theme add some transition
elif changer == False:
    st.markdown("""<style>
                  .css-1djdyxw {
    margin: 19px 14px !important;
    font-size: 48px;
    color: black;
    transform: scale3d(1.5, 1.5, 1.5);
}

.stCheckbox label {
    border: 1px solid #EEF6FF;
}

.st-df {
    padding: 10px;
}

.st-cn {
    padding: 20px;
    border-radius: 5px;
    background-color: #ee7274 !important;
    font-size: 1.2em;
    font-family: 'Poppins', sans-serif;
}

.css-1ubkpyc {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
}

.css-lybem {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
    border: 1px solid red;
    box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
}

.css-qbe2hs {
    margin: 21px -1px;
    padding: 18px 35px 14px 35px;
    border: 1px solid red;
}

.css-n19jqu:hover {
    background: #ee7274 !important;
    color: black !important;
}

.css-n19jqu {
    margin: 34px 41.5%;
    padding: 19px 58px !important;
    border: 1px solid red;
    box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;
    background: #ee7274 !important;
    color: white;
}

.st-br {
    padding: 8px !important
}

.st-bc {
    padding: 8px !important;
    background: transparent
}

.st-go {
    background: transparent !important;
}

.st-bs {
    background: transparent !important;
}

.st-bx {
    background: transparent !important;
}

.st-bu {
    background: transparent !important;
}

.st-cz {
    background: transparent !important;
}

.st-cl {
    padding: 8px !important;
}

.st-bg {
    padding: 8px !important;
}

.st-bv {
    background: transparent !important;
    border: none !important;
}
#heading {
    height: 144px;
    left: 550px;
    top: 386px;
    font-family: Poppins;
    font-style: normal;
    font-weight: 600;
    font-size: 96px;
    line-height: 185px;
    letter-spacing: -0.02em;
}

.css-1djdyxw {
    margin: 10px 53px;
}

.stButton {
    margin: 0px !important;
}

.css-1ko0gb7 {
    margin: 0px 0px 1rem !important;
}

.css-hi6a2p {
    max-width: 1000px !important;
    padding: 2.5rem 1.5rem 6rem !important;
}

h1,
h2,
h3,
h4,
h5,
h6,
p,
b,
i {
    color: black !important;
    font-family: 'Poppins', sans-serif !important;
}

.css-ip91b3 {
    width: 22rem !important;
}

.css-pday0i {
    width: 21.5rem;
    background: white !important;
}

a {
    color: #1a0dab !important;
    text-decoration: none !important;
}

.css-hi6a2p {
    flex: 1 1 0%;
    width: 100%;
    padding: 2.5rem 1rem 6rem;
    max-width: 730px;
    margin: 53px;
    border-radius: 5px;
}

hr {
    margin: 1em 3px;
    padding: 0px;
    color: inherit;
    background-color: transparent;
    border-top: none;
    border-right: none;
    border-left: none;
    border-image: initial;
    border-bottom: 21px solid #f0f5f7 !important;
    margin: 12px -32px;
    border-radius: 5px;
}

.css-feqc82 {
    position: relative;
    width: 584px;
    justify-content: center;
    left: 188px;
    top: 34px;
}

.css-1bi8zkq {
    width: 518px;
    margin: 7vh 0vw 0 4vw !important;
}

@media screen and (max-width: 530px) {
    .css-n19jqu {
        margin: 0 22.5% !important;
    }
}

.css-1v3fvcr {
    overflow-x: hidden;
    overflow-y: hidden;
}
            </style>""", unsafe_allow_html=True)

#  on click change to dark theme
# st.markdown("<p style='margin:-396px 791px 0px -15px;z-index:0;color:black;'>hello</p>", unsafe_allow_html=True)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links


def get_results(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    # replace whitespace with +
    query = query.replace(" ", "+")
    return response


def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = ".yuRUbf h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"
    # related search tab
    css_identifier_featured = ".GyAeWb"
    results = response.html.find(css_identifier_result)
    # related search tab

    output = []

    for result in results:
        item = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_link, first=True).attrs['href'],
            'text': result.find(css_identifier_text, first=True).text,
        }

        output.append(item)

    return output

def youtube_videos(query):
    query = urllib.parse.quote_plus(query)
    response2 = get_source(f"https://www.google.com/search?q={query}&sxsrf=AOaemvK8imeKYLRhi4mg-vzXoQ1_XPxwlA:1630319960797&source=lnms&tbm=vid&sa=X&ved=2ahUKEwjtlIiRx9jyAhWegtgFHcjcDR4Q_AUoAnoECAEQBA&biw=1366&bih=693")
    return response2

# youtube videos functions
def parse_youtube_videos(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = ".LC20lb"
    css_identifier_description = ".aCOpRe"
    css_identifier_time = ".fG8Fp"

    results = response.html.find(css_identifier_result)
    output2 = []
    for result in results:
        item2 = {
            'title': result.find(css_identifier_title, first=True).text,
            'link': result.find(css_identifier_title, first=True).attrs['href'],
            'description': result.find(css_identifier_description, first=True).text,
            'time': result.find(css_identifier_time, first=True).text,
        }
        output2.append(item2)
        return output2

def youtube_google_search(query):
    response2 = youtube_videos(query)
    return parse_youtube_videos(response2)
def google_search(query):
    response = get_results(query)
    return parse_results(response)


results = google_search(query)
# favicons

# export results to csv file


# youtube
# if youtube.com in link then cut the link and take out watch?v =

# -59px ​0
# end youtube

if query:
    placeholder.empty()
    if changer ==True:
        st.markdown("""<style>
         .css-hi6a2p{background-color:#242731 !important;}
         .st-em {background-color: rgb(14 14 14) !important;}
         span{color: #ffffff !important;}
         </style>
         """, unsafe_allow_html=True)
    else:
        st.markdown("""<style>
         .css-hi6a2p{background-color:white !important}
         </style>
         """, unsafe_allow_html=True)
    st.markdown("""<style>
       .css-1v3fvcr {
    overflow-x: hidden;
    overflow-y: auto;
}

.images1,
.images2,
.images3,
.bottom_images1,
.bottom_images2,
.bottom_images3 {
    display: none;
}

.css-n19jqu {
    margin: -75px 74.5%;
    position: absolute;
}

.css-feqc82 {
    top: 22px;
    left: 114px;
}

.stCheckbox {
    width: 100px;
    position: absolute;
    visibility: hidden;
}
.st-ei{
    width:0px !important;
}
.st-ef {
    width: 0px !important;
}
@media screen and (min-width: 2000px) {
    .css-n19jqu {
        margin: -46px 74.5% !important;
    }
}

.css-hlxwf4 {
    margin: -59px 0 !important;
}

@media screen and (max-width: 1000px) {
    .css-n19jqu {
        margin: -97px 72.5%;
    }
}
@media screen and (min-width: 1000px) {
    .css-n19jqu {
        margin:-58px 74.5% !important;
    }

}
@media screen and (max-width: 2560px) {
    .css-feqc82 {
        top:71px !important;
    }
}

     </style>""", unsafe_allow_html=True)
   
    menu = ["All","Images","Videos","News","Info"]
    choice = st.selectbox("", menu)
    if choice == "All":
        try:
            try:
            
                col1, col2 = st.columns([0.5, 6])
                with col2:
                    st.header('Featured answer :')
                    featured_answer = people_also_ask.get_simple_answer(query)
                    if "youtube.com/watch?v" in featured_answer:
                        url = featured_answer
                        session = HTMLSession()
                        response = session.get(url)
                        title = response.html.find('title', first=True).text
                        featured_answer1 = featured_answer.split(
                            "youtube.com/watch?v=")[1]
                        yt_url1 = f"https://i.ytimg.com/vi/{featured_answer1}/0.jpg"
                        st.markdown(f'<a href="{yt_url1}" target="_blank"><iframe height="400" src="https://www.youtube.com/embed/{featured_answer1}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style = "width:90%;border-radius:5px;"></iframe></a>', unsafe_allow_html=True)
                        st.header(f"[{title}]({featured_answer})")
                
                    else:
                        st.markdown(featured_answer, unsafe_allow_html=True)
                    if featured_answer == "":
                        try:
                            # replace meaning of or defination of with space
                            if "meaning of" in query:
                                query = query.replace("meaning of", "")
                            if "defination of" in query:
                                query = query.replace("defination of", "")
                            # replace the word with space
                            if " " in query:
                                query = query.replace(" ", "")
                            if 'meaning' in query:
                                query = query.replace('meaning', "")
                            if 'defination' in query:
                                query = query.replace('defination', "")
                            if 'what is' in query:
                                query = query.replace('what is', "")
                            if 'What is' in query:
                                query = query.replace('What is', "")

                            url = "https://www.vocabulary.com/dictionary/" + query
                            session = HTMLSession()
                            response = session.get(url)
                            defination = response.html.find(
                                '.definition', first=True).text
                            defination2 = response.html.find(
                                '.pos-icon', first=True).text
                            # remove defination2 text from defination
                            defination = defination.replace(defination2, "")
                            st.markdown(
                                f'<p><b>{defination2}</b> → {defination}</p>', unsafe_allow_html=True)
                            
                        except:
                            pass


                st.markdown('---')
                st.write("\n")
            except:

                pass
            df = pandas.DataFrame(results)

            title = df['title']
            link = df['link']
            text = df['text']
            link2 = df['link']
            try:

                favicon = df['favicon']
            except:
                favicon = ""

            # write title then link and then text
            # add link inside the title
            for i in range(len(title)):

                col1, col2 = st.columns([0.5, 6])
                # add style
                style = """
                <style>
                .css-1v0mbdj{
                    margin: 8px 2px;
                }
                .css-1v0mbdj img{
                    border-radius:5px;
                }
                .css-vtsuw1{
                    bottom: 10px;    
                }
                """
                st.markdown(style, unsafe_allow_html=True)

                # st.link(title[i], link[i])
                with col1:
                    try:
                        favicon_url = "https://www.google.com/s2/favicons?sz=64&domain_url=" + link[i]
                        st.image(favicon_url, width=32)
                    except:
                        pass

                with col2:

                    st.header(f"[{title[i]}]({link[i]})")
                col1, col2 = st.columns([0.5, 6])
                # If youtube in favicon url then show image
                # if image is not loaded then pass
                if "youtube.com" in favicon_url:
                    col1, col2 = st.columns([6, 2])
                    with col1:
                        st.markdown(f'{text[i][0:300]}')
                    with col2:

                        if "/watch?v" in link[i]:
                            link3 = link[i][32:]
                            yt_url = f"https://i.ytimg.com/vi/{link3}/0.jpg"
                            st.markdown(
                                f"<img src ='{yt_url}' style='width: 100%;border-radius:5px;'>", unsafe_allow_html=True)
                        # if not then leave the space
                else:
                    st.markdown(f'{text[i][0:500]}')
                st.markdown("---")
                st.write("\n")
        except:
            st.error("Sorry, No results found :( Please try another query")
        try:
            url = "https://search.brave.com/search?q="+query
            st.markdown(
                "<style> html{font-family: -apple-system,system-ui,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',sans-serif;}</style>", unsafe_allow_html=True)
            try:
                session = HTMLSession()
                response = session.get(url)

            except requests.exceptions.RequestException as e:
                print(e)

            title1 = response.html.find('.infobox-title')[0].text
            description = response.html.find('.infobox-description')[0].text
            big_description = response.html.find('.body .mb-6')[0].text
            links = response.html.find('.links a')[0].attrs['href']
            try:
                rating = response.html.find('.h6')[0].text
                rating_image = response.html.find('.rating-source')[0].attrs['src']
                rating_text = response.html.find(
                    '.r .flex-hcenter .text-sm ')[0].text

            except:
                pass

    # wikipedia image scraping

            try:
                # image
                img_url = links

                try:
                    session = HTMLSession()
                    response = session.get(img_url)

                except requests.exceptions.RequestException as e:
                    print(e)

                image_url = response.html.find(
                    '.infobox-image img')[0].attrs['src']

            except:
                pass

            # title
            try:

                # center the image
                st.sidebar.markdown(
                    f'<img src="{image_url}" alt="0" style="width: 100%;border-radius: 5px;">', unsafe_allow_html=True)
                # st.sidebar.image("https:"+image_url, width=150,)
            except:
                pass
            st.sidebar.markdown(
                f"<h1 style = 'margin:0px 5rem;'>{title1}</h1>", unsafe_allow_html=True)
            st.sidebar.markdown(
                f"<p style='margin:15px 3rem;font-size:0.9rem; font-family: -apple-system,system-ui,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',sans-serif;'>{description}</p>", unsafe_allow_html=True)
            st.sidebar.write(big_description+f"[Wikipedia]({links})")
            try:
                st.sidebar.markdown(
                    f"<h1 style = 'margin:0px 5rem;'>Ratings</h1><br>", unsafe_allow_html=True)
                st.sidebar.markdown(
                    f"<img src='{rating_image}' style='border-radius:20px;'>   &nbsp;  {rating_text}", unsafe_allow_html=True)
            except:
                pass
        except:
            pass
    elif choice == "Images":
        st.write('Images tab comming sooon')
    elif choice == "Videos":
        st.write('Videos tab comming sooon')
    elif choice == "News":
        st.write('News tab Comming soon')
    elif choice == "Info":
        st.write('Info tab Comming soon')