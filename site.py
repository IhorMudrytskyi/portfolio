import streamlit as st

tab = st.tabs(["Головна", "5 семестр", "6 семестр"])

if "main" not in st.session_state:
    st.session_state.main = "home"

if "cyber" not in st.session_state:
    st.session_state.cyber = "home"

if "htb" not in st.session_state:
    st.session_state.htb = "home"

if "crypto" not in st.session_state:
    st.session_state.crypto = "home"

def render_grid(images, names, links=None, cols_count=4):
    for row in range(0, len(images), cols_count):
        cols = st.columns(cols_count)

        for col, i in zip(cols, range(row, min(row + cols_count, len(images)))):
            with col:
                with st.container(border=True):
                    st.image(images[i], use_container_width=True)

                    st.markdown(
                        f"""
                        <div style="
                            height:70px;
                            display:flex;
                            align-items:center;
                            justify-content:center;
                            text-align:center;
                            font-weight:600;
                            font-size:14px;
                        ">
                            {names[i]}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if links:
                        st.link_button("Відкрити", links[i], use_container_width=True)

# __________________________Головна__________________________
with tab[0]:
    st.markdown("<h1 style='text-align:center'>Вітаю на сайті портфоліо курсанта групи ННІ4-23-303Кб Мудрицького Ігоря Володимировича</h1>", unsafe_allow_html=True)

# __________________________5 семестр__________________________
with tab[1]:

    disc1, disc2 = st.columns(2)

    with disc1:
        if st.button("Кібербезпека", use_container_width=True, key="cyber 5"):
            st.session_state.main = "cyber"

    with disc2:
        st.link_button("TryHackMe", "https://tryhackme.com/p/migor2k05", use_container_width=True, key="thm 5")

# __________________________Кібербезпека__________________________
    if st.session_state.main == "cyber":
        
        cisco, htb = st.columns(2)

        with cisco:
            if st.button("Cisco", use_container_width=True, key="cisco 5"):
                st.session_state.cyber = "cisco"

        with htb:
            if st.button("HackTheBox", use_container_width=True, key="htb 5"):
                st.session_state.cyber = "htb"

# __________________________Cisco__________________________
        if st.session_state.cyber == "cisco":
            from config import name_cisco_5sem, image_cisco_5sem, link_cisco_5sem
            render_grid(image_cisco_5sem, name_cisco_5sem, link_cisco_5sem, 4)
            
            with st.container(border=True):
                st.markdown("<h4 style='text-align:center'>Початок роботи з Cisco Packet Tracer</h4>", unsafe_allow_html=True)
                st.image("https://raw.githubusercontent.com/IhorMudrytskyi/portfolio/main/image/5sem/cyber/cisco/Початок роботи з Cisco Packet Tracer.png", use_container_width=True)

            with st.container(border=True):
                st.markdown("<h4 style='text-align:center'>Exploring Networking with Cisco Packet Tracer</h4>", unsafe_allow_html=True)
                st.image("https://raw.githubusercontent.com/IhorMudrytskyi/portfolio/main/image/5sem/cyber/cisco/Exploring Networking with Cisco Packet Tracer.png", use_container_width=True)

            with st.container(border=True):
                st.markdown("<h4 style='text-align:center'>Exploring Internet of Things with Cisco Packet Tracer</h4>", unsafe_allow_html=True)
                st.image("https://raw.githubusercontent.com/IhorMudrytskyi/portfolio/main/image/5sem/cyber/cisco/Exploring Internet of Things with Cisco Packet Tracer.png", use_container_width=True)
            

# __________________________HackTheBox__________________________
        if st.session_state.cyber == "htb":

            htb = st.columns(3)

            with htb[0]:
                if st.button("Machines", use_container_width=True, key="mach 5"):
                    st.session_state.htb = "mach"

            with htb[1]:
                if st.button("Challanges", use_container_width=True, key="chal 5"):
                    st.session_state.htb = "chal"

            with htb[2]:
                if st.button("Modules", use_container_width=True, key="mod 5"):
                    st.session_state.htb = "mod"

# __________________________HackTheBox Machines__________________________
            if st.session_state.htb == "mach":
                from config import image_htb_mach_5sem, name_htb_mach_5sem, link_htb_mach_5sem
                render_grid(image_htb_mach_5sem, name_htb_mach_5sem, link_htb_mach_5sem, 4)

# __________________________HackTheBox Challanges__________________________
            if st.session_state.htb == "chal":
                from config import image_htb_chal_5sem, name_htb_chal_5sem, link_htb_chal_5sem
                render_grid(image_htb_chal_5sem, name_htb_chal_5sem, link_htb_chal_5sem, 4)

# __________________________HackTheBox Modules__________________________
            if st.session_state.htb == "mod":
                from config import image_htb_mod_5sem, name_htb_mod_5sem, link_htb_mod_5sem
                render_grid(image_htb_mod_5sem, name_htb_mod_5sem, link_htb_mod_5sem, 4)

# __________________________6 семестр__________________________
with tab[2]:
    
    disc = st.columns(2)

    with disc[0]:
        if st.button("Кібербезпека", use_container_width=True, key = "cyber 6"):
            st.session_state.main = "cyber"

    with disc[1]:
        if st.button("ПКтаС", use_container_width=True, key = "crypto 6"):
            st.session_state.main = "crypto"
# __________________________Кібербезпека__________________________
    if st.session_state.main == "cyber":
        
        col = st.columns(3)

        with col[0]:
            if st.button("Modules", use_container_width=True, key="mod 6"):
                st.session_state.htb = "mod"

        with col[1]:
            if st.button("Machines", use_container_width=True, key="mach 6"):
                st.session_state.htb = "mach"

        with col[2]:
            if st.button("Challanges", use_container_width=True, key="chal 6"):
                st.session_state.htb = "chal"
# __________________________HackTheBox Modules 6 семестр__________________________
        if st.session_state.htb == "mod":
            from config import image_htb_mod_6sem, name_htb_mod_6sem, link_htb_mod_6sem
            render_grid(image_htb_mod_6sem, name_htb_mod_6sem, link_htb_mod_6sem, 4)

# __________________________HackTheBox Machines 6 семестр__________________________
        if st.session_state.htb == "mach":
            from config import image_htb_mach_6sem, name_htb_mach_6sem, link_htb_mach_6sem
            render_grid(image_htb_mach_6sem, name_htb_mach_6sem, link_htb_mach_6sem, 4)

# __________________________HackTheBox Challanges 6 семестр__________________________
        if st.session_state.htb == "chal":
            from config import image_htb_chal_6sem, name_htb_chal_6sem, link_htb_chal_6sem
            render_grid(image_htb_chal_6sem, name_htb_chal_6sem, link_htb_chal_6sem, 4)

# __________________________ПКтаС 6 семестр__________________________
    if st.session_state.main == "crypto":

        cols = st.columns(3)

        with cols[0]:
            st.link_button("TryHackMe", "https://tryhackme.com/p/migor2k05", use_container_width=True, key="thm 6")

        with cols[1]:
            st.link_button("CryptoHack", "https://cryptohack.org/user/MudritskiyIgor/", use_container_width=True, key="cryptohack 6")

        with cols[2]:
            if st.button("PicoCTF", use_container_width=True, key="picoctf 6"):
                st.session_state.crypto = "pico"

# __________________________PicoCTF 6 семестр__________________________
        if st.session_state.crypto == "pico":
            from config import image_pico_6sem, name_pico_6sem

            for i in range(0, len(image_pico_6sem)):
                with st.container(border=True):
                    st.markdown(f"<h4 style='text-align:center'>{name_pico_6sem[i]}</h4>", unsafe_allow_html=True)
                    st.image(image_pico_6sem[i], use_container_width=True)
