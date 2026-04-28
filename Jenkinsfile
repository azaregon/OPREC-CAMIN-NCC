pipeline {
    agent any

    tools {
        sonarRunner 'sonqube'
    }

    stages {

        stage('Checkout') {
            steps {
                echo '=== STAGE: CHECKOUT ==='
                checkout scm
            }
        }

        stage('Preparation') {
            steps {
                echo '=== STAGE: PREPARATION ==='
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo '=== STAGE: SONARQUBE ANALYSIS ==='

                withSonarQubeEnv('sonqube') {
                    sh '''
                        echo "Checking scanner..."
                        which sonar-scanner || echo "NOT FOUND"

                        sonar-scanner \
                          -Dsonar.projectKey=debug-project \
                          -Dsonar.sources=. \
                          -X
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo '=== STAGE: QUALITY GATE ==='

                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: false
                }
            }
        }
    }

    post {
        always {
            echo '=== PIPELINE FINISHED ==='
        }
    }
}
