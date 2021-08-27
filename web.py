from re import S
import pandas
from logging import PlaceHolder
from numpy.lib.function_base import place
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import streamlit as st
import people_also_ask

st.set_page_config(page_title="Jha Browser")
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)
# css
st.markdown("""
<style>@import url('@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

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
             body { overflow-x:hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




placeholder = st.markdown("<h1 style='text-align: center;margin-top:-60px;font-size:7rem !important;' id = 'heading'>Jha Browser</h1><p style='text-align:center;font-size:1.3em;'>Fast, Secure, Full privacy control to the user, Non tracking Browser</p><p  style='text-align:center;margin-bottom:-2px;font-size:1.1em;'>Search Here!!</p>", unsafe_allow_html=True)


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


col1, col2 = st.columns([6, 2])
with col1:
    query = st.text_input("")
with col2:
    button = """
<style>
            .st-df{padding:10px;}
            .st-cn{margin:90px 40%;padding:20px;border-radius:5px;background-color:#ee7274 !important;font-size:1.2em;font-family: 'Poppins', sans-serif;}
            .stCheckbox span{visibility:hidden;}
            .css-hi6a2p{background-color:white !important}
            .css-1ubkpyc{margin:21px -1px;padding: 18px 35px 14px 35px;}
            .css-lybem{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;}
            .css-qbe2hs{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;}
            .css-n19jqu:hover{background:#ee7274 !important; color:white !important}
            .css-n19jqu{margin:21px 7px;padding:19px 43px !important;border: 1px solid red;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;background:#ee7274 !important;color:black;}
            .st-br{border:1px solid grey;border-bottom-color:grey;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;padding:8px !important}
            .st-bc{padding:9px !important;background:transparent}
            .st-go{background: transparent;}
            .st-bs{background:transparent}
            .st-bx{background:transparent}
            .st-bu{background:transparent}
            .st-cz{background:transparent}
            .st-cl{padding: 9px !important;}
            .st-bg{padding: 9px !important;}
            .st-bv{background:transparent}
            #heading{font-size:7rem !important;font-family: 'Righteous', cursive !important;}
            .stButton{margin:-8px;}
            .css-1ko0gb7{margin:0px 0px 1rem;}
            .css-hi6a2p{max-width:1000px !important ;background:white;padding: 2.5rem 1.5rem 6rem !important;}
            h1,h2,h3,h4,h5,h6,p,b,i{color:black!important;font-family: 'Poppins', sans-serif;}
            .css-ip91b3{width:22rem;}
            .css-pday0i{width:24rem;background:white;}
            a{color:#1a0dab!important;text-decoration:none;}
            .css-hi6a2p {flex: 1 1 0%;width: 100%;padding: 2.5rem 1rem 6rem;max-width: 730px;margin: 53px;border-radius: 5px;}
            hr {margin: 1em 3px;padding: 0px;color: inherit;background-color: transparent;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 21px solid #f0f5f7!important;margin: 12px -32px;border-radius: 5px;}
</style>
"""
    st.markdown(button, unsafe_allow_html=True)
    st.button("Search")
#  on click change to dark theme
# st.markdown("<p style='margin:-396px 791px 0px -15px;z-index:0;color:black;'>hello</p>", unsafe_allow_html=True)
changer = st.checkbox("Change Theme")
if changer == True:
    st.markdown("""
            <style>
            .st-df{padding:10px;}
            .st-cn{margin:-396px 791px 0px -15px;padding:20px;border-radius:5px;background-color:#ee7274 !important;font-size:1.2em;font-family: 'Poppins', sans-serif;}
            .css-1djdyxw{color:white !important}
            .css-hi6a2p{background-color:#242731 !important}
            .css-1ubkpyc{margin:21px -1px;padding: 18px 35px 14px 35px;}
            .css-lybem{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;}
            .css-qbe2hs{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;color:black;}
            .css-n19jqu{margin:22px 4px;padding:19px 68px !important;border: 1px solid red;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;background:#ee7274 !important;color:white;}
            .css-n19jqu:hover{background:#ee7274 !important; color:white !important}
            .st-br{border:1px solid grey;border-bottom-color:grey;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;padding:9px !important}
            .st-bc{padding:9px !important;background:transparent}
            .st-go{background: rgb(203, 199, 199);}
            .st-bs{background:rgb(203, 199, 199);}
            .st-bx{background:rgb(203, 199, 199);}
            .st-bu{background:rgb(203, 199, 199);}
            .st-cz{background:rgb(203, 199, 199);}
            .st-cl{padding: 9px !important;}
            .css-1h8rjc8{background:#1E2028;}
            .stButton{margin:-8px;}
            .css-1ko0gb7{margin:0px 0px 1rem;}
            .css-hi6a2p{max-width:1000px !important ;background:white;padding: 2.5rem 1.5rem 6rem !important;}
            .css-ip91b3{width:22rem;}
            .css-pday0i{width:24rem;background:#242731!important;}
            .css-2lw3zc{color:white !important;}
            #heading{font-size:6.5rem !important;}
            .css-12jmujn{color:white !important}
            h1,h2,h3,h4,h5,h6,p,b,i{color:white !important;font-family: 'Poppins', arial, sans-serif;}
            .css-hi6a2p {flex: 1 1 0%;width: 100%;padding: 2.5rem 1rem 6rem;max-width: 730px;margin: 53px;border-radius: 5px;}
            hr {margin: 1em 3px;padding: 0px;color: inherit;background-color: #1E2028 !important;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 21px solid #1F2128!important;margin: 12px -32px;border-radius: 5px;}
            .css-158txa1{color:white !important}
            html{scrollbar-color: revert;}
            a{color:#6da7ff!important;text-decoration:none;}
            /* scroll bar */
            ::-webkit-scrollbar {
            width: 8px;
            }
            /* Track */
            ::-webkit-scrollbar-track {
            background: rgb(44, 43, 43);
            }
            </style>""", unsafe_allow_html=True)
# while changing the theme add some transition
elif changer == False:
    st.markdown("""<style>
        .st-df{padding:10px;}
        .st-cn{margin:-410px 791px 0px -15px;padding:20px;border-radius:5px;background-color:#ee7274 !important;font-size:1.2em;font-family: 'Poppins', sans-serif;}
            .css-hi6a2p{background-color:white !important}
            .css-1ubkpyc{margin:21px -1px;padding: 18px 35px 14px 35px;}
            .css-lybem{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;}
            .css-qbe2hs{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;}
            .css-n19jqu:hover{background:#ee7274 !important; color:white !important}
            .css-n19jqu{margin:22px 4px;padding:19px 68px !important;border: 1px solid red;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;background:#ee7274 !important;color:black;}
            .st-br{border:1px solid grey;border-bottom-color:grey;box-shadow: rgb(0 0 0 / 16%) 0px 4px 16px;padding:8px !important}
            .st-bc{padding:9px !important;background:transparent}
            .st-go{background: transparent;}
            .st-bs{background:transparent}
            .st-bx{background:transparent}
            .st-bu{background:transparent}
            .st-cz{background:transparent}
            .st-cl{padding: 9px !important;}
            #heading{font-size:7rem !important;}
            .stButton{margin:-8px;}
            .css-1ko0gb7{margin:0px 0px 1rem;}
            .css-hi6a2p{max-width:1000px !important ;background:white;padding: 2.5rem 1.5rem 6rem !important;}
            h1,h2,h3,h4,h5,h6,p,b,i{color:black!important;font-family: 'Poppins', sans-serif;}
            .css-ip91b3{width:22rem;}
            .css-pday0i{width:24rem;background:white;}
            a{color:#1a0dab!important;text-decoration:none;}
            .css-hi6a2p {flex: 1 1 0%;width: 100%;padding: 2.5rem 1rem 6rem;max-width: 730px;margin: 53px;border-radius: 5px;}
            hr {margin: 1em 3px;padding: 0px;color: inherit;background-color: transparent;border-top: none;border-right: none;border-left: none;border-image: initial;border-bottom: 21px solid #f0f5f7!important;margin: 12px -32px;border-radius: 5px;}
            </style>""", unsafe_allow_html=True)

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


def google_search(query):
    response = get_results(query)
    return parse_results(response)


results = google_search(query)
# favicons

# export results to csv file


# youtube
# if youtube.com in link then cut the link and take out watch?v =


# end youtube
if query:
    placeholder.empty()
    col1, col2, col3, col4, col5, col6, col7 = st.columns(
        (0.5, 1, 1, 1, 1, 1, 1))
    with col1:
        all = st.markdown("All")
    with col2:
        images = st.markdown("Images")
    with col3:
        videos = st.markdown("News")
    with col4:
        maps = st.markdown("Videos")
    with col5:
        st.write("")
    with col6:
        st.write("")
    with col7:
        st.markdown("Info")
    try:
        try:
            st.header('Featured answer :')
            col1, col2 = st.columns([0.5, 6])
            with col2:
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
                        st.markdown('<h3>Definition</h3>',
                                    unsafe_allow_html=True)
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
                    favicon_url = "https://www.google.com/s2/favicons?sz=64&domain_url=" + \
                        link[i]
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