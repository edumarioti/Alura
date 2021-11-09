
public class TestaCondicional {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");

		int idade = 20;
		int quantidadeDePessoas = 2;
		
		if (idade >= 18) {
			System.out.println("Você tem mais de 18 anos");
			System.out.println("Seja bem vindo!");
		} else {
			if (quantidadeDePessoas >= 2) {
				System.out.println("Você não tem mais de 18 anos, mas está acompanhado.");
				System.out.println("Seja bem vindo!");
			} else {
				System.out.println("Que pena, você não pode entrar");
			}
		}
	}
}
