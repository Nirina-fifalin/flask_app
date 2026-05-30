pipeline {
    triggers {
        pollSCM('* * * * *')
    }
    agent {
        kubernetes {
            label 'jenkins-agent-flask'
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: ci
spec:
  serviceAccountName: jenkins
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
    image: alpine/k8s:1.27.16
    command: ["cat"]
    tty: true
    securityContext:
      runAsUser: 0
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
                        docker build -t 192.168.49.1:4000/pythontest:latest .
                        docker push 192.168.49.1:4000/pythontest:latest
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