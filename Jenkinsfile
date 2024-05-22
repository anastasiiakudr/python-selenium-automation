pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    docker.build('pytest-selenium')
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests using Docker Compose
                    sh 'docker-compose up --abort-on-container-exit'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker containers
                sh 'docker-compose down'
            }
        }
    }
}
