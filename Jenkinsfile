pipeline {
    agent any

    environment {
        // Must match your SonarQube server name in Jenkins
        SONARQUBE_ENV = 'SonarQube'
    }

    tools {
        sonarRunner 'sonqube'
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
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
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
