pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // No checkout step needed for a basic pipeline
            }
        }

        stage('Build') {
            steps {
                // Build your script
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Deploy') {
            steps {
                // Run the script and deploy the result
                sh 'python example3.py'
                sh 'cp recognized.txt C:\ProgramData\Jenkins\.jenkins\workspace\Speech-to-text'
            }
        }
    }
}

