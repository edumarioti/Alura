
public class TestaBanco {

	public static void main(String[] args) {
		Cliente edu = new Cliente();
		edu.nome = "Eduardo Marioti";
		edu.cpf = "011.654.479-16";
		edu.profissao = "Desenvolvedor";
		
		Conta contaDoEdu = new Conta();
		contaDoEdu.titular = edu;
		contaDoEdu.deposita(100);
	}
}
