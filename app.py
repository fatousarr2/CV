import streamlit as st

# ----- CONFIG PAGE -----
st.set_page_config(page_title="CV - FATOU SARR", layout="wide")

# ----- STYLE -----
page_bg = """
<style>
    body {
        background-color: #007BFF; /* Bleu */
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----- LAYOUT -----
col_main, col_side = st.columns([0.7, 0.3])

# ----- MAIN CONTENT -----
with col_main:
    st.title("Géomaticienne - SIG & Cartographie")

    st.write("""
    Étudiante en géomatique, passionnée par les SIG, la cartographie numérique et
    l’analyse des données spatiales. Je cherche à développer mes compétences
    à travers des projets et stages.
    """)

    st.markdown("---")

    # ----- FORMATION -----
    st.header("🎓 Parcours Académique")
    st.write("Licence en Géomatique – CEDT-G15 – 2024 / 2026")
    st.write("Baccalauréat Série L2 – Lycée de FISSEL – 2024")
    st.write("BFEM – Lycée de Fissel – 2020")

    st.markdown("---")

    # ----- COMPÉTENCES -----
    st.header("🛠 Compétences")
    col1, col2 = st.columns(2)

    with col1:
        st.write("✔️ Cartographie avec QGIS et ArcGIS")
        st.write("✔️ Collecte de données terrain (GPS, mobile, drone)")
        st.write("✔️ Bases en SIG et analyse spatiale")

    with col2:
        st.write("✔️ Plans 2D (AutoCAD) et 3D (SketchUp)")
        st.write("✔️ Maîtrise de Word, Excel et PowerPoint")
        st.write("✔️ Notions en télédétection")

    st.markdown("---")

    # ----- EXPERIENCES -----
    st.header("🚀 Expériences Académiques")
    st.write("📌 Projet universitaire : Cartographie d’un quartier")
    st.write("📌 Collecte et organisation des données terrain")
    st.write("📌 Création de cartes thématiques pour présentation")

    st.markdown("---")

    # ----- LOISIRS -----
    st.header("🎯 Loisirs")
    st.write("Sport")
    st.write("Cuisine")
    st.write("Réseaux sociaux")

# ----- SIDEBAR-LIKE COLUMN -----
with col_side:
    st.header("👤 Profil")
    st.write("FATOU SARR")
    st.write("📍 YOFF, Dakar")
    st.write("📧 fatousarr02012002@email.com")
    st.write("📞 +221 77 669 08 12")
    st.info("Disponible pour un stage en géomatique")

    st.markdown("---")

    st.header("🌐 Langues")
    st.write("Français – courant")
    st.write("Wolof – courant")
    st.write("Anglais – intermédiaire")
