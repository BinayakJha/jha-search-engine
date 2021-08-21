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
hide_streamlit_style = """
            <style>
            
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stConnectionStatus{visibility: hidden;}
            .viewerBadge_container__1QSob {visibility: hidden !important;}
             body { overflow-x:hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Jha Browser - Made By Binayak jha")
st.write("Fast, Secure, Full privacy control to the user, Non tracking Browser")
def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)
col1,col2 = st.columns([6,2])
with col1:
    query = st.text_input("Search the world")
with col2:
    button = """
<style>
    .css-1ubkpyc{margin:21px -1px;padding: 12px 28px 12px 28px;}
    .stButton{margin:-8px;}
</style>
"""
    st.markdown(button, unsafe_allow_html=True)
    st.button("Search")

 


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


import pandas
# export results to csv file

# a = st.button("")

# if a:
#     # hide the a button
#     col1, col2, col3,col4,col5,col6,col7= st.columns(7)
#     with col1:
#         all = st.markdown("All")
#     with col2:
#         images = st.markdown("Images")
#     with col3:
#         videos = st.markdown("News")
#     with col4:
#         maps = st.markdown("Videos")
#     with col5:
#         st.write("")
#     with col6:
#         st.write("")
#     with col7:
#         st.markdown("Info")



#     try:
#         try:
#             st.header('Featured answer :')
#             col1,col2 = st.columns([0.5,6]) 
#             with col2:            
#                 featured_answer = people_also_ask.get_simple_answer(query)
#                 st.write(featured_answer)
#             st.markdown('---')
#             st.write("\n")
#         except:
#             pass
#         df = pandas.DataFrame(results)
#         title = df['title']
#         link = df['link']
#         text = df['text']

#         for i in range(len(title)):
#             st.header(title[i])
#             st.markdown(link[i])
#             st.text(text[i])
#             st.markdown("---")

#             st.write("\n")
#     except:
#         st.error("Sorry, No results found :( Please try another query")

if query:
    col1, col2, col3,col4,col5,col6,col7= st.columns(7)
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
                st.write(featured_answer)
            st.markdown('---')
            st.write("\n")
        except:
            st.write('No Featured answer found!')
            pass
        df = pandas.DataFrame(results)
        title = df['title']
        link = df['link']
        text = df['text']
        # write title then link and then text
        # add link inside the title
        for i in range(len(title)):
            # st.link(title[i], link[i])
            st.header(f"[{title[i]}]({link[i]})")
            st.text(text[i])
            st.markdown("---")
            st.write("\n")
    except:
        st.error("Sorry, No results found :( Please try another query")

