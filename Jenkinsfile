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
                bash 'echo -e "Create\nTest\nPythontest\n5\nExit"|python3 statshare.py'
            }
        }
      stage('Test DB') {
            steps {
                bash 'echo -e "Read\nExit"|python3 statshare.py'
            }
        }
    }

}
