
public class TestaContaDaMarcela {

	public static void main(String[] args) {
		Conta contaDaMarcela = new Conta();
		contaDaMarcela.titular = new Cliente();
		
		System.out.println(contaDaMarcela.titular);
		contaDaMarcela.titular.nome = "Marcela";
		contaDaMarcela.titular.cpf = "222.222.222-22";
		contaDaMarcela.titular.profissao = "Mecânica";
	}
	
}
