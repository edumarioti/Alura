
public class TestaCondicional {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");

		int idade = 20;
		int quantidadeDePessoas = 2;
		
		if (idade >= 18) {
			System.out.println("Voc� tem mais de 18 anos");
			System.out.println("Seja bem vindo!");
		} else {
			if (quantidadeDePessoas >= 2) {
				System.out.println("Voc� n�o tem mais de 18 anos, mas est� acompanhado.");
				System.out.println("Seja bem vindo!");
			} else {
				System.out.println("Que pena, voc� n�o pode entrar");
			}
		}
	}
}
