# 🚀 Production DevOps FastAPI

<p align="center">

![AWS](https://img.shields.io/badge/AWS-EKS-orange?style=for-the-badge&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?style=for-the-badge&logo=terraform)
![Helm](https://img.shields.io/badge/Helm-Charts-0F1689?style=for-the-badge&logo=helm)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?style=for-the-badge&logo=grafana)
![FastAPI](https://img.shields.io/badge/FastAPI-Python-009688?style=for-the-badge&logo=fastapi)

</p>

---

# 📖 Project Overview

Production DevOps FastAPI is a production-style cloud-native deployment project demonstrating how a **FastAPI** application can be deployed on **Amazon EKS** using **Docker**, **Kubernetes**, **Helm**, and **Terraform**.

The application is exposed using the **AWS Load Balancer Controller** and monitored with **Prometheus** and **Grafana**. The project also demonstrates **Rolling Updates** and **Rollbacks**, following production-oriented DevOps practices.

---

# 🎯 Objectives

- Provision AWS Infrastructure using Terraform
- Deploy Amazon EKS Cluster
- Containerize FastAPI using Docker
- Deploy using Kubernetes & Helm
- Configure AWS Load Balancer Controller
- Monitor with Prometheus & Grafana
- Demonstrate Rolling Updates
- Demonstrate Kubernetes Rollback

---

# ✨ Features

- Infrastructure as Code (Terraform)
- Dockerized FastAPI Application
- Amazon EKS Deployment
- Kubernetes Deployment & Service
- Helm Chart Deployment
- AWS Load Balancer Controller
- Prometheus Monitoring
- Grafana Dashboards
- Rolling Updates
- Rollbacks
- High Availability (2 Replicas)

---

# 🛠 Tech Stack

| Layer | Technology |
|---------|------------|
| Language | Python 3.11 |
| Framework | FastAPI |
| Containerization | Docker |
| Registry | Docker Hub |
| Infrastructure | Terraform |
| Cloud | AWS |
| Orchestration | Amazon EKS |
| Kubernetes | Kubernetes |
| Package Manager | Helm |
| Load Balancer | AWS Load Balancer Controller |
| Monitoring | Prometheus |
| Dashboard | Grafana |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
production-devops-fastapi/
│
├── app/
│   └── main.py
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── eks.tf
│   ├── outputs.tf
│   └── terraform.tfvars
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── helm/
│   └── fastapi-app/
│
├── screenshots/
│
├── architecture/
│   └── architecture-diagram.png
│
├── Dockerfile
├── Dockerfile.jenkins
├── Jenkinsfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
└── .dockerignore
```

---

# 🏗 Architecture Diagram

> Add your architecture diagram here.

```text
architecture/architecture-diagram.png
```

```md
![Architecture](architecture/architecture-diagram.png)
```

---

# 🚀 Deployment Workflow

```text
Developer
     │
     ▼
FastAPI Application
     │
     ▼
Docker Build
     │
     ▼
Docker Hub
     │
     ▼
Terraform
     │
     ▼
Amazon EKS
     │
     ▼
Helm Deployment
     │
     ▼
Kubernetes
     │
     ▼
AWS Load Balancer Controller
     │
     ▼
Application Load Balancer
     │
     ▼
Users

             │
             ▼

 Prometheus ─────────► Grafana
```

---

# 📸 Project Screenshots

## ☁ Amazon EKS Cluster

![](screenshots/02-eks-cluster-created.png)

---

## ☸ Kubernetes Worker Nodes

![](screenshots/03-worker-nodes.png)

---

## 🖥 Kubernetes Nodes

![](screenshots/04-kubectl-get-nodes.png)

---

## 📦 Kubernetes Pods

![](screenshots/05-kubectl-get-pods.png)

---

## 🚀 Kubernetes Deployment

![](screenshots/06-kubernetes-deployment.png)

---

## 🌐 Kubernetes Service

![](screenshots/07-kubernetes-service.png)

---

## ⚙ Helm Deployment

![](screenshots/08-helm-deployment.png)

---

## ⚖ AWS Load Balancer Controller

![](screenshots/09-aws-load-balancer-controller.png)

---

## 🌍 AWS Application Load Balancer

![](screenshots/10-aws-load-balancer.png)

---

## ⚡ FastAPI Application

![](screenshots/11-fastapi-application.png)

---

## 📊 Prometheus Dashboard

![](screenshots/12-prometheus-dashboard.png)

---

## 📈 Grafana Dashboard

![](screenshots/13-grafana-dashboard.png)

---

## 🔄 Rolling Update

![](screenshots/14-rolling-update.png)

---

## 📜 Rollout History

![](screenshots/15-rollout-history.png)

---

## ⏪ Rollback

![](screenshots/16-rollback.png)

---

## ✅ Final Application Running

![](screenshots/17-final-fastapi-running.png)

# 🔄 Rolling Update

The application was upgraded from **v1** to **v2** using Kubernetes Rolling Updates.

### Benefits

- Zero Downtime Deployment
- High Availability
- Automatic Pod Replacement
- Safe Production Release

---

# ⏪ Rollback

A Kubernetes Rollback was performed to restore the previous stable application version.

### Benefits

- Quick Recovery
- Production Safety
- Reduced Downtime

---

# 📊 Monitoring

The Kubernetes cluster is monitored using **Prometheus** and **Grafana**.

### Metrics Collected

- CPU Usage
- Memory Usage
- Node Health
- Pod Health
- Cluster Resources
- Kubernetes Events

---

# 🚀 Future Improvements

- GitHub Actions CI/CD
- Amazon ECR
- Horizontal Pod Autoscaler (HPA)
- Cluster Autoscaler
- ArgoCD GitOps
- Route53 Domain
- HTTPS using AWS ACM
- Loki Logging
- Jaeger Tracing
- AWS Secrets Manager

---

# 👨‍💻 Author

## Shivraj Amale

Cloud & DevOps Engineer

### Skills

- AWS
- Docker
- Kubernetes
- Terraform
- Helm
- FastAPI
- Prometheus
- Grafana

### Connect

- GitHub: https://github.com/shivrajamale
- LinkedIn: https://www.linkedin.com/in/shivrajamale/

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
