import streamlit as st
import os
import re

# =======================
# CONFIGURASI DASAR
# =======================
st.set_page_config(
    page_title="Tiga Putri",
    page_icon=":handbag:",
    layout="wide"
)

# =======================
# WELCOME NOTIFICATION
# =======================
if "welcome_shown" not in st.session_state:
    st.session_state.welcome_shown = False

if not st.session_state.welcome_shown:
    st.toast("✨ Welcome to Tiga Putri — Timeless Indonesian Craftsmanship ✨", icon="👜")
    st.session_state.welcome_shown = True


# =======================
# INIT CART
# =======================
if "cart" not in st.session_state:
    st.session_state.cart = []
    
# =======================
# CSS CUSTOM
# =======================
st.markdown("""
    <style>
    /* Font Import */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=Poppins:wght@300;400;600&display=swap');

    /* Background & Font */
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background-color: #FAF9F6;
        color: #2C2C2C;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #fff;
        padding: 20px;
        border-right: 1px solid #eee;
    }
    section[data-testid="stSidebar"] h2 {
        font-family: 'Playfair Display', serif;
        color: #7B1E3B;
    }

    /* Buttons */
    .stButton button {
        background-color: #7B1E3B;
        color: white;
        border-radius: 12px;
        padding: 8px 16px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #a83250;
        transform: scale(1.05);
    }

    /* Product Card */
    .product-card {
        background: #fff;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        transition: 0.3s;
    }
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    }
    .product-title {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        margin: 10px 0;
        color: #333;
    }
    .product-price {
        font-size: 16px;
        color: #7B1E3B;
        font-weight: bold;
    }

    /* Footer */
    .footer {
        margin-top: 50px;
        padding: 30px;
        text-align: center;
        font-size: 14px;
        color: #666;
        border-top: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# =======================
# LOGO & BRAND
# =======================
from PIL import Image
logo = Image.open("data/assets/logo.png")  # pastikan path logo benar

st.sidebar.image(logo, use_container_width=True)
st.sidebar.markdown("<h2 style='text-align:center;'>Tiga Putri</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align:center; color:#666;'>Elegant Export & Import Fashion for Women</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# =======================
# NAVIGASI
# =======================
page = st.sidebar.radio("Navigate", ["🏠 Home", "🌍 About", "📸 Lookbook", "🛍️ Shop", "🛒 Cart", "👤 Account"])


# =======================
# SIDEBAR FILTER
# =======================
st.sidebar.markdown("### 🔎 Search Product")
st.sidebar.text_input("Search by Name/Code")

st.sidebar.markdown("### 📂 Category")
kategori = st.sidebar.selectbox("Pilih Kategori", [
    "Semua",
    "Tas", "Tote Bags", "Handbags", "Backpack", "Clutch",
    "Aksesoris", "Dompet", "Perhiasan", "Scarf", "Ikat Pinggang",
    "Fashion Lainnya", "Sepatu", "Sandal", "Outerwear"
])

warna = st.sidebar.multiselect("Warna", ["Hitam", "Putih", "Merah", "Biru", "Hijau"])
material = st.sidebar.multiselect("Material", ["Pandan", "Kulit", "Batik", "Sintetis"])
harga = st.sidebar.slider("Harga (Rp)", 100000, 2000000, (200000, 800000))
ukuran = st.sidebar.multiselect("Ukuran", ["Small", "Medium", "Large"])
country = st.sidebar.selectbox("Country (Export)", ["Indonesia", "Singapore", "Malaysia", "USA", "Europe"])

# =======================
# DATA PRODUK (letakkan di atas, sekali saja)
# =======================
products = [
    {
        "kode": "P-TB-001",
        "name": "Blue Butterfly Woven Tote",
        "category": "Handmade Tote Bag",
        "desc": "Handcrafted woven tote bag decorated with vibrant blue butterfly motifs.",
        "price": 250000,
        "img": "data/assets/produk1.jpg"
    },
    {
        "kode": "P-CB-002",
        "name": "Monochrome Crossbody",
        "category": "Crossbody Bag",
        "desc": "Stylish crossbody bag in modern black & white pattern, lightweight & durable.",
        "price": 300000,
        "img": "data/assets/produk2.jpg"
    },
    {
        "kode": "P-TB-003",
        "name": "Floral Batik-Inspired Tote",
        "category": "Handmade Tote Bag",
        "desc": "Woven pandan tote bag with batik floral pattern in earthy tones.",
        "price": 250000,
        "img": "data/assets/produk3.jpg"
    }
]

# =======================
# HALAMAN HOME
# =======================
if page == "🏠 Home":
    st.markdown("<h1 style='text-align:center;'>✨ Tiga Putri ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:20px;'>Timeless Indonesian Craftsmanship</p>", unsafe_allow_html=True)
    st.image("data/assets/ban2.png", use_container_width=True)  # gambar hero/banner
    
    st.markdown("### 🌟 Featured Collection")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("data/assets/produk1.jpg")
        st.caption("Blue Butterfly Woven Tote")
    with col2:
        st.image("data/assets/produk2.jpg")
        st.caption("Monochrome Crossbody")
    with col3:
        st.image("data/assets/produk3.jpg")
        st.caption("Floral Batik-Inspired Tote")

# =======================
# HALAMAN ABOUT
# =======================
elif page == "🌍 About":
    st.markdown("<h1>About Us</h1>", unsafe_allow_html=True)
    st.write("""
    **Tiga Putri** is a proud Indonesian brand that brings high–quality woven bags and fashion pieces,  
    crafted with a blend of **traditional artistry** and **modern design**.  

    We believe in **elegance, authenticity, and sustainability** — values that shine through every product we create.  

    Our vision is to introduce the beauty of **handmade Indonesian craftsmanship** to the international market,  
    empowering local artisans while delivering timeless luxury to women around the world.
    """)

    st.markdown("---")

    # =======================
    # LAYANAN EKSPOR & IMPOR
    # =======================
    st.subheader("📦 Export & Import Services")
    st.write("""
    We provide **premium export and import services** in the fashion industry:
    - 🌍 Export of handmade products to various countries  
    - 📦 Import of premium raw materials for production  
    - 🤝 International business consulting services  
    """)

    st.markdown("---")

    # =======================
    # KONTAK
    # =======================
    st.subheader("📞 Contact Us")
    st.write("📧 Email:tigaputri@gmail.com")
    st.write("📱 WhatsApp: +62 812-3456-7890")
    st.write("📍 Address: Sukabumi, Indonesia")

    import streamlit as st

    st.write("Contact us for more information or to request an order:")

    with st.form("contact_form"):
        nama = st.text_input("Full Name")
        email = st.text_input("Email")
        pesan = st.text_area("Message")
        submit = st.form_submit_button("Submit")

        if submit:
            st.success(f"Thank you {nama}, your message has been sent!")

# =======================
# HALAMAN LOOKBOOK
# =======================
elif page == "📸 Lookbook":
    st.header("📸 Lookbook – Timeless Elegance by Tiga Putri")
    st.write("""
    Explore our curated lookbook collection.  
    Each design reflects **Indonesian artistry** blended with **modern elegance**.
    """)

    # Data Lookbook
    lookbook_items = [
        {
            "img": "data/assets/produk1.jpg",
            "title": "Blue Butterfly Woven Tote",
            "desc": "A handwoven tote with elegant blue butterfly motifs, spacious and durable — perfect for daily style with a natural touch."
        },
        {
            "img": "data/assets/produk2.jpg",
            "title": "Monochrome Crossbody",
            "desc": "A lightweight black-and-white woven crossbody bag with a modern pattern and braided strap, ideal for casual outings."
        },
        {
            "img": "data/assets/produk3.jpg",
            "title": "Floral Batik-Inspired Tote",
            "desc": "A pandan woven tote with batik-style floral accents, combining tradition and style for eco-friendly everyday use."
        }
    ]

    # Slider untuk navigasi
    index = st.slider("Swipe the Lookbook →", 0, len(lookbook_items)-1, 0)

    # Tampilkan item sesuai slider
    item = lookbook_items[index]
    st.image(item["img"], use_container_width=True)
    st.markdown(f"### {item['title']}")
    st.caption(item["desc"])

# =======================
# HALAMAN SHOP
# =======================
elif page == "🛍️ Shop":
    st.markdown("<h1 style='text-align:center;'>Shop Our Collections</h1>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, p in enumerate(products):
        col = cols[idx % len(cols)]   # aman kalau produk lebih dari 3
        with col:
            st.image(p["img"], use_container_width=True)
            st.markdown(f"**{p['name']}**")
            st.caption(p["category"])
            st.write(p["desc"])
            st.markdown(f"💰 **Rp {p['price']:,}**")

            if st.button("👜 Add to Bag", key=f"add_{p['kode']}"):
                st.session_state.cart.append(p)
                st.toast(f"Added {p['name']} to your bag", icon="👜")

elif page == "🛒 Cart":
    st.title("🛒 Your Shopping Bag")
    cart = st.session_state.cart
    if not cart:
        st.info("Your bag is empty.")
    else:
        total = 0
        for idx, item in enumerate(cart):
            c1, c2, c3 = st.columns([1, 6, 2])
            with c1:
                st.image(item["img"], width=80)
            with c2:
                st.markdown(f"**{item['name']}**")
                st.caption(item["category"])
                st.write(item["desc"])
                st.markdown(f"Rp {item['price']:,}")
            with c3:
                if st.button("❌ Remove", key=f"remove_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.experimental_rerun()
            total += item["price"]

        st.markdown(f"### 💵 Total: Rp {total:,}")
        if st.button("✅ Checkout (Simulation)"):
            st.success("Thank you! Your order has been placed (simulation).")
            st.session_state.cart = []

# =======================
# HALAMAN ACCOUNT
# =======================
elif page == "👤 Account":
    st.markdown("<h1 style='text-align:center;'>Account</h1>", unsafe_allow_html=True)
    st.write("Please enter your email below to access or create your account.")

    if "registered_users" not in st.session_state:
        # Simulasi database user {email: password}
        st.session_state.registered_users = {"demo@tigaputri.com": "12345"}

    if "user_email" not in st.session_state:
        # STEP 1: input email
        with st.form("account_form"):
            email = st.text_input("E-mail *", placeholder="yourname@domain.com")
            submitted = st.form_submit_button("Continue")

            if submitted:
                if not email:
                    st.error("⚠️ Required information")
                elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.error("⚠️ Expected format: yourname@domain.com")
                else:
                    st.session_state.user_email = email
                    st.experimental_rerun()

    else:
        # STEP 2: cek apakah email sudah terdaftar
        email = st.session_state.user_email
        st.info(f"📧 Email: {email}")

        if email in st.session_state.registered_users:
            # Minta password untuk login
            with st.form("login_form"):
                password = st.text_input("Password", type="password")
                login = st.form_submit_button("Login")

                if login:
                    if password == st.session_state.registered_users[email]:
                        st.success("✅ Login successful! Welcome back.")
                        if st.button("Logout"):
                            del st.session_state["user_email"]
                            st.experimental_rerun()
                    else:
                        st.error("❌ Incorrect password.")

            # Forgot password
            if st.button("Forgot Password?"):
                st.session_state["reset_mode"] = True

            if "reset_mode" in st.session_state and st.session_state["reset_mode"]:
                st.subheader("🔑 Reset Password")
                with st.form("reset_form"):
                    new_pass = st.text_input("Enter New Password", type="password")
                    confirm_pass = st.text_input("Confirm New Password", type="password")
                    reset = st.form_submit_button("Reset Password")

                    if reset:
                        if not new_pass or len(new_pass) < 10:
                            st.error("⚠️ Password must be at least 10 characters.")
                        elif new_pass != confirm_pass:
                            st.error("⚠️ Passwords do not match.")
                        else:
                            st.session_state.registered_users[email] = new_pass
                            st.success("🎉 Password reset successful! Please login again.")
                            del st.session_state["reset_mode"]
                            del st.session_state["user_email"]
                            st.experimental_rerun()

        else:
            # Akun baru → langsung ke form Create Account
            st.markdown("<h2>Create an account</h2>", unsafe_allow_html=True)
            st.write("By creating an account, you agree to accept the General Terms and Conditions of Use and that your data will be processed in compliance with the Privacy Policy of Tiga Putri.")
            st.markdown("*Required information")

            with st.form("create_account_form"):
                # Login Information
                password = st.text_input("Password *", type="password")
                confirm_password = st.text_input("Confirm Password *", type="password")

                # Password tips
                st.caption("For your security, we invite you to fill your password according to the following criteria:")
                st.write("- At least 10 characters\n- At least 1 uppercase letter\n- At least 1 lowercase letter\n- At least 1 number\n- At least 1 special character")

                # Personal Information
                st.subheader("Personal Information")
                title = st.selectbox("Title *", ["", "Mrs", "Ms", "Mr", "Dr"])
                first_name = st.text_input("First Name *")
                last_name = st.text_input("Last Name *")
                tel_code = st.text_input("Area Code *", "+62")
                tel_number = st.text_input("Telephone Number *", placeholder="Minimum 8 numbers")
                dob_month = st.selectbox("Month", list(range(1,13)))
                dob_day = st.selectbox("Day", list(range(1,32)))
                dob_year = st.selectbox("Year", list(range(1950,2025)))

                # Billing Information
                st.subheader("Billing Information")
                location = st.text_input("Location *", "Indonesia")
                company = st.text_input("Company (optional)")
                address = st.text_input("Address *")
                address2 = st.text_input("Address continued (optional)")
                city = st.text_input("City *")
                state = st.text_input("State *")
                zipcode = st.text_input("Zip code *")

                # Marketing consent
                marketing = st.checkbox("I agree to receive information by email about offers, services, products and events from Tiga Putri, in accordance with the Privacy Policy.")

                # Submit
                submit = st.form_submit_button("Create Account")

                if submit:
                    errors = []
                    if not password or len(password) < 10:
                        errors.append("Password must be at least 10 characters.")
                    if password != confirm_password:
                        errors.append("Passwords do not match.")
                    if not first_name:
                        errors.append("First name is required.")
                    if not last_name:
                        errors.append("Last name is required.")
                    if not tel_number.isdigit() or len(tel_number) < 8:
                        errors.append("Telephone number must be at least 8 digits.")
                    if not address or not city or not state or not zipcode:
                        errors.append("Address, city, state, and zip code are required.")

                    if errors:
                        for e in errors:
                            st.error(f"⚠️ {e}")
                    else:
                        st.session_state.registered_users[email] = password
                        st.success("🎉 Account created successfully! Welcome to Tiga Putri.")
                        st.session_state["user_account"] = {
                            "email": email,
                            "password": password,
                            "first_name": first_name,
                            "last_name": last_name,
                            "tel": f"{tel_code}{tel_number}",
                            "dob": f"{dob_day}-{dob_month}-{dob_year}",
                            "location": location,
                            "address": address,
                            "city": city,
                            "state": state,
                            "zip": zipcode,
                            "marketing": marketing
                        }
                        if st.button("Logout"):
                            del st.session_state["user_email"]
                            st.experimental_rerun()

# Footer
st.markdown("<div class='footer'>© 2025 Tiga Putri | Timeless Indonesian Craftsmanship</div>", unsafe_allow_html=True)
