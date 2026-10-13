```groovy
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        APP_NAME = 'hello-python-nti'
        CONTAINER_PORT = '5000'
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Configure Branch') {
            steps {
                script {
                    def branch = env.BRANCH_NAME

                    // Automatically calculate a host port from the branch name
                    def portOffset = Math.floorMod(branch.hashCode(), 1000)
                    env.HOST_PORT = "${10000 + portOffset}"

                    echo "Branch: ${branch}"
                    echo "Automatically allocated host port: ${env.HOST_PORT}"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    set -eu

                    docker build \
                        -t "$APP_NAME-$BRANCH_NAME:$BUILD_NUMBER" .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        set -eu

                        echo "$DOCKER_PASSWORD" |
                            docker login \
                                -u "$DOCKER_USERNAME" \
                                --password-stdin

                        docker tag \
                            "$APP_NAME-$BRANCH_NAME:$BUILD_NUMBER" \
                            "$DOCKER_USERNAME/$APP_NAME:$BRANCH_NAME-$BUILD_NUMBER"

                        docker push \
                            "$DOCKER_USERNAME/$APP_NAME:$BRANCH_NAME-$BUILD_NUMBER"

                        docker logout
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    set -eu

                    docker rm -f "$APP_NAME-$BRANCH_NAME" \
                        2>/dev/null || true

                    docker run -d \
                        --name "$APP_NAME-$BRANCH_NAME" \
                        --restart unless-stopped \
                        -p "$HOST_PORT:$CONTAINER_PORT" \
                        "$APP_NAME-$BRANCH_NAME:$BUILD_NUMBER"

                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'Python multibranch pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
```
