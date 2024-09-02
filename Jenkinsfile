pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        SLACK_CHANNEL = 'cypherus.slack.com'
        SLACK_CREDENTIAL_ID = 'U07KYDUBWHF'
    }

    stages {

        // Clonae o repositório onde estão o código da aplicação e o arquivo docker-compose.yml.
        stages('Checkout') {
            steps {
                git curl: 'https://github.com/Auggustto/DesafioTecnicoBackend'
            }
        }

        // Construindo as imagens e subindo os containers
        stages('Build and Start Containers') {
            steps{
                script {
                    sh 'docker-compose.yml -f $DOCKER_COMPOSE_FILE up --build -d'
                }
            }
        }

        // Executa os testes dentro do container
        stages('Run tests') {
            steps {
                sh 'docker-compose -f $DOCKER_COMPOSE_FILE run test'
            }
        }

        // Derruba os containers e limpa os recursos
        stages('Stop and clean Up') {

            steps{
                sh 'docker-compose -f $DOCKER_COMPOSE_FILE down --volumes --remove-orphans'
            }
        }
    }
    // Garante que os containers serão derrubados mesmo em caso de falha
    post {
        always {
            sh 'docker-compose -f $DOCKER_COMPOSE_FILE down --volumes --remove-orphans'
        }
        success {
            slackSend(channel: "${SLACK_CHANNEL}", color: 'good', message: "Pipeline '${env.JOB_NAME} [${env.BUILD_NUMBER}]' foi bem-sucedido! :white_check_mark:")
        }
        failure {
            slackSend(channel: "${SLACK_CHANNEL}", color: 'danger', message: "Pipeline '${env.JOB_NAME} [${env.BUILD_NUMBER}]' falhou. :x:")
        }
        always {
            slackSend(channel: "${SLACK_CHANNEL}", color: 'warning', message: "Pipeline '${env.JOB_NAME} [${env.BUILD_NUMBER}]' terminou com status: ${currentBuild.currentResult}.")
        }
    }
}
