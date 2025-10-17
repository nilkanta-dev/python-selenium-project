pipeline {
    agent {
        docker {
            image 'python:3.12-slim'   // You can change to another Python version if needed
            args '--network jenkins-network'
        }
    }

    environment {
        SELENIUM_URL = 'http://selenium-standalone-chrome:4444/wd/hub'
        VENV = ".venv"  // inside workspace, writable now that permissions are correct
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Python Environment') {
            steps {
                sh '''
                    python -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    mkdir -p reports screenshots || true
                    pytest tests \
                        --maxfail=1 -v \
                        --junitxml=reports/junit-results.xml \
                        || true
                '''
            }
            post {
                always {
                    echo "Archiving reports and screenshots..."
                    archiveArtifacts artifacts: 'reports/**, screenshots/**', allowEmptyArchive: true
                    junit 'reports/junit-results.xml'
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
    }
}
