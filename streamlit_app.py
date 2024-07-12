import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Samuel Koffler, Undergrad')

st.info('Student at Michigan State University, focused in Computer Science with an interest in Chemistry and Pharmacology')

icon_size = 20

st_button('youtube', 'https://www.youtube.com/@CereaLover123', 'My YouTube channel', icon_size)
st_button('youtube', 'https://youtube.com/playlist?list=PL6jgA9JKEkMHi8SsHUa1-qOeUhADCBwwW&si=IlNnJLWHAp2PYCd2', 'My reference YouTube videos playlist', icon_size)
#st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://x.com/SamuelKoffler', 'Follow me on X', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/samuel-koffler-3216b0290/', 'Follow me on LinkedIn', icon_size)
#st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
#st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
