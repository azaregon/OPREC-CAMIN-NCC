pipeline {
    agent {
        docker {
            image 'python:3.13.3-slim'
            // We mount the Docker binary and the Socket so Python can run docker commands
            args '''-u root \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v /usr/bin/docker:/usr/bin/docker \
                    -v /usr/libexec/docker/cli-plugins/docker-compose:/usr/libexec/docker/cli-plugins/docker-compose'''
        }
    }

    environment {
        DOCKER_HOST   = 'unix:///var/run/docker.sock'
        SONARQUBE_ENV = 'sonarserver'
        PROJECT_KEY   = 'go-project'
        PROJECT_NAME  = 'go-project'
        SCANNER_HOME  = tool 'sonarqube8.0'
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    # Install JRE for Sonar and Go for the tests
                    apt-get update -qq
                    apt-get install -y -qq default-jre-headless golang-go
                    
                    git config --global --add safe.directory ${WORKSPACE}
                '''
            }
        }

        stage('Build') {
            steps {
                dir('file prod') {
                    // This will now work because we mounted the docker binary/socket
                    sh 'docker compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                // This works because we installed golang-go in the Setup stage
                sh 'go test ./... -v -coverprofile=coverage.out'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=${PROJECT_KEY} -Dsonar.sources=."
                }
            }
        }
    }

    post {
        always {
            dir('file prod') { sh 'docker compose down' }
        }
    }
}
