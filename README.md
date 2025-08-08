# FanPulse – Real-time Game Score Service

A simple sports score API deployed on Kubernetes with Helm, monitored via Prometheus + Grafana + Loki.

## Features
- Python Flask app simulating real-time scores
- Dockerized for portability
- Kubernetes deployment with Helm
- GitHub Actions CI/CD pipeline
- Observability with Prometheus, Grafana, Loki
- Horizontal scaling with HPA

## Quick Start Guide

1. Start Minikube:

    minikube start

2. Build & Deploy locally:

    docker build -t fanpulse:latest ./app
    helm upgrade --install fanpulse ./charts/fanpulse

3. Access service:

    minikube service fanpulse