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
# css 
st.markdown("""<style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500&display=swap');
body {
    font-family: 'Poppins', sans-serif;
}
.css-1u0jg5e {visibility: hidden;}
</style>""", unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            
            # #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stConnectionStatus{visibility: hidden;}
            .viewerBadge_container__1QSob {visibility: hidden !important;}

             body { overflow-x:hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown('''<li role="option" aria-selected="false" aria-disabled="false" class="css-h60zsd e1pxm3bq3" ><span class="css-1qkncxf e1pxm3bq4" style = "visibisity:hidden">About Streamlit sharing</span></li>''', unsafe_allow_html=True)
placeholder = st.markdown("<h1 style='text-align: center;margin-top:-60px;'>Jha Browser</h1><p style='text-align:center;'>Fast, Secure, Full privacy control to the user, Non tracking Browser</p><p  style='text-align:center;margin-bottom:-2px;'>Search Here!!</p>", unsafe_allow_html=True)
def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
col1,col2 = st.columns([6,2])
with col1:
    query = st.text_input("")
with col2:
    button = """
<style>
    .css-1ubkpyc{margin:21px -1px;padding: 18px 35px 14px 35px;}
    .css-lybem{margin:21px -1px;padding: 18px 35px 14px 35px;border: 1px solid red;}
    .st-br{border:1px solid grey;border-bottom-color:grey}
    .st-bc{padding:8px !important;}
    .stButton{margin:-8px;}
    hr{background-color: #d8c2c2e0;}

</style>
"""
    st.markdown(button, unsafe_allow_html=True)
    st.button("Search")
#  on click change to dark theme

 


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
    css_identifier_featured=".di3YZe"
    results = response.html.find(css_identifier_result)
    

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

import pandas
# export results to csv file



# youtube 
# if youtube.com in link then cut the link and take out watch?v = 


# end youtube
if query:
    placeholder.empty()
    col1, col2, col3,col4,col5,col6,col7= st.columns((0.5,1,1,1,1,1,1))
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
            col1,col2 = st.columns([0.5,6]) 
            with col2:            
                featured_answer = people_also_ask.get_simple_answer(query)
                if "youtube.com/watch?v" in featured_answer:
                    url = featured_answer
                    session = HTMLSession()
                    response = session.get(url)
                    title = response.html.find('title', first=True).text
                    featured_answer1 = featured_answer.split("youtube.com/watch?v=")[1]
                    yt_url1 = f"https://i.ytimg.com/vi/{featured_answer1}/0.jpg"
                    # st.markdown(f"<a href='{featured_answer}' target='_blank'><img src ='{yt_url1}' style='width: 80%;border-radius:5px;'></a>",unsafe_allow_html=True)
                    # open embed video direct in youtube
                    # st.markdown(f"<a href='https://www.youtube.com/embed/{featured_answer1}' target='_blank'><img src ='{yt_url1}' style='width: 80%;border-radius:5px;'></a>",unsafe_allow_html=True)
                    st.markdown(f'<a href="{yt_url1}" target="_blank"><iframe height="400" src="https://www.youtube.com/embed/{featured_answer1}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style = "width:90%;border-radius:5px;"></iframe></a>',unsafe_allow_html=True)
                    st.header(f"[{title}]({featured_answer})")
                else:
                    st.markdown(featured_answer,unsafe_allow_html=True)
            st.markdown('---')
            st.write("\n")
        except:
            st.write('No Featured answer found!')
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
           
            col1,col2 = st.columns([0.5,6])
            # add style 
            style =  """
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
                    favicon_url = "https://www.google.com/s2/favicons?sz=64&domain_url="+link[i]
                    st.image(favicon_url,width=32)
                except:
                    pass

            with col2:
                
                st.header(f"[{title[i]}]({link[i]})")
            col1,col2 = st.columns([0.5,6])
                # If youtube in favicon url then show image
                # if image is not loaded then pass
            if "youtube.com" in favicon_url:
                        col1,col2 = st.columns([6,2])
                        with col1:
                             st.markdown(f'{text[i]}')
                        with col2:

                            if "/watch?v" in link[i]:
                                link3 = link[i][32:]
                                yt_url = f"https://i.ytimg.com/vi/{link3}/0.jpg"
                                st.markdown(f"<img src ='{yt_url}' style='width: 100%;border-radius:5px;'>",unsafe_allow_html=True)
                    # if not then leave the space
            else:
                st.markdown(f'{text[i]}')
            st.markdown("---")
            st.write("\n")
    except:
        st.error("Sorry, No results found :( Please try another query")
    try:
        url = "https://search.brave.com/search?q="+query
        st.markdown("<style> html{font-family: -apple-system,system-ui,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',sans-serif;}</style>", unsafe_allow_html=True)
        try:
            session = HTMLSession()
            response = session.get(url)
            
        except requests.exceptions.RequestException as e:
            print(e)

        title1 =  response.html.find('.infobox-title')[0].text
        description = response.html.find('.infobox-description')[0].text
        big_description = response.html.find('.body .mb-6')[0].text
        links = response.html.find('.links a')[0].attrs['href']
        try:
            rating = response.html.find('.h6')[0].text
            rating_image = response.html.find('.rating-source')[0].attrs['src']
            rating_text = response.html.find('.r .flex-hcenter .text-sm ')[0].text

        except:
            pass
        
# wikipedia image scraping


        try:
            # image
            img_url = f"https://en.wikipedia.org/wiki/{title1}"

            try:
                session = HTMLSession()
                response = session.get(img_url)
                
            except requests.exceptions.RequestException as e:
                print(e)

            image_url = response.html.find('.infobox-image img')[0].attrs['src']

        except:
            pass



        # title
        try:
            
            # center the image
            st.sidebar.markdown(f'<img src="{image_url}" alt="0" style="width: 100%;border-radius: 5px;">', unsafe_allow_html=True)
            # st.sidebar.image("https:"+image_url, width=150,)
        except:
            pass
        st.sidebar.markdown(f"<h1 style = 'margin:0px 5rem;'>{title1}</h1>", unsafe_allow_html=True)
        st.sidebar.markdown(f"<p style='margin:15px 3rem;font-size:0.9rem; font-family: -apple-system,system-ui,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',sans-serif;'>{description}</p>",unsafe_allow_html=True)
        st.sidebar.write(big_description+f"[Wikipedia]({links})")
        try:
            st.sidebar.markdown(f"<h1 style = 'margin:0px 5rem;'>{rating}</h1><br>", unsafe_allow_html=True)
            st.sidebar.markdown(f"<img src='{rating_image}' style='border-radius:20px;'>   &nbsp;  {rating_text}",unsafe_allow_html=True)
        except:
            pass
    except:
        pass

