public class App {
    public static void main(String[] args) {
        System.out.println("Iniciando a API do E-commerce...");
        // Causando uma vulnerabilidade proposital para o SonarQube captar
        String dbPassword = "senha_secreta_123"; 
        System.out.println("Conectando ao banco com a senha: " + dbPassword);
    }
}
