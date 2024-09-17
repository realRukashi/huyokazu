import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

page_bg_img = '''
<style>
body {
background-image: url("https://z-p4-instagram.fsgn7-2.fna.fbcdn.net/v/t39.30808-6/453923086_18038822134974117_3031235235791238446_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi44OTB4MTExMy5zZHIuZjMwODA4LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=z-p4-instagram.fsgn7-2.fna.fbcdn.net&_nc_cat=109&_nc_ohc=8hKBuV7U1qoQ7kNvgH_J37J&_nc_gid=f675bd80169e443187867337012af1bf&edm=AP4sbd4AAAAA&ccb=7-5&ig_cache_key=MzQyNjE5NzM1ODM2NTE5ODM0MA%3D%3D.3-ccb7-5&oh=00_AYBtO6oiltE_2KL5ZiQ9dE5tDsycWMEU0mAIEeZDJ8kgcQ&oe=66EF4A0E&_nc_sid=7a9f4b");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
"""
<style>
.big-font 
{
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Xin chào, mình là Thanh Huy, sinh viên chương trình Cử nhân Tài năng khoa Công nghệ Thông tin khóa 2024, Đại học Khoa học Tự nhiên - ĐHQG TP.HCM, và cũng là cựu học sinh khóa 20 của trường THPT chuyên Nguyễn Bỉnh Khiêm, Quảng Nam.</p>', unsafe_allow_html=True)

st.write(''); st.write(''); st.write('')

nt1, nt2 = st.columns([1, 2])

with nt1:
    st.write('')
with nt2:
    st.write("Dưới đây các nền tải mạng xã hội của mình:")

ig, fb, tk, th, lk, wc = st.columns([1, 1, 1, 1, 1, 1])

with ig:
    st.link_button("Instagram", "https://www.instagram.com/ng_thenkhyy/")

with fb:
    st.link_button('Facebook', 'https://www.facebook.com/profile.php?id=100046108965087')

with tk:
    st.link_button('Tiktok', 'https://www.tiktok.com/@kazu_19_?fbclid=IwY2xjawFWaJVleHRuA2FlbQIxMAABHUDfH3Z49I8KP5IhWU3rvfTkjkcVRlNk2Le3wlYxzRZHOxYyJhOjSe-tVg_aem__iXHWt8cbU-FQpZdSolPHg')

with th:
    st.link_button('Threads', 'https://www.threads.net/@ng_thenkhyy?xmt=AQGz_3ApPVsa-wqFHP5_tX4c08Dk-E6hL2FvxCqgo_q_qUw')

with lk:
    st.link_button('Locket', 'https://locket.camera/invites/9PXHMvPWsONwU2bAV2knXC0Opga2c25c77e1d83bfc3a?type=Link&variant=1002&social_title=Add+me+on+Locket+%F0%9F%92%9B&social_desc=I+want+to+add+you+to+my+Home+Screen+with+Locket.+Tap+the+link+to+accept.&social_img=https://firebasestorage.googleapis.com:443/v0/b/locket-img/o/users%252F9PXHMvPWsONwU2bAV2knXC0Opga2%252Fpublic%252Finvite_link_previews%252F1725950567.63421.webp?alt%3Dmedia%26token%3D504879cd-4149-452f-b738-b6f9b61b7553&lang=en')

with wc:
    st.link_button('Wechat', 'https://scontent.xx.fbcdn.net/v/t1.15752-9/459074749_835860308751555_8864477067973937065_n.jpg?stp=dst-jpg_s206x206&_nc_cat=100&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeELgTH1dodMdI46ZrsOEXJM8kdRVyN987PyR1FXI33zs58v4BNsMn7xynG1dYlHW_pXKSfYwwORdUMuAbYE1jfR&_nc_ohc=258uJICIcfMQ7kNvgHBDfCO&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&_nc_gid=A_EN2G8etr2ErX1VbL9kTOQ&oh=03_Q7cD1QEUDdqz9nes_8ndKHycB8yOqWCctBGP0FsRRsLJDfagQg&oe=6710FEAD')

st.write(''); st.write(''); st.write('')
