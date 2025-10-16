pipeline {
  agent {
    docker {
      image 'python:3.11-slim'
      args '-u root:root --network jenkins-network' // run container on the same network
    }
  }

  environment {
    SELENIUM_URL = 'http://selenium-standalone-chrome:4444/wd/hub'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Prepare venv & install deps') {
      steps {
        sh '''
          python -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          . .venv/bin/activate
          mkdir -p reports screenshots || true
          pytest tests \
            --maxfail=1 -q \
            --junitxml=reports/junit-results.xml \
            || true
        '''
      }
      post {
        always {
          archiveArtifacts artifacts: 'reports/**, screenshots/**', allowEmptyArchive: true
          junit 'reports/junit-results.xml'
        }
      }
    }
  }

  post {
    always {
      echo "Pipeline finished"
    }
  }
}
