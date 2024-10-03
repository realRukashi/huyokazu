import streamlit as st

col1, col2= st.columns([1, 5])

with col1:
    st.write("")
with col2:
    original_title = '<p style="font-family:Courier; color:Pink; font-size: 20px;">Below are my social media platforms:</p>'
    st.markdown(original_title, unsafe_allow_html=True)
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
