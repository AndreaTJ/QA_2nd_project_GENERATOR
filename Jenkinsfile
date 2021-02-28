pipeline {
    agent any
    stages {
        stage('Configure - Ansible'){
            steps{
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
               
            }
        }                  
    }
}
