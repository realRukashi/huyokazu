import streamlit as st

from streamlit.components.v1 import html



def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

st.button('My instagram', on_click = open_page, args=('https://www.instagram.com/ng_thenkhyy/',))