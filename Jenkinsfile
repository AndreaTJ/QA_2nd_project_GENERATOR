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
                sh 'scp docker-compose.yaml jenkins@35.188.151.251:docker-compose.yaml && docker-compose push'
                sh "ssh 35.188.151.251 && docker stack deploy --compose-file docker-compose.yaml flaskapp"
               
            }
        } 
    }
}
