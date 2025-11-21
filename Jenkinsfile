pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ravirguru/auto_gui_project.git'
            }
        }

        stage('Run Tests - Chrome') {
            steps {
                sh '''
                    docker run --rm \
                        -v $WORKSPACE:/project \
                        -w /project \
                        selenium/standalone-chrome:latest \
                        bash -c "pip install -r requirements.txt && pytest -v --junitxml=reports/junit-chrome.xml || true"
                '''
            }
        }

        stage('Run Tests - Firefox') {
            steps {
                sh '''
                    docker run --rm \
                        -v $WORKSPACE:/project \
                        -w /project \
                        selenium/standalone-firefox:latest \
                        bash -c "pip install -r requirements.txt && pytest -v --junitxml=reports/junit-firefox.xml || true"
                '''
            }
        }

        stage('List Reports') {
            steps {
                sh 'ls -R reports'
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
        }
    }
}
