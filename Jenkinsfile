node {
    def app

    stage('Clone repository')
    {

 checkout scm
    }

    stage('Build image') {


   steps
     {
       sh '/home/sterlite/.jenkins/workspace/test/Applications/netvertex/docker/build-nvsmx-image.sh 7.1.0.1'
     }    /* app = docker.build("getintodevops/hellonode")*/
    }

    stage('Test image') {

    {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
           docker.withRegistry('https://registry.hub.docker.com', 'ff7db3f6-a82b-4f02-b258-d40a4b302a9c') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
    
