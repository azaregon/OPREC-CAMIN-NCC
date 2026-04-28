pipeline {
    agent {
        docker {
            image 'python:3.13.3-slim'
            // CRITICAL: Mounts the socket and tells the agent to use it locally
            args '''-u root \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    -v /usr/bin/docker:/usr/bin/docker \
                    -v /usr/libexec/docker/cli-plugins/docker-compose:/usr/libexec/docker/cli-plugins/docker-compose \
                    -e DOCKER_HOST=unix:///var/run/docker.sock'''
        }
    }

    environment {
        SONARQUBE_ENV = 'sonarserver'
        PROJECT_KEY   = 'go-project'
        PROJECT_NAME  = 'go-project'
        // Ensure this name matches Manage Jenkins > Tools
        SCANNER_HOME  = tool 'sonarqube8.0'
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    # Install JRE for Sonar and Go for testing (slim images are empty)
                    apt-get update -qq && apt-get install -y -qq default-jre-headless golang-go
                    
                    git config --global --add safe.directory ${WORKSPACE}
                '''
            }
        }

        stage('Build') {
            steps {
                // dir() ensures we stay in 'file prod' for the whole block
                dir('file prod') {
                    // -d prevents the pipeline from hanging/blocking
                    sh 'docker compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                // Runs the Go tests and generates the coverage file for Sonar
                sh 'go test ./... -v -coverprofile=coverage.out'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE_ENV}") {
                    sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=${PROJECT_KEY} \
                          -Dsonar.projectName=${PROJECT_NAME} \
                          -Dsonar.sources=. \
                          -Dsonar.go.coverage.reportPaths=coverage.out
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            // Cleanup containers to free up RAM on your Surabaya server
            dir('file prod') {
                sh 'docker compose down'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output above.'
        }
    }
}
