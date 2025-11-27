pipeline {
    agent any

    environment {
        RUN_ENV = "jenkins"
        CI = "true"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ravirguru/auto_gui_project.git'
            }
        }

        stage('Create Video Folder') {
            steps {
                sh "mkdir -p videos"
            }
        }

        /* ===================== CHROME WITH VNC + VIDEO ===================== */

        stage('Start Chrome Selenium (VNC Enabled)') {
            steps {
                sh """
                    docker rm -f selenium-chrome chrome-video || true

                    docker run -d --name selenium-chrome \
                      -p 4444:4444 \
                      -p 5900:5900 \
                      selenium/standalone-chrome:latest
                """
                sh "sleep 5"
            }
        }

        stage('Start Chrome Video Recording') {
            steps {
                sh """
                    docker run -d --name chrome-video \
                      --link selenium-chrome \
                      -v ${WORKSPACE}/videos:/videos \
                      selenium/video
                """
            }
        }

        stage('Run Tests - Chrome') {
            steps {
                sh """
                    docker run --rm \
                      -e RUN_ENV=jenkins \
                      -e GRID_URL=http://host.docker.internal:4444/wd/hub \
                      -v /c/jenkins_home/workspace/python-selenium-pipeline:/project \
                      -w /project \
                      python:3.10 \
                      bash -c "ls -la && pip install -r requirements.txt && pytest -v --browser chrome --junitxml=reports/junit-chrome.xml"
                """
            }
        }

        stage('Stop Chrome Video') {
            steps {
                sh """
                    docker stop chrome-video || true
                    docker rm chrome-video || true
                """
            }
        }

        stage('Stop Chrome Selenium') {
            steps {
                sh "docker rm -f selenium-chrome || true"
            }
        }

        /* ===================== FIREFOX WITH VNC + VIDEO ===================== */

        stage('Start Firefox Selenium (VNC Enabled)') {
            steps {
                sh """
                    docker rm -f selenium-firefox firefox-video || true

                    docker run -d --name selenium-firefox \
                      -p 4445:4444 \
                      -p 5901:5900 \
                      selenium/standalone-firefox:latest
                """
                sh "sleep 5"
            }
        }

        stage('Start Firefox Video Recording') {
            steps {
                sh """
                    docker run -d --name firefox-video \
                      --link selenium-firefox \
                      -v ${WORKSPACE}/videos:/videos \
                      selenium/video
                """
            }
        }

        stage('Run Tests - Firefox') {
            steps {
                sh """
                   echo WORKSPACE = ${WORKSPACE}
                    ls -R ${WORKSPACE}

                    docker run --rm \
                        -e RUN_ENV=jenkins \
                        -e GRID_URL=http://host.docker.internal:4445/wd/hub \
                        -v /c/jenkins_home/workspace/python-selenium-pipeline:/project \
                        -w /project \
                        python:3.10 \
                        bash -c "pip install -r requirements.txt && pytest -v --browser firefox --junitxml=reports/junit-firefox.xml || true"
                    """
            }
        }

        stage('Stop Firefox Video') {
            steps {
                sh """
                    docker stop firefox-video || true
                    docker rm firefox-video || true
                """
            }
        }

        stage('Stop Firefox Selenium') {
            steps {
                sh "docker rm -f selenium-firefox || true"
            }
        }

        /* ===================== REPORTS ===================== */

        stage('List Videos') {
            steps {
                sh "ls -lh videos || true"
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
            archiveArtifacts artifacts: 'videos/*.mp4', fingerprint: true
        }
        cleanup {
            cleanWs()
        }
    }
}