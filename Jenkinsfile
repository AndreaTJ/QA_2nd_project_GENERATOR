pipeline {
    agent any
    environment {
        DOCKERHUB_LOGIN = credentials("docker-hub-credentials")
    }
    stages {
        stage('Configure - Ansible'){
            steps{
                sh 'chmod +x ./scripts/configure_ansible.sh'
                sh './scripts/test.sh'
            }
        }                  
    }
}