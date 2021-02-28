#!/bin/bash
cd ~/home/jenkins/.jenkins/workspace/Generator_Project_2
ansible-playbook -i inventory.yaml playbook.yaml 
