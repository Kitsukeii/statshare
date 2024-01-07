pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
      stage('Create DB') {
            steps {
                sh 'echo -e "Create\nTest\nPythontest\n5\nExit"|python3 statshare.py'
            }
        }
      stage('Test DB') {
            steps {
                sh 'echo -e "Read\nExit"|python3 statshare.py'
            }
        }
    }

}
