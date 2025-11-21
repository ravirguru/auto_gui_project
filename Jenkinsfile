pipeline {
    agent any

    stages {
        stage('Pull Python Image') {
            steps {
                sh 'docker pull python:3.10'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh '''
                    mkdir -p reports

                    docker run --rm \
                    -v $WORKSPACE:/project \
                    -w /project \
                    python:3.10 \
                    bash -c "pip install -r requirements.txt && pytest -v --junitxml=reports/junit-report.xml || true"
                '''
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
