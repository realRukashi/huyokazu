import streamlit as st
import time
import numpy as np
import pandas as pd

#st.set_page_config(layout="wide")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://cdn.pixabay.com/photo/2016/11/18/22/58/stars-1837306_640.jpg");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{

background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown(
"""
<style>
.big-font 
{
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Xin chào, mình là Thanh Huy, cực học sinh khóa 20 trường THPT chuyên Nguyễn Bỉnh Khiêm, Quảng Nam và hiện tại mình là sinh viên lớp CNTN khoa CNTT của HCMUS.</p>', unsafe_allow_html=True)

st.write(''); st.write(''); st.write('')

#nt1, nt2 = st.columns([1, 2])

#with nt1:
    #st.write('')
#with nt2:

st.write("Dưới đây các nền tải mạng xã hội của mình:")
st.write('')

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

#nt3, nt4 = st.columns([1, 1.7])

#with nt3:
    #st.write('')
#with nt4:
st.write('Dưới đây là các OJ của mình:')
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
