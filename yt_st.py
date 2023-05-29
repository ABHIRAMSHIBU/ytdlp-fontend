import streamlit as st
import os

url = st.text_input('YouTube Video Link')
directory = st.text_input("Download Directory","/data/Music Videos")

if st.button('Download'):
    with st.spinner('Wait for it...'):
        os.system(f'yt-dlp -f "bv*+ba" "{url}" -o "{directory}/%(title)s.%(ext)s"')
    st.balloons()
    st.success('Done!')