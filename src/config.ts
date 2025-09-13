export const siteConfig = {
  name: "Guy Junior CALVET",
  title: "Junior Data Engineering/Business Intelligence",
  description: "Portfolio de Guy Junior CALVET",
  accentColor: "#1d4ed8",
  social: {
    email: "juniorguycalvet@gmail.com",
    linkedin: "https://www.linkedin.com/in/guyjuniorcalvet",
    github: "https://github.com/guyjuniorcalvet",
  },
  AboutMe:
        "Curieux, rigoureux et oriente resultats, je combine une formation en science des donnees et intelligence des affaires avec une experience en service a la clientele et en gestion de projet. Je m’interesse particulierement a l’analyse predictive, a la visualisation de donnees et a l’optimisation de processus.Mon objectif est de batir une carriere ou je peux contribuer a transformer les donnees en leviers strategiques pour les organisations, tout en developpant des projets concrets a impact reel.",
  skills: ["Programmation Orientée Objets (POO)", "C++","HTML", "R", "Python", "Jira", "PowerBI", "Optimisation"],
  projects: [
    {
      name: "Classification-Clients-et-Images-avec-Reseaux-Neuronaux",
      description:
        "Deux projets de classification avec des reseaux de neurones : un PMC avec Scikit-Learn pour des donnees tabulaires et des CNN avec TensorFlow/Keras pour des images.",
      link: "https://github.com/guyjuniorcalvet/Reseaux_de_neurones_LM",
      skills: ["JupyterNotebook", "Python", "TensorFlow", "Keras", "CNN", "VGG16", "Scikit-Learn"],
    },
    {
      name: "Rotaract_de_Delmas_Shiny",
      description:
        "Application d'alimentation (Shiny) et de gestion de la base de donnees du Rotaract de Delmas connectee à leur Base de donnees MySQL (hebergee dans le cloud).",
      link: "https://github.com/guyjuniorcalvet/Rotaract_delmas_Shiny",
      skills: ["Rstudio", "R", "Shiny", "Pool", "Oracle","SQL", "MySQL", "Googlecloud", "Supabase"],
    },
  ],
  experience: [
    {
      company: "Universite du Quebec a Chicoutimi",
      title: "Stage-Projet ete 2025",
      dateRange: "8 semaines",
      bullets: [
          "Projet de creation d’une interface interactive et intuitive (Shiny) qui est connectee a la base de donnees MySQL d’une organisation communautaire basee en Haiti, le Rotaract Club Delmas.",
      ],
    },
  ],
  education: [
    {
      school: "Universite du Quebec a Chicoutimi",
      degree: "Baccalaureat en informatique-Sciences des donnees et de l'intelligence d'affaires",
      dateRange: "2023 - 2026",
      achievements: [
        "Etudiant en dernière annee",
        "Membre de l'equipe de l'UQAC au CSGames25 a l'UlAVAL",
      ],
    },
    {
      school: "Université Notre Dame d'Haiti - FSESP",
      degree: "Licence en Administration des affaires",
      dateRange: "2017 - 2021",
      achievements: [
        "Moyenne genérale de 80/100 avec plus de 120 crédits",
        "Membre du comité des clubs d'Echecs, de lecture et du bénévolat",
      ],
    },
  ],
};
