pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }

        stage('Package') {
            steps {
                sh 'tar -czf jenkins-ci-project.tar.gz app.py test_app.py'
            }
        }
    }
}
