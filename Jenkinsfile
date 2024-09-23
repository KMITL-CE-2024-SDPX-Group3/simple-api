pipeline{
    agent any

    environment{
        APP_NAME = "Simple API - SDPX G3"
        IMAGE_NAME = "ghcr.io/kmitl-ce-2024-sdpx-group3/simple-api-image:lastest"
        VENV_NAME = 'myenv'

    }
    stages{
        stage("Setup Python Environment"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "python3 -m venv ${VENV_NAME}"
                sh ". ${VENV_NAME}/bin/activate"
            }
        }

        stage("Install Python Dependencies"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "${VENV_NAME}/bin/pip install -r requirements.txt"
            }
        }

        stage("Run Unit Test"){
            agent {
                label "VM-Test"
            }
            steps {
                sh ". ${VENV_NAME}/bin/activate && python3 -m unittest tests/test_plus.py"
            }
        }

        stage("Build Docker Image"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "docker compose build"
                sh "docker ps"
            }
        }

        stage("Run Docker Container"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "docker compose up -d"
            }
        }

        stage("Clone simple-api-robot repository"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "rm -rf simple-api-robot"
                sh "git clone https://github.com/KMITL-CE-2024-SDPX-Group3/simple-api-robot"
            }
        }

        stage("Run Robot Test"){
            agent {
                label "VM-Test"
            }
            steps {
                sh ". ${VENV_NAME}/bin/activate && robot test-plus.robot"
            }
        }

        stage("Push Docker Image") {
            agent {
                label "VM-Test"
            }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "Sun-GitHub-Package",
                        passwordVariable: "GITHUB_PASSWORD",
                        usernameVariable: "GITHUB_USERNAME"
                    )]
                ){
                    sh "docker login ghcr.io -u ${GITHUB_USERNAME} -p ${GITHUB_PASSWORD}"
                    sh "docker push ghcr.io/kmitl-ce-2024-sdpx-group3/simple-api-image"
                    sh "docker rmi -f ghcr.io/kmitl-ce-2024-sdpx-group3/simple-api-image:lastest"
                }
            }
        }

        stage("Stop Docker Container"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "docker compose down"
            }
        }

        stage("PreProd - Pull Image"){
            agent {
                label "VM-PreProd"
            }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "Sun-GitHub-Package",
                        passwordVariable: "GITHUB_PASSWORD",
                        usernameVariable: "GITHUB_USERNAME"
                    )]
                ){
                    sh "docker login ghcr.io -u ${GITHUB_USERNAME} -p ${GITHUB_PASSWORD}"
                    sh "docker pull ghcr.io/kmitl-ce-2024-sdpx-group3/simple-api-image"
                }
            }
        }

        stage("PreProd - Run Container from Image"){
            agent {
                label "VM-PreProd"
            }
            steps {
                sh "docker compose up -d"
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment
            sh "rm -rf ${VENV_NAME}"
        }
    }
}