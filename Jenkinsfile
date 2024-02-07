pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from your Git repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Install dependencies or run any build steps
                bat 'pip install -r recognized.txt' // Use 'bat' for Windows shell
            }
        }

        stage('Deploy') {
            steps {
                // Run your Python script and deploy the result
                bat 'python example3.py'                // Use 'bat' for Windows shell
                bat 'copy recognized.txt C:\\Users\\KNAGASWE\\Documents\\speechtotext' // Use 'bat' for Windows shell
            }
        }
    }
}

