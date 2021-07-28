pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        echo "build the application"
        powershell 'python --version'
      }
    }
   stage("test") {
      steps {
        echo "test the application"
      }
    }
   stage("deploy") {
      steps {
        echo "deploy the application"
      }
    }
  }
}
