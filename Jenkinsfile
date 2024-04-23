pipeline {
    agent any

    stages {
         stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/devarajareddy92/Bhakti.git']]])
            }
        }
        

        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    docker.build('my-python-app')
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                // Run the Docker container based on the built image
                script {
                    docker.image('my-python-app').run('-d', '-p', '5000:5000', 'my-python-app')
                }
            }
        }

       
    }

    post {
        always {
            // Clean up: Stop and remove the Docker container
            script {
                docker.image('my-python-app').stop()
                docker.image('my-python-app').remove()
            }
        }
    }
}