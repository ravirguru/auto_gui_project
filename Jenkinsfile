pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                sh '''
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-pip
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ravirguru/auto_gui_project.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v --junitxml=reports/junit-report.xml || true'
                sh 'ls -R .'
            }
        }
    }

    post {
        always {
            junit 'reports/junit-report.xml'
        }
    }
}
