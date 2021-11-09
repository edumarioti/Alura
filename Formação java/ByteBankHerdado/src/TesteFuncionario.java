
public class TesteFuncionario {

	public static void main(String[] args) {
		
		Funcionario edu = new Gerente();
		
		edu.setNome("Eduardo Marioti");
		edu.setCpf("116.165.236-18");
		edu.setSalario(2500);
		
		System.out.println(edu.getNome());
		System.out.println(edu.getBonificacao());
	}
}
