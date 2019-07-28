pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sleep 10
        bat(script: 'echo "hello"', returnStatus: true, returnStdout: true)
      }
    }
  }
}