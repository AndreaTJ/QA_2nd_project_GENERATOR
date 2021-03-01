pipeline {
    agent any
    stages {
       
        stage('Test'){
            steps{
                
                dir("service1") {
                        sh "pytest --cov=app --cov-report term-missing"
                }
                
                /*
                dir("service2") {
                        sh "python3 -m pytest --cov=app"
                }
                 dir("service3") {
                        sh "python3 -m pytest --cov=app"
                }
                 dir("service4") {
                        sh "python3 -m pytest --cov=app"
                }
            }
        }*/
        

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
                sh "ssh 35.188.151.251 docker stack deploy --compose-file docker-compose.yaml flaskapp"
               
            }
        } 
    }
}

               
         
