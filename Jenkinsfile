pipeline {
    agent any
    stages {
        
        stage('Build'){
            steps{
                sh 'docker-compose build'
               
            }
        } 
        stage('Configure - Ansible'){
            steps{
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
               
            }
        } 
        
        stage('Deploy'){
            steps{
                sh 'docker-compose push && docker stack deploy --compose-file docker-compose.yaml flaskapp'
               
            }
        } 
    }
}
