# ♾️ DevOps Masterclass: Jenkins, Git, CloudBees

## 1. Git (Version Control)
The brain of the operation.

### Essential Commands
```bash
git init                # Start repo
git clone <url>        # Download
git branch feature-x   # Create branch
git checkout feature-x # Switch branch
git add .              # Stage files
git commit -m "Msg"    # Save snapshot
git push origin main   # Upload
git pull               # Download updates
```

### Pull Requests (PR)
*   Never push to `main` directly.
*   Push to `feature-branch` -> Open PR -> Review -> Merge.

---

## 2. Jenkins (CI/CD)
The Automation Server. It runs your tests automatically.

### What is a Pipeline?
A script that defines the build steps.

### Sample Jenkinsfile (Groovy)
This file lives in your repo root. Jenkins reads it.
```groovy
pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Installing Dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running Robot Framework...'
                sh 'robot tests/'
            }
        }
        
        stage('Deploy') {
            when { branch 'main' }
            steps {
                echo 'Deploying to Prod...'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts 'reports/**' # Save html reports
        }
    }
}
```

---

## 3. CloudBees
**What is it?** Enterprise Jenkins.
*   **Scalability**: Manages Jenkins masters/agents effectively.
*   **Governance**: Enforces security policies across teams.
*   **Analytics**: Shows build trends/failures.

In an interview, say: *"I used CloudBees Core to manage our Jenkins pipelines, ensuring high availability and standardized build templates."*
