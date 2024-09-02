pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        SLACK_CHANNEL = 'D07KN8GSNJY'
    }

    stages {

        // Clona o repositório onde estão o código da aplicação e o arquivo docker-compose.yml
        stage('Checkout') {
            steps {
                // git url: 'https://github.com/Auggustto/DesafioTecnicoBackend.git'
                checkout([$class: 'GitSCM', branches:[[name: '*/main']], uerRemoteConfigs: [[url: 'https://github.com/Auggustto/DesafioTecnicoBackend.git']]])
            }
        }

        // Validando os arquivos clonados
        stage('Validate') {
            steps {
                script {
                    sh 'ls -la'
                }
            }
        }

        // Construindo as imagens e subindo os containers
        stage('Build and Start Containers') {
            steps {
                script {
                    sh 'docker-compose -f $DOCKER_COMPOSE_FILE up --build -d'
                }
            }
        }

        // Executa os testes dentro do container
        // stage('Run tests') {
        //     steps {
        //         sh 'docker-compose -f $DOCKER_COMPOSE_FILE run test'
        //     }
        // }

        // Derruba os containers e limpa os recursos
        stage('Stop and Clean Up') {
            steps {
                sh 'docker-compose -f $DOCKER_COMPOSE_FILE down --volumes --remove-orphans'
            }
        }
    }
    
    // Garante que os containers serão derrubados mesmo em caso de falha
    post {
        success {
            slackSend(channel: "${SLACK_CHANNEL}", color: 'good', message: "Pipeline '${env.JOB_NAME} [${env.BUILD_NUMBER}]' foi bem-sucedido! :white_check_mark:")
        }
        failure {
            slackSend(channel: "${SLACK_CHANNEL}", color: 'danger', message: "Pipeline '${env.JOB_NAME} [${env.BUILD_NUMBER}]' falhou. :x:")
        }
        always {
            slackSend(channel: "${SLACK_CHANNEL}", color: 'warning', message: "Pipeline '${env.JOB_NAME} [${env.BUILD_NUMBER}]' terminou com status: ${currentBuild.currentResult}.")
            sh 'docker-compose -f $DOCKER_COMPOSE_FILE down --volumes --remove-orphans'
        }
    }
}
