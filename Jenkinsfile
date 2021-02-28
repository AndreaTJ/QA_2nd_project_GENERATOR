pipeline {
    agent any
    stages {
        stage('Configure - Ansible'){
            steps{
                sh 'chmod +x ./scripts/configure_ansible.sh'
                sh './scripts/configure_ansible'
            }
        }                  
    }
}
