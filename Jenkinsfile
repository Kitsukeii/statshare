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
                sh 'echo -e "Create\n Test\n Pythontest\n 5\n Exit"|python3 statshare.py'
            }
        }
      stage('Test DB') {
            steps {
                sh 'echo -e "Read\n Exit"|python3 statshare.py'
            }
        }
    }

}
