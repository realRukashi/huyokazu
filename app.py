import streamlit as st 

about_page = st.Page(
    page = "view/main.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,
)

about_page2 = st.Page(
    page = "view/main2.py",
    title = "Social Network",
    icon = ":material/sensors:",
)

about_page3 = st.Page(
    page = "view/main3.py",
    title = "Online Judge",
    icon = ":material/code:",
)

pg = st.navigation([about_page, about_page2, about_page3])

st.sidebar.text("Made with 💓 by thenkhy")

pg.run()