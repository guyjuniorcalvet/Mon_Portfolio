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
        "Curieux, rigoureux et orient� r�sultats, je combine une formation en science des donn�es et intelligence des affaires avec une exp�rience en service � la client�le et en gestion de projet. Je m�int�resse particuli�rement � l�analyse pr�dictive, � la visualisation de donn�es et � l�optimisation de processus.Mon objectif est de b�tir une carri�re o� je peux contribuer � transformer les donn�es en leviers strat�giques pour les organisations, tout en d�veloppant des projets concrets � impact r�el.",
  skills: ["Programmation Orient�e Objets (POO)", "C++","HTML", "R", "Python", "Jira", "PowerBI", "Optimisation"],
  projects: [
    {
      name: "Classification-Clients-et-Images-avec-Reseaux-Neuronaux",
      description:
        "Deux projets de classification avec des r�seaux de neurones : un PMC avec Scikit-Learn pour des donn�es tabulaires et des CNN avec TensorFlow/Keras pour des images.",
      link: "https://github.com/guyjuniorcalvet/Reseaux_de_neurones_LM",
      skills: ["JupyterNotebook", "Python", "TensorFlow", "Keras", "CNN", "VGG16", "Scikit-Learn"],
    },
    {
      name: "Rotaract_de_Delmas_Shiny",
      description:
        "Application d'alimentation (Shiny) et de gestion de la base de donn�es du Rotaract de Delmas connect�e � leur Base de donn�es MySQL (h�berg�e dans le cloud).",
      link: "https://github.com/guyjuniorcalvet/Rotaract_delmas_Shiny",
      skills: ["Rstudio", "R", "Shiny", "Pool", "Oracle","SQL", "MySQL", "Googlecloud", "Supabase"],
    },
  ],
  experience: [
    {
      company: "Universit� du Qu�bec � Chicoutimi",
      title: "Stage-Projet �t� 2025",
      dateRange: "8 semaines",
      bullets: [
          "Projet de cr�ation d�une interface interactive et intuitive (Shiny) qui est connect�e � la base de donn�es MySQL d�une organisation communautaire bas�e en Ha�ti, le Rotaract Club Delmas.",
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
      school: "Universit� du Qu�bec � Chicoutimi",
      degree: "Baccalaur�at en informatique-Sciences des donn�es et de l'intelligence d'affaires",
      dateRange: "2023 - 2026",
      achievements: [
        "Etudiant en derni�re ann�e",
        "Membre de l'�quipe de l'UQAC au CSGames25 � l'UlAVAL",
      ],
    },
    {
      school: "Universit� Notre Dame d'Haiti - FSESP",
      degree: "Licence en Administration des affaires",
      dateRange: "2017 - 2021",
      achievements: [
        "Moyenne g�n�rale de 80/100 avec plus de 120 cr�dits",
        "Membre du comit� des clubs d'Echecs, de lecture et du b�n�volat",
      ],
    },
  ],
};
