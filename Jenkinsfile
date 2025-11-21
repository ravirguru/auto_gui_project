pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root'  // runs container commands as root
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ravirguru/auto_gui_project.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest -v --junitxml=reports/junit-report.xml'
            }
        }

        stage('List Files') {
            steps {
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
