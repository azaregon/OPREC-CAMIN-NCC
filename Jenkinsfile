pipeline {
    agent any

    environment {
        // Change this to your SonarQube server name in Jenkins
        SONARQUBE_ENV = 'SonarQube'
    }

    stages {

        stage('Checkout') {
            steps {
                echo '=== STAGE: CHECKOUT ==='
                checkout scm
                echo 'Repository checked out successfully'
            }
        }

        stage('Preparation') {
            steps {
                echo '=== STAGE: PREPARATION ==='
                sh 'pwd'
                sh 'ls -la'
                echo 'Preparation done'
            }
        }

        stage('Build (Mock)') {
            steps {
                echo '=== STAGE: BUILD ==='
                echo 'Skipping actual build (debug mode)'
            }
        }

        stage('Test (Mock)') {
            steps {
                echo '=== STAGE: TEST ==='
                echo 'Skipping tests (debug mode)'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo '=== STAGE: SONARQUBE ANALYSIS ==='

                steps {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=debug-project \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=http://localhost:9000 \
                      -Dsonar.login=YOUR_TOKEN
                    '''
                }

                echo 'SonarQube analysis triggered'
            }
        }

        stage('Quality Gate') {
            steps {
                echo '=== STAGE: QUALITY GATE ==='

                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }

                echo 'Quality Gate check completed'
            }
        }
    }

    post {
        always {
            echo '=== PIPELINE FINISHED ==='
        }

        success {
            echo '=== STATUS: SUCCESS ✅ ==='
        }

        failure {
            echo '=== STATUS: FAILURE ❌ ==='
        }
    }
}
