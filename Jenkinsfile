pipeline {
    agent any // Or 'agent { label "docker" }' if you have specific agents

    environment {
        DOCKER_HOST = 'unix:///var/run/docker.sock'
        SONARQUBE_ENV = 'sonarserver'
        PROJECT_KEY   = 'go-project'
        PROJECT_NAME  = 'go-project'
        SCANNER_HOME  = tool 'sonqube'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'tugas-1',
                    url: 'https://github.com/azaregon/OPREC-CAMIN-NCC',
                    credentialsId: 'admin'
            }
        }

        stage('Setup & Build') {
            steps {
                // Use dir() to ensure all commands inside happen within that folder
                dir('file prod') {
                    sh '''
                        git config --global --add safe.directory ${WORKSPACE}
                        apt-get update -qq && apt-get install -y -qq default-jre-headless
                        
                        # Use -d to run in background so the pipeline can continue
                        docker compose up -d
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                // If you are running tests OUTSIDE the container, you need Go installed on the agent
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
            // Shut down the containers so they don't leak resources
            dir('file prod') {
                sh 'docker compose down'
            }
        }
        success { echo 'Pipeline sukses' }
        failure { echo 'Pipeline gagal' }
    }
}
