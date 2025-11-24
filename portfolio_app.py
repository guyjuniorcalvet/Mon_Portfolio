import streamlit as st
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import os

# --- GET CWD ---
CWD = os.path.dirname(__file__)
IMG_PATH = os.path.join(CWD, "IMG_9432.JPG")
CV_PATH = os.path.join(CWD, "GuyJuniorCalvet_CV.pdf")

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Mon_Portfolio | Guy Junior Calvet"
PAGE_ICON = "random"
NAME = "Guy Junior Calvet"
DESCRIPTION = """
3rd year Computer Science student, specializing in BI and Web Development.
"""
EMAIL = "juniorguycalvet@gmail.com"
LINKEDIN = "https://linkedin.com/in/guyjuniorcalvet"
GITHUB = "https://github.com/guyjuniorcalvet"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LANGUAGE SELECTION ---
lang_dict = {
    "Français": "fr",
    "English": "en"
}
lang_options = list(lang_dict.keys())
selected_lang_text = st.sidebar.selectbox("Language / Langue", lang_options)
lang = lang_dict[selected_lang_text]

# --- CONTENT DICTIONARIES ---
content_fr = {
    "bio_title": "Ma Bio",
    "linkedin_button": "Mon LinkedIn",
    "github_button": "Mon GitHub",
    "cv_button": "Télécharger mon CV",
    "cv_file": CV_PATH,  # Make sure you have this file
    "projects_header": "Mes Projets",
    "project_link_button": "Voir le projet",

    "project1_title": "Classification-Clients-et-Images-avec-Reseaux-Neuronaux",
    "project1_desc": "Deux projets de classification avec des reseaux de neurones : un PMC avec Scikit-Learn pour des donnees tabulaires et des CNN avec TensorFlow/Keras pour des images.",
    "project1_tech": "JupyterNotebook, Python, TensorFlow, Keras, CNN, VGG16, Scikit-Learn",
    "project1_link": "https://github.com/guyjuniorcalvet/Reseaux_de_neurones_LM",
    
    "project2_title": "Rotaract_de_Delmas_Shiny",
    "project2_desc": "Application d'alimentation (Shiny) et de gestion de la base de donnees du Rotaract de Delmas connectee leur Base de donnees MySQL (hebergee dans le cloud).",
    "project2_tech": "Rstudio, R, Shiny, Pool, Oracle, SQL, MySQL, Googlecloud, Supabase",
    "project2_link": "https://github.com/guyjuniorcalvet/Rotaract_delmas_Shiny",

   "project3_title": "MINI-ARCADE PROJET WEB en Collaboration avec des étudiant(e)s (5 collabo) en jeux video et en génie informatique",
    "project3_desc": "Developpement d'un site web interactif de mini-jeux d'arcade qui booste l'apprentissage tout en s'amusant pour des enfants",
    "project3_tech": "Backend = Node.js, Express, MongoDB // Frontend = HTML, CSS, JavaScript",
    "project3_link": "https://github.com/users/casstoipaslatete/projects/1/views/1",

    "project5_title": "Votre Prochain Super Projet",
    "project5_desc": "Description de votre projet ici. Expliquez le problème que vous avez résolu et votre solution.",
    "project5_tech": "Python, Streamlit, ...",
    "project5_info": "Ceci est un emplacement réservé. Vous pouvez le modifier pour ajouter votre troisième projet.",
    "project_header": "Projet Interactif : Analyseur de Sentiments",
    "project_description": "Entrez une phrase et l'IA analysera si le sentiment est positif, négatif ou neutre.",
    "text_input_label": "Votre texte ici...",
    "analyze_button": "Analyser",
    "analysis_result_header": "Résultat de l'analyse",
    "sentiment_label": "Sentiment détecté",
    "subjectivity_label": "Subjectivité",
    "positive": "Positif",
    "negative": "Négatif",
    "neutral": "Neutre",
}

content_en = {
    "bio_title": "My Bio",
    "linkedin_button": "My LinkedIn",
    "github_button": "My GitHub",
    "cv_button": "Download My CV",
    "cv_file": CV_PATH, # Make sure you have this file
    "projects_header": "My Projects",
    "project_link_button": "View Project",

    "project1_title": "Client and Image Classification with Neural Networks",
    "project1_desc": "Two classification projects with neural networks: a PMC with Scikit-Learn for tabular data and a CNN with TensorFlow/Keras for images.",
    "project1_tech": "JupyterNotebook, Python, TensorFlow, Keras, CNN, VGG16, Scikit-Learn",
    "project1_link": "https://github.com/guyjuniorcalvet/Classification-Clients-et-Images-avec-Reseaux-Neuronaux",

    "project2_title": "Rotaract_de_Delmas_Shiny",
    "project2_desc": "A Shiny application for data entry and management of the Rotaract de Delmas database connected to their MySQL database (hosted in the cloud).",
    "project2_tech": "Rstudio, R, Shiny, Pool, Oracle, SQL, MySQL, Googlecloud, Supabase",
    "project2_link": "https://github.com/guyjuniorcalvet/Rotaract_delmas_Shiny",

    "project3_title": "MINI-ARCADE WEB PROJECT in collaboration with video game and computer engineering students (5 collaborators)","project3_title": "MINI-ARCADE WEB PROJECT in collaboration with video game and computer engineering students (5 collaborators)",
    "project3_desc": "Development of an interactive mini-arcade game website that boosts learning while having fun for children.",
    "project3_tech": "Backend = Node.js, Express, MongoDB // Frontend = HTML, CSS, JavaScript",
    "project3_link": "https://github.com/users/casstoipaslatete/projects/1/views/1",

    "project_header": "Interactive Project: Sentiment Analyzer",
    "project_description": "Enter a sentence and the AI will analyze if the sentiment is positive, negative, or neutral.",
    "text_input_label": "Your text here...",
    "analyze_button": "Analyze",
    "analysis_result_header": "Analysis Result",
    "sentiment_label": "Detected Sentiment",
    "subjectivity_label": "Subjectivity",
    "positive": "Positive",
    "negative": "Negative",
    "neutral": "Neutral",
}

content = content_fr if lang == "fr" else content_en

# --- HEADER SECTION ---
with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        # You can upload your photo to the same directory and use st.image("your_photo.png")
        st.image(IMG_PATH, width=250)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.write("📫", EMAIL)

# --- ACTION BUTTONS ---
with st.container():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button(content["linkedin_button"], LINKEDIN, use_container_width=True)
    with col2:
        st.link_button(content["github_button"], GITHUB, use_container_width=True)
    with col3:
        # To add a CV download button
        with open(content["cv_file"], "rb") as file:
            st.download_button(
                label=content["cv_button"],
                data=file,
                file_name=content["cv_file"],
                mime="application/octet-stream",
                use_container_width=True
            )

# --- PROJECTS SECTION ---
with st.container():
    st.write("---")
    st.header(content["projects_header"])
    
    # --- Project 1 ---
    with st.expander(f"🧠 {content['project1_title']}"):
        st.write(content['project1_desc'])
        st.write(f"**Technologies:** {content['project1_tech']}")
        st.link_button(content["project_link_button"], content["project1_link"])

    # --- Project 2 ---
    with st.expander(f"📊 {content['project2_title']}"):
        st.write(content['project2_desc'])
        st.write(f"**Technologies:** {content['project2_tech']}")
        st.link_button(content["project_link_button"], content["project2_link"])

    # --- Project 3: Placeholder ---
    with st.expander(f"✨ {content['project3_title']}"):
        st.write(content['project3_desc'])
        st.write(f"**Technologies:** {content['project3_tech']}")
        st.link_button(content["project_link_button"], content["project3_link"])

# --- INTERACTIVE PROJECT SECTION ---
with st.container():
    st.write("---")
    st.header(content["project_header"])
    st.write(content["project_description"])

    user_text = st.text_area(label=content["text_input_label"], height=100)

    if st.button(content["analyze_button"]):
        if user_text:
            st.subheader(content["analysis_result_header"])
            
            if lang == 'fr':
                blob = TextBlob(user_text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
                polarity = blob.sentiment[0]
            else:
                blob = TextBlob(user_text)
                polarity = blob.sentiment.polarity

            if polarity > 0.1:
                sentiment = f"✅ {content['positive']}"
            elif polarity < -0.1:
                sentiment = f"❌ {content['negative']}"
            else:
                sentiment = f"😐 {content['neutral']}"

            st.write(f"**{content['sentiment_label']}:** {sentiment}")
            
            if lang == 'en': # Subjectivity is more reliable for English with TextBlob
                 st.write(f"**{content['subjectivity_label']}:** {blob.sentiment.subjectivity:.2f}")

        else:
            st.warning("Please enter some text to analyze.")

# --- FOOTER ---
st.write("---")
st.write("© 2025 | Made with ❤️ using Streamlit")
