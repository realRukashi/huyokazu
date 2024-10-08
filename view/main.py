import streamlit as st 

st.markdown(
"""
<style>
.big-font 
{
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")

with col1:
    st.image("./img/main1.jpg", width = 350);
with col2:
    #st.markdown('<p class="big-font">Nguyễn Thanh Huy</p>', unsafe_allow_html=True)
    #st.title("Nguyễn Thanh Huy", anchor = False)
    original_title = '<p style="font-family:Courier; color:Pink; font-size: 30px;">Nguyễn Thanh Huy</p>'
    original_title2 = '<p style="font-family:Courier; color:Pink; font-size: 15px;">study at Bachelor Talent of Computer Science - HCMUS</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.markdown(original_title2, unsafe_allow_html=True)
