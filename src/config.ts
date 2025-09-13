export const siteConfig = {
  name: "Guy Junior CALVET",
  title: "Junior Data Engineering/Business Intelligence",
  description: "Portfolio de Guy Junior CALVET",
  accentColor: "#1d4ed8",
  social: {
    email: "juniorguycalvet.com",
    linkedin: "https://www.linkedin.com/in/guyjuniorcalvet",
    github: "https://github.com/guyjuniorcalvet",
  },
  aboutMe:
        "Curieux, rigoureux et orienté résultats, je combine une formation en science des données et intelligence des affaires avec une expérience en service à la clientèle et en gestion de projet. Je m’intéresse particulièrement à l’analyse prédictive, à la visualisation de données et à l’optimisation de processus.Mon objectif est de bâtir une carrière où je peux contribuer à transformer les données en leviers stratégiques pour les organisations, tout en développant des projets concrets à impact réel.",
  skills: ["Programmation Orientée Objets (POO)", "C++","HTML", "R", "Python", "Jira", "PowerBI", "Optimisation"],
  projects: [
    {
      name: "Classification-Clients-et-Images-avec-Reseaux-Neuronaux",
      description:
        "Deux projets de classification avec des réseaux de neurones : un PMC avec Scikit-Learn pour des données tabulaires et des CNN avec TensorFlow/Keras pour des images.",
      link: "https://github.com/guyjuniorcalvet/Reseaux_de_neurones_LM",
      skills: ["JupyterNotebook", "Python", "TensorFlow", "Keras", "CNN", "VGG16", "Scikit-Learn"],
    },
    {
      name: "Rotaract_de_Delmas_Shiny",
      description:
        "Application d'alimentation (Shiny) et de gestion de la base de données du Rotaract de Delmas connectée à leur Base de données MySQL (hébergée dans le cloud).",
      link: "https://github.com/guyjuniorcalvet/Rotaract_delmas_Shiny",
      skills: ["Rstudio", "R", "Shiny", "Pool", "Oracle","SQL", "MySQL", "Googlecloud", "Supabase"],
    },
  ],
  experience: [
    {
      company: "Université du Québec à Chicoutimi",
      title: "Stage-Projet été 2025",
      dateRange: "8 semaines",
      bullets: [
          "Projet de création d’une interface interactive et intuitive (Shiny) qui est connectée à la base de données MySQL d’une organisation communautaire basée en Haïti, le Rotaract Club Delmas.",
      ],
    },
    {
      company: "Startup Inc",
      title: "Full Stack Developer",
      dateRange: "Jun 2020 - Dec 2021",
      bullets: [
        "Built and launched MVP product from scratch using React and Node.js",
        "Implemented CI/CD pipeline reducing deployment time by 60%",
        "Collaborated with product team to define technical requirements",
      ],
    },
    {
      company: "Digital Agency",
      title: "Frontend Developer",
      dateRange: "Aug 2018 - May 2020",
      bullets: [
        "Developed responsive web applications for 20+ clients",
        "Improved site performance scores by 35% on average",
        "Introduced modern JavaScript frameworks to legacy codebases",
      ],
    },
  ],
  education: [
    {
      school: "Université du Québec à Chicoutimi",
      degree: "Baccalauréat en informatique-Sciences des données et de l'intelligence d'affaires",
      dateRange: "2023 - 2026",
      achievements: [
        "Etudiant en dernière année",
        "Membre de l'équipe de l'UQAC au CSGames25 à l'UlAVAL",
      ],
    },
    {
      school: "Université Notre Dame d'Haiti - FSESP",
      degree: "Licence en Administration des affaires",
      dateRange: "2017 - 2021",
      achievements: [
        "Moyenne générale de 80/100 avec plus de 120 crédits",
        "Membre du comité des clubs d'Echecs, de lecture et du bénévolat",
      ],
    },
  ],
};
