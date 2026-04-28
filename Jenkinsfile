pipeline {
    agent any

    environment {
        IMAGE_NAME = "python:3.13.3-slim"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Docker') {
            steps {
                sh 'docker version'
            }
        }

        stage('Run Python in Docker') {
            steps {
                script {
                    docker.image(env.IMAGE_NAME).inside {
                        sh '''
                            python --version
                            echo "Container is working"
                        '''
                    }
                }
            }
        }

        stage('Run Your App') {
            steps {
                script {
                    docker.image(env.IMAGE_NAME).inside {
                        sh '''
                            if [ -f requirements.txt ]; then
                                pip install -r requirements.txt
                            fi

                            if [ -f main.py ]; then
                                python main.py
                            else
                                echo "No main.py found, skipping..."
                            fi
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished (success or failure)'
        }

        success {
            echo 'Pipeline succeeded ✅'
        }

        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
