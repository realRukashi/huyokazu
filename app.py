import streamlit as st 

about_page = st.Page(
    page = "view/main.py",
    title = "About me",
    icon = ":material/account_circle:",
    default = True,
)

about_page2 = st.Page(
    page = "view/main2.py",
    title = "hi",
    icon = ":material/smart_toy:",
)

pg = st.navigation(pages = [about_page, about_page2])

pg.run()