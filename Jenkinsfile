pipeline {
    agent any
    
    stages {
        stage('Bulid') {
            steps {
                bat 'robotframework --version'
            }
        }

        stage('Test') {
            steps {
                bat 'robot task_suite.robot'
            }
        }

        stage('Deploy') {
            steps {
                // Run your Python script and deploy the result
                bat 'copy recognized1.txt C:\\Users\\KNAGASWE\\Documents\\speechtotext'  // Use 'bat' for Windows shell
            }
        }
    }
}
 post {
        success {
            echo 'Pipeline succeeded! Your code is built, tested, and deployed successfully.'
        }
        failure {
            echo 'Pipeline failed! Please check the build, test, or deployment logs for errors.'
        }
    }


