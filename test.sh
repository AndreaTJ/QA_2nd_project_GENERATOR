#!/bin/bash
pwd

cd ./service1/testing
pip3 install -r requirements.txt
pwd
pytest --cov app 
cd ..

cd ./service2
pytest --cov app
cd ..

cd ./service3
pytest --cov app
cd ..

cd ./service4
pytest --cov app
cd ..
