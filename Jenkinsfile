pipeline {
    agent any
    
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Build') {
            steps {
                // Build your script
                sh 'python example3.py'
            }
        }
    }
}

