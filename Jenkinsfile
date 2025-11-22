pipeline {
    agent any

    environment {
        RUN_ENV = "jenkins"
        CI = "true"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ravirguru/auto_gui_project.git'
            }
        }

        /* ---------------- Chrome ---------------- */
        stage('Start Chrome Selenium') {
            steps {
                sh """
                    docker rm -f selenium-chrome || true
                    docker run -d --name selenium-chrome -p 4444:4444 selenium/standalone-chrome:latest
                """
                sh "sleep 5"
            }
        }

        stage('Run Tests - Chrome') {
            steps {
                sh """
                    echo WORKSPACE = ${WORKSPACE}

                    docker run --rm \
                        -e RUN_ENV=jenkins \
                        -e GRID_URL=http://host.docker.internal:4444/wd/hub \
                        -v ${WORKSPACE}:/project \
                        -w /project \
                        python:3.10 \
                        bash -c "pip install -r requirements.txt && pytest -v --browser chrome --junitxml=reports/junit-chrome.xml || true"
                """
            }
        }

        stage('Stop Chrome') {
            steps { sh "docker rm -f selenium-chrome || true" }
        }


        /* ---------------- Firefox ---------------- */
        stage('Start Firefox Selenium') {
            steps {
                sh """
                    docker rm -f selenium-firefox || true
                    docker run -d --name selenium-firefox -p 4445:4444 selenium/standalone-firefox:latest
                """
                sh "sleep 5"
            }
        }

        stage('Run Tests - Firefox') {
            steps {
                sh """
                    echo WORKSPACE = ${WORKSPACE}

                    docker run --rm \
                        -e RUN_ENV=jenkins \
                        -e GRID_URL=http://host.docker.internal:4445/wd/hub \
                        -v ${WORKSPACE}:/project \
                        -w /project \
                        python:3.10 \
                        bash -c "pip install -r requirements.txt && pytest -v --browser firefox --junitxml=reports/junit-firefox.xml || true"
                """
            }
        }

        stage('Stop Firefox') {
            steps { sh "docker rm -f selenium-firefox || true" }
        }

        stage('List Reports') {
            steps { sh "ls -R reports" }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
        }
    }
}
