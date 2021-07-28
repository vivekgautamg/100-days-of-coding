pipeline {
  agent any
  stages {
    stage("build") {
      steps {
        echo "build the application"
        bat python -m py-compile demo_jenkins.py
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
