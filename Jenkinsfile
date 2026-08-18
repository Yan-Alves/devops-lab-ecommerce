pipeline {
    agent any

    stages {
        stage('Análise de Segurança com o SonarQube') {
            steps {
                script {
                    // Puxando a ferramenta configurada na interface do Jenkins
                    def scannerHome = tool 'sonar-scanner'
                    
                    // Usando a conexão 'sonarqube' que foi criada com o Token
                    withSonarQubeEnv('sonarqube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        stage('Deploy no Kubernetes') {
            steps {
                echo "Simulando o deploy da aplicação no cluster Kubernetes..."
                sh "cat kubernetes/ecommerce-deploy.yaml"
                // Após a validação do SonarQube virá o comando real de apply
            }
        }
    }
}
