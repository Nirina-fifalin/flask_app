pipeline {
    triggers {
        pollSCM('* * * * *')
    }
    agent {
        kubernetes {
            label 'jenkins-agent-my-app'
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: ci
spec:
  containers:
  - name: python
    image: python:3.9
    command: ["cat"]
    tty: true
  - name: docker
    image: docker:latest
    command: ["cat"]
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  - name: kubectl
    image: bitnami/kubectl:latest
    command: ["cat"]
    tty: true
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }
    stages {
        stage('Test python') {
            steps {
                container('python') {
                    sh '''
                        pip install -r requirements.txt
                        python test.py --verbose
                    '''
                }
            }
        }
        stage('Build image') {
            steps {
                container('docker') {
                    sh '''
                        docker build -t host.minikube.internal:4000/pythontest:latest .
                        docker push host.minikube.internal:4000/pythontest:latest
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                container('kubectl') {
                    sh '''
                        kubectl apply -f ./kubernetes/deployment.yaml
                        kubectl apply -f ./kubernetes/service.yaml
                    '''
                }
            }
        }
    }
}