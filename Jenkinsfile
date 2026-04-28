pipeline {
    agent any

    tools {
        // MUST match exactly what you named in Jenkins
        sonarScanner 'sonqube'
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

        stage('Build (Mock)') {
            steps {
                echo '=== STAGE: BUILD ==='
                echo 'Skipping build...'
            }
        }

        stage('Test (Mock)') {
            steps {
                echo '=== STAGE: TEST ==='
                echo 'Skipping test...'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo '=== STAGE: SONARQUBE ANALYSIS ==='

                withSonarQubeEnv('sonqube') {
                    sh '''
                        echo "Using scanner:"
                        which sonar-scanner

                        echo "Starting scan..."
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

        success {
            echo '=== STATUS: SUCCESS ✅ ==='
        }

        failure {
            echo '=== STATUS: FAILURE ❌ ==='
        }
    }
}
