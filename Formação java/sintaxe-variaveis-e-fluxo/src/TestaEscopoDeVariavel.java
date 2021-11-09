
public class TestaEscopoDeVariavel {
	public static void main(String[] args) {
		System.out.println("Testando condicionais");

		int idade = 18;
		int quantidadeDePessoas = 3;
		boolean acompanhado;
		
		if (quantidadeDePessoas >= 2) {
			acompanhado = true;
		} else {
			acompanhado = false;
		}
		
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
