import streamlit as st
import time
import numpy as np
import pandas as pd

from streamlit.components.v1 import html

st.header("Hello everyone welcome to my website")
st.subheader("These are my personal pages:")

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)



ig = st.button('My instagram', on_click = open_page, args = ('https://tinyurl.com/4znb2n79',))
if ig:
    st.experimental_rerun()
