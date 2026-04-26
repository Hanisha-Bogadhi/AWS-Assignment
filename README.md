# AWS Deployment Assignment

## Overview
This project demonstrates deployment of a Flask backend and Express frontend using multiple AWS architectures.

---

## Task 1: Single EC2 Deployment
- Flask backend + Express frontend on one EC2 instance
- Different ports for each service
- Simple and cost-effective setup

---

## Task 2: Separate EC2 Deployment
- Backend and frontend deployed on different EC2 instances
- Communication via API endpoints
- Improved scalability and isolation

---

## Task 3: Docker + AWS ECS + ECR + VPC
- Applications containerized using Docker
- Docker images stored in Amazon ECR
- Deployment managed using ECS
- Networking handled via VPC configuration

---

## Cost Optimization
- Stop EC2 instances when not in use
- teminated EC2 for task 1 and task 2 after deploy
- Stop ECS services when not required
- Use AWS Free Tier whenever possible

---

## Repository
GitHub: <https://github.com/Hanisha-Bogadhi/AWS-Assignment.git>

---

## Deployment URLs
- Task 1: 
    - http://98.130.134.166:3000

	- http://98.130.134.166:5000 
    
- Task 2: 
    - http://18.61.48.94:3000 

	- http://98.130.142.230:5000

- Task 3:
   - http://16.112.78.254:3000 

   - http://16.112.78.254:5000 

 
