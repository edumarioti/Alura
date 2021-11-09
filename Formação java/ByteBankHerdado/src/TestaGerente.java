
public class TestaGerente {

	public static void main(String[] args) {
		Gerente gerente = new Gerente();
		
		gerente.setNome("Gerente Marioti");
		gerente.setCpf("200.165.236-18");
		gerente.setSalario(5000);
		gerente.setSenha(2345);
		
		System.out.println(gerente.getNome());
		System.out.println(gerente.getBonificacao());
		
		System.out.println(gerente.autentica(2345));
		
		System.out.println(gerente.getBonificacao());
	}
}
