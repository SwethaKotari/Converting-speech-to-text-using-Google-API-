pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Check Robot Framework version
                bat 'robot --version'
            }
        }

        stage('Test') {
            steps {
                // Execute Robot Framework test suite
                bat 'robot task_suite.robot'
            }
        }

        stage('Deploy') {
            steps {
                // Copy recognized1.txt to the destination directory
                bat 'copy recognized1.txt C:\\Users\\KNAGASWE\\Documents\\speechtotext'  // Use 'bat' for Windows shell
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
}


