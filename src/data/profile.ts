export const PROFILE = {
    name: "Prasanna Adithya",
    role: "Data Validation & Automation Engineer",
    title: "QE Automation | Python Developer | Data Validation Expert",
    about: `I am an emotionally resilient and self-driven Problem Solver with a passion for Data Validation and Automation. 
  I specialize in building modular Python architectures for complex data reconciliation tasks, ranging from file-to-file comparisons to database validations.
  With deep expertise in handling DataFrame comparisons, fixed-width file processing, and dynamic configuration systems, I ensure data integrity across large-scale systems.`,
    social: {
        github: "https://github.com/prasannaadithya-zeref",
        linkedin: "#", // User didn't provide, leaving placeholder
        email: "mailto:contact@example.com" // User didn't provide
    },
    skills: {
        languages: ["Python", "SQL (Oracle, PostgreSQL, Redshift, MongoDB)", "Gherkin (Behave)"],
        frameworks: ["Robot Framework", "Pandas", "Pytest", "React", "Node.js"],
        tools: ["AWS S3", "Jenkins", "CloudBees", "Git", "JIRA"],
        concepts: [
            "Data Validation",
            "DataFrame Comparisons",
            "ETL Testing",
            "Fixed-width File Processing",
            "Log Parsing",
            "CI/CD Implementation"
        ]
    },
    experience: [
        {
            role: "Data Validation & Automation Engineer",
            company: "Current Company",
            period: "Present",
            description: "Leading automation initiatives for data reconciliation and validation frameworks.",
            achievements: [
                "Developed a modular Python framework for file-to-file and file-to-table reconciliation driven by dynamic .properties files.",
                "Implemented rigorous exception handling and mismatch reporting for DataFrame comparisons.",
                "Automated header/detail/trailer validation for fixed-width file processing.",
                "Integrated AWS S3 for cloud-based data validation workflows."
            ]
        }
    ],
    projects: [
        {
            title: "Data Reconciliation Framework",
            description: "A Python-based framework for comparing large datasets across different formats (CSV, Fixed-width, Database). Features dynamic configuration and detailed HTML reporting.",
            tech: ["Python", "Pandas", "SQL", "HTML Reports"],
            link: "#"
        },
        {
            title: "Log Parsing & Validation Tool",
            description: "Automated tool to parse complex application logs and validate business logic execution against expected patterns.",
            tech: ["Python", "Regex", "File I/O"],
            link: "#"
        },
        {
            title: "Portfolio Website",
            description: "My personal portfolio highlighting my automation and testing work.",
            tech: ["React", "Tailwind CSS", "Framer Motion"],
            link: "https://github.com/prasannaadithya-zeref/Automation-portfolio-rnd"
        }
    ]
}
