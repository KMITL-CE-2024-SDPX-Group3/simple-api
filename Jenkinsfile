pipeline{
    agent any

    environment{
        APP_NAME = "Simple API - SDPX G3"
        IMAGE_NAME = "ghcr.io/kmitl-ce-2024-sdpx-group3/simple-api-image:lastest"

    }
    stages{
        stage("Build Image"){
            steps{
                sh "echo BUILDING"
                sh "echo ${env.APP_NAME}"
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}