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
                sh '''
                #!/bin/bash
                echo -e "Create\nTest\nPythontest\n5\nExit"|python3 statshare.py
                '''
            }
        }
      stage('Test DB') {
            steps {
                sh '''
                #!/bin/bash
                echo -e "Read\nExit"|python3 statshare.py
                '''
            }
        }
    }

}
