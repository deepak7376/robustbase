pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "robustbase_img"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git url: 'https://github.com/deepak7376/robustbase.git', branch: 'master'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Create Dockerfile dynamically
                    writeFile file: 'Dockerfile', text: '''
                    FROM python:3.8-slim

                    WORKDIR /app

                    # Copy requirements file
                    COPY requirements.txt .

                    # Install dependencies
                    RUN pip install --no-cache-dir -r requirements.txt

                    # Copy requirements-dev file
                    COPY requirements-dev.txt .

                    # Install dev dependencies
                    RUN pip install --no-cache-dir -r requirements-dev.txt

                    # Copy the rest of the application
                    COPY . .

                    # Command to run tests
                    CMD ["pytest", "tests/"]
                    '''

                    // Build Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run Docker container and execute pytest
                sh 'docker run --rm ${DOCKER_IMAGE}'
            }
        }

        stage('Cleanup') {
            steps {
                // Remove Docker image
                sh 'docker rmi ${DOCKER_IMAGE}'
            }
        }
    }

    post {
        always {
            // Clean up workspace after build
            cleanWs()
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
