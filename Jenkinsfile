pipeline{
    agent any

    environment{
        APP_NAME = "Simple API - SDPX G3"
        IMAGE_NAME = "ghcr.io/kmitl-ce-2024-sdpx-group3/simple-api-image:lastest"

    }
    stages{
        stage('Activate Existing Python Environment') {
            steps {
                script {
                    // Activate the existing virtual environment
                    sh '''
                    . ~/test-env/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage("Run Unit Test"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "python3 -m unittest tests/test_plus.py"
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
                sh "git clone https://github.com/KMITL-CE-2024-SDPX-Group3/simple-api-robot"
            }
        }

        stage("Run Robot Test"){
            agent {
                label "VM-Test"
            }
            steps {
                sh "robot test-plus.robot"
            }
        }

        stage("Push Docker Image") {
            agent {
                label "VM-Test"
            }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "Sun-GitHub-Token",
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
                        credentialsId: "Sun-GitHub-Token",
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
}