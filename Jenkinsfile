pipeline {
    agent any
    stages {
        stage('Configure - Ansible'){
            steps{
                sh 'chmod +x ./scripts/configure_ansible.sh'
                sh "pwd"
                sh "ls -la"
                sh './scripts/configure_ansible'
                
            }
        }                  
    }
}
