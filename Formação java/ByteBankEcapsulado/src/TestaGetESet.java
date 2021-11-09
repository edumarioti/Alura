
public class TestaGetESet {

	public static void main(String[] args) {
		Conta conta = new Conta(123, 253);
		conta.setNumero(12235);
		System.out.println(conta.getNumero());
		
		Cliente cliente = new Cliente();
		cliente.setNome("Eduardo Marioti");
		
		conta.setTitular(cliente);
		System.out.println(conta.getTitular().getNome());
		
		conta.getTitular().setProfissao("Desenvolvedor");
	}
}
