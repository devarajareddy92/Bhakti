pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
              git branch: 'main',
                  url: 'https://github.com/devarajareddy92/Bhakti.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build('my-python-app1')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container based on the built image
                    docker.image('my-python-app1').run('-d', '-p', '5000:5000')
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up: Stop and remove the Docker container
                docker.image('my-python-app1').stop()
                docker.image('my-python-app1').remove()
            }
        }
    }
}
