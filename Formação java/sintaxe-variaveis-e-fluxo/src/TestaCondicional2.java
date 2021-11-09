
public class TestaCondicional2 {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");

		int idade = 18;
		int quantidadeDePessoas = 3;
		boolean acompanhado = quantidadeDePessoas >= 2;
		
		if (idade >= 18 || acompanhado) { // or
			System.out.println("Seja bem vindo!");
		} else {
			System.out.println("Que pena, você não pode entrar");
		}
		
		if (idade >= 18 && acompanhado) { // and
			System.out.println("Seja bem vindo!");
		} else {
			System.out.println("Que pena, você não pode entrar");
		}
	}
}
