pipeline {
    agent any

    environment {
        RUN_ENV = "jenkins"
        CI = "true"
        //GRID_URL = http://selenium-hub:4444/wd/hub" works for shared Docker network.
        GRID_URL = "http://host.docker.internal:4444/wd/hub"

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

        /* ===================== START SELENIUM GRID ===================== */

        stage('Start Selenium Hub & Nodes (Parallel Grid + noVNC)') {
            steps {
                sh """
                docker rm -f selenium-hub || true
                docker rm -f chrome-node-1 chrome-node-2 chrome-node-3 chrome-node-4 || true
                docker rm -f firefox-node-1 firefox-node-2 || true

                echo "Starting Selenium Hub..."
                docker run -d --name selenium-hub \
                -p 4444:4444 \
                -p 4442:4442 \
                -p 4443:4443 \
                selenium/hub:latest

                sleep 10

                echo "Starting 4 Chrome Nodes..."
                for i in 1 2 3 4; do
                docker run -d --name chrome-node-\$i \
                  --link selenium-hub:hub \
                  -e SE_EVENT_BUS_HOST=selenium-hub \
                  -e SE_EVENT_BUS_PUBLISH_PORT=4442 \
                  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 \
                  -e SE_NODE_MAX_SESSIONS=1 \
                  -p \$((7900 + i)):7900 \
                  selenium/node-chrome:latest
                done

                echo "Starting 2 Firefox Nodes..."
                for i in 1 2; do
                docker run -d --name firefox-node-\$i \
                  --link selenium-hub:hub \
                  -e SE_EVENT_BUS_HOST=selenium-hub \
                  -e SE_EVENT_BUS_PUBLISH_PORT=4442 \
                  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 \
                  -e SE_NODE_MAX_SESSIONS=1 \
                  -p \$((7910 + i)):7900 \
                  selenium/node-firefox:latest
                done
                """
            }
        }

        /* ===================== START VIDEO RECORDING ===================== */

        stage('Start Chrome + Firefox Video Recording') {
            steps {
                sh """
                docker run -d --name chrome-video \
                  --link chrome-node-1 \
                  -v ${WORKSPACE}/videos:/videos \
                  selenium/video

                docker run -d --name firefox-video \
                  --link firefox-node-1 \
                  -v ${WORKSPACE}/videos:/videos \
                  selenium/video
                """
            }
        }

        /* ===================== RUN TESTS (PARALLEL) ===================== */

        stage('Run Tests - Chrome (Parallel)') {
            steps {
                sh """
                docker run --rm \
                  -e RUN_ENV=jenkins \
                  -e GRID_URL=${GRID_URL} \
                  -v /c/jenkins_home/workspace/python-selenium-pipeline:/project \
                  -w /project \
                  python:3.10 \
                  bash -c "pip install -r requirements.txt && pytest -v -n auto --browser chrome --junitxml=reports/junit-chrome.xml"
                """
            }
        }

        stage('Run Tests - Firefox (Parallel)') {
            steps {
                sh """
                docker run --rm \
                  -e RUN_ENV=jenkins \
                  -e GRID_URL=${GRID_URL} \
                  -v /c/jenkins_home/workspace/python-selenium-pipeline:/project \
                  -w /project \
                  python:3.10 \
                  bash -c "pip install -r requirements.txt && pytest -v -n auto --browser firefox --junitxml=reports/junit-firefox.xml"
                """
            }
        }

        /* ===================== STOP VIDEOS ===================== */

        stage('Stop Videos') {
            steps {
                sh """
                docker stop chrome-video firefox-video || true
                docker rm chrome-video firefox-video || true
                """
            }
        }

        /* ===================== STOP GRID ===================== */

        stage('Stop Selenium Grid') {
            steps {
                sh """
                docker rm -f selenium-hub chrome-node-1 chrome-node-2 firefox-node-1 firefox-node-2 || true
                """
            }
        }

        stage('List Videos') {
            steps {
                sh "ls -lh videos || true"
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
            archiveArtifacts artifacts: 'videos/*.mp4', allowEmptyArchive: true, fingerprint: true
        }
        cleanup {
            cleanWs()
        }
    }
}
