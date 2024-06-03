pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git url: 'https://github.com/deepak7376/robustbase.git', branch: 'master'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh '''
                # Create a virtual environment
                python3 -m venv venv

                # Activate virtual environment
                source venv/bin/activate

                # Install dependencies
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh '''
                # Activate virtual environment
                source venv/bin/activate

                # Run pytest
                pytest tests/
                '''
            }
        }

        stage('Cleanup') {
            steps {
                // Clean up the workspace
                cleanWs()
            }
        }
    }

    post {
        always {
            // Clean up the virtual environment if it exists
            sh 'rm -rf venv'
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
