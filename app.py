import streamlit as st
from engine_final import generate_recommendations, load_master_colors, SKIN_PROFILES

st.set_page_config(layout="wide")

st.sidebar.header("🎨 Card Customization")

card_width = st.sidebar.slider("Card Width (px)", 600, 1400, 1000)
border_radius = st.sidebar.slider("Border Radius", 0, 30, 12)
font_size = st.sidebar.slider("Font Size", 10, 24, 14)

show_labels = st.sidebar.checkbox("Show Color Names", True)
show_titles = st.sidebar.checkbox("Show Section Titles", True)

bg_style = st.sidebar.selectbox("Background Style", ["White", "Light Grey", "Dark"])

st.sidebar.header("👤 User Input")

colors = load_master_colors()
color_names = list(colors.keys())

shirts = st.sidebar.multiselect("Shirts", color_names)
pants = st.sidebar.multiselect("Pants", color_names)

season = st.sidebar.selectbox("Season", ["All", "Spring", "Summer", "Autumn", "Winter"])

skin_profile = st.sidebar.selectbox("Skin Profile", ["None"] + list(SKIN_PROFILES.keys()))
contrast = st.sidebar.selectbox("Contrast", ["None", "High", "Low"])

if skin_profile == "None":
    skin_profile = None
if contrast == "None":
    contrast = None

input_data = {
    "shirts": shirts,
    "pants": pants,
    "season": season,
    "skin_profile": skin_profile,
    "contrast_preference": contrast
}

results = generate_recommendations(input_data)

bg_map = {
    "White": "#FFFFFF",
    "Light Grey": "#F5F5F5",
    "Dark": "#1E1E1E"
}

background = bg_map[bg_style]

st.markdown(f'''
<div style="
    max-width:{card_width}px;
    margin:auto;
    background:{background};
    border-radius:{border_radius}px;
    padding:20px;
    box-shadow:0px 10px 25px rgba(0,0,0,0.2);
">
''', unsafe_allow_html=True)

def render_row(title, items):

    if show_titles:
        st.markdown(f"### {title}")

    html = f"""
    <div style="
        display:flex;
        width:100%;
        overflow:hidden;
        border-radius:{border_radius}px;
        margin-bottom:15px;
    ">
    """

    for item in items:
        text_color = "#000" if item["hex"] in ["#FFFFFF", "#F5F5DC"] else "#FFF"

        html += f"""
        <div style="
            flex:1;
            background:{item['hex']};
            height:90px;
            display:flex;
            align-items:flex-end;
            justify-content:center;
            color:{text_color};
            font-size:{font_size}px;
            font-weight:600;
        ">
            {item['color'] if show_labels else ""}
        </div>
        """

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

render_row("Smart Shirts", results["smart_shirts"])
render_row("Smart Pants", results["smart_pants"])
render_row("Core Neutrals", results["all_season_neutrals"])

st.markdown("</div>", unsafe_allow_html=True)
