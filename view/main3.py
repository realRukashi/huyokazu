import streamlit as st

col1, col2= st.columns([1, 6])

with col1:
    st.write("")
with col2:
    original_title = '<p style="font-family:Courier; color:Pink; font-size: 20px;">Below are my online judges (OJ) accounts:</p>'
    st.markdown(original_title, unsafe_allow_html=True)
st.write('')

nbk, lqd, cla, vnoj, cf, lc = st.columns([1, 1, 1, 1, 1, 1])

with nbk:
    st.link_button('nbkoj', 'https://nbk.homes/user')  

with lqd:
    st.link_button('lqdoj', 'https://lqdoj.edu.vn/user/OKAZU')

with cla:
    st.link_button('claoj', 'https://claoj.edu.vn/user/KAZU')

with vnoj:
    st.link_button('vnoi', 'https://oj.vnoi.info/user/OSKAZU')

with cf:
    st.link_button('codeforces', 'https://codeforces.com/profile/OKAZU')

with lc:
    st.link_button('leetcode', 'https://leetcode.com/u/OKAZU/')