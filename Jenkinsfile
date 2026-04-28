pipeline {
    agent {
    }

    environment {
        SONARQUBE_ENV = 'sonarserver'
        PROJECT_KEY   = 'go-project'
        PROJECT_NAME  = 'go-project'
        SCANNER_HOME  = tool 'sonarqube8.0'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'tugas-1',
                    url: 'https://github.com/azaregon/OPREC-CAMIN-NCC',
                    credentialsId: 'admin'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                    git config --global --add safe.directory ${WORKSPACE}
                    apt-get update -qq
                    apt-get install -y -qq default-jre-headless
                    cd 'file prod'
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose up'
            }
        }

        stage('Test') {
            steps {
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
                timeout(time: 20, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline sukses'
        }
        failure {
            echo 'Pipeline gagal'
        }
    }
}
