timestamps {
     node ('master') {
        ansiColor('xterm') {
            try{
                stage('UP'){
                    checkout scm
                    sh "docker-compose up -d --build"
                }
                stage('RUN'){
                     sh "docker-compose run pythonservice pytest -v -n=4 --env=develop --url=https://maxipro-develop.dclouds.ru/ /tests/"
                     sh "docker-compose down"
                }
            }finally{  
                stage('DELETE') {
                    deleteDir()               
                }
            }
         }
     }
}