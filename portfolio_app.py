import streamlit as st
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import os
import openai

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
    
    "chatbot_header": "Pourquoi m'embaucher ?",
    "chatbot_description": "Décrivez le poste en question et l'IA vous expliquera pourquoi je suis le candidat idéal.",
    "job_description_label": "Écrivez ou collez la description du poste ici...",
    "analyze_button": "Analyser",
    "analysis_result_header": "Analyse de ma candidature",
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

    "chatbot_header": "Why Hire Me?",
    "chatbot_description": "Describe the job and the AI will explain why I am the ideal candidate.",
    "job_description_label": "Write or paste the job description here...",
    "analyze_button": "Analyze",
    "analysis_result_header": "My Candidacy Analysis",
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

# --- CHATBOT SECTION ---
with st.container():
    st.write("---")
    st.header(content["chatbot_header"])
    st.write(content["chatbot_description"])

    job_description = st.text_area(label=content["job_description_label"], height=200)

    if st.button(content["analyze_button"]):
        if job_description:
            with st.spinner("Analyse en cours..."):
                # --- USER PROFILE ---
                user_profile = """
                **Profil :**
                Étudiant en Baccalauréat en informatique - science des données et de l'intelligence d'affaires, passionné par la conception de solutions logicielles modernes pour résoudre des problèmes complexes. Je m'intéresse particulièrement à la mise en place de pratiques DevOps et à la sécurisation des applications pour garantir la protection des données.

                **Compétences Techniques :**
                - Méthodologies : Agile (Scrum), POO, Cycle de développement de Logiciel (SDLC)
                - Gestion de bases de données : SQL, Oracle
                - Outils : Visual Studio 2022, Git
                - Langages : Python, R, C++
                - Spécialisation : Structuration de pipelines de données

                **Expérience Professionnelle :**
                - **Stage universitaire / Superviseur : Aurélien Nicosia (06/2025 - 07/2025) :** Création d'une interface interactive et intuitive (Shiny) connectée à une base de données MySQL pour une organisation communautaire en Haïti (Rotaract Club Delmas).
                - **Flex driver / FEDEX (Depuis 05/2024) :** Chauffeur de courrier à temps partiel.

                **Formation :**
                - **Bacc en Informatique-Scs des données et de l'intelligence d'affaires, UQAC (2023 - 2026)**
                - **Licence en Administration des affaires, Université Notre Dame d'Haïti (2017 - 2021)**

                **Activités :**
                - Participation aux CSGAMES25 à l'ULaval.
                - Membre du club Rotaract de Delmas depuis Mars 2020.

                **Objectifs de Carrière et Personnalité :**
                - **Objectif :** Recherche un poste (stage ou emploi) qui contribue à mes études, avec une préférence pour le développement d'applications et de logiciels, idéalement dans le secteur de la finance.
                - **Personnalité :** Autonome, dynamique, très collaboratif et motivé par l'apprentissage continu.
                - **Approche :** Je vois les difficultés comme des défis à affronter de manière structurée, étape par étape.
                - **Localisation :** Ouvert à toute opportunité, avec une préférence pour Saguenay ou la ville de Québec. Télétravail bienvenu.
                """

                # --- PROMPT FOR OPENAI ---
                prompt = f"""
                Tu es un assistant IA expert en recrutement. Ton rôle est d'agir comme si tu étais Guy Junior CALVET et de rédiger une lettre de motivation courte et percutante.
                Analyse la description de poste suivante et utilise les informations du profil de Guy Junior CALVET pour expliquer pourquoi il est le candidat idéal.

                **Profil de Guy Junior CALVET :**
                {user_profile}

                **Description du poste :**
                {job_description}

                **Instructions :**
                1.  Commence par une phrase d'accroche qui montre que tu as compris le besoin de l'entreprise.
                2.  Mets en évidence 2 ou 3 compétences ou expériences clés du profil de Guy qui correspondent PARFAITEMENT à l'offre.
                3.  Mentionne sa motivation et ses qualités personnelles (soft skills) en lien avec le poste ou l'entreprise.
                4.  Si la localisation du poste correspond aux préférences de Guy (Saguenay, Québec, ou télétravail), mentionne-le comme un atout.
                5.  Conclus par une phrase enthousiaste pour proposer un entretien.
                6.  La réponse doit être rédigée à la première personne ("Je", "Mon", "Ma").
                7.  Sois concis, professionnel et convaincant.
                """

                try:
                    openai.api_key = st.secrets["OPENAI_API_KEY"]
                    response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "Tu es un assistant IA expert en recrutement agissant au nom de Guy Junior CALVET."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    st.subheader(content["analysis_result_header"])
                    st.success(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Une erreur est survenue : {e}")
        else:
            st.warning("Veuillez coller une description de poste pour l'analyse.")


# --- FOOTER ---
st.write("---")
st.write("© 2025 | Made with ❤️ using Streamlit")
