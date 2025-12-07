// CI/CD LEVEL 1: JENKINSFILE EXPLAINED
// ======================================
// This is the actual code that runs your automation in the cloud.

pipeline {
    agent any // Run on any available machine (Node)

    environment {
        // Define secrets here (never hardcode passwords!)
        DB_PASS = credentials('db-password-secret') 
    }

    stages {
        // Stage 1: Checkout Code
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/my-repo.git'
            }
        }

        // Stage 2: Install
        stage('Setup') {
            steps {
                echo 'Installing Python Dependencies...'
                // sh runs shell commands (Linux) or bat (Windows)
                sh 'pip install -r requirements.txt' 
            }
        }

        // Stage 3: Test
        stage('Execution') {
            parallel { // ADVANCED: Run styles in parallel!
                stage('API Tests') {
                    steps { sh 'robot tests/api_suite.robot' }
                }
                stage('UI Tests') {
                    steps { sh 'robot tests/ui_suite.robot' }
                }
            }
        }
    }
    
    // Stage 4: Reporting (Always runs)
    post {
        always {
            junit 'reports/*.xml' // Process results for graph
            archiveArtifacts 'reports/*.html' // Save HTML for download
        }
        failure {
            // Slack Notification would go here
            echo 'Build Failed! Sending Alert...'
        }
    }
}

// [HANDS ON TASK]
// Copy this file to the root of your repo as 'Jenkinsfile'.
// If you have Jenkins installed locally, create a "Pipeline" job and point it to your Git.
