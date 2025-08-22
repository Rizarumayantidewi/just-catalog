import streamlit as st

# Add Logo
st.image("data/logo3p.png", width=150)  # ganti dengan path logo kamu

# Title
st.subheader("📦 Pandan Product Catalog")

# Product data (example, replace with CSV/Database)
products = [
    {"name": "Pandan Bag with Floral Motif - Elegant Pink", "price": 150000, "desc": "Combination of woven pandan + crocodile-pattern synthetic leather.", "Color": "Pink & white with printed floral design.", "Size": "35 x 28 x 12 cm.", "Features": "2 strong handles, 1 main compartment with zipper." , "Advantages": "Perfect for casual & semi-formal occasions, lightweight yet elegant", "img": "data/IMG20250817152213.jpg"},
    {"name": "Pandan Bag with Butterfly Motif - Blue & White", "price": 150000, "desc": "Natural woven pandan + braided synthetic handles.", "Color": "White with blue butterfly motif.", "Size": "40 x 30 x 12 cm.", "Features": "Long shoulder handles, spacious inner compartment." , "Advantages": "Unique design, ideal for shopping, casual walks, or vacation trips", "img": "data/IMG20250817162412.jpg"},
    {"name": "Natural Woven Pandan Bag - Rose Motif", "price": 150000, "desc": "Natural pandan weave + jute fabric combination.", "Color": "Natural brown & white with pink rose motif.", "Size": "38 x 30 x 13 cm.", "Features": "Thick & durable handles, main zipper closure." , "Advantages": "Natural & eco-friendly look, suitable for both casual and formal fashion", "img": "data/IMG20250817163843.jpg"},
]

# --- Filter ---
search = st.text_input("🔍 Search product")
min_price, max_price = st.slider(
    "💰 Price Filter", 
    min_value=0, max_value=200000, 
    value=(0, 200000), step=10000
)

# Filter products based on search & price
filtered_products = [
    p for p in products 
    if search.lower() in p["name"].lower() 
    and min_price <= p["price"] <= max_price
]

st.write(f"Showing {len(filtered_products)} filtered products:")

# --- Layout Grid (3 columns) ---
cols = st.columns(3)
for i, product in enumerate(filtered_products):
    with cols[i % 3]:
        st.image(product["img"], width=150)
        st.subheader(product["name"])
        st.write(product["desc"])
        st.write(f"💰 Rp {product['price']:,}")

        st.markdown(f"[🛒 Buy Now via Gmail]")
