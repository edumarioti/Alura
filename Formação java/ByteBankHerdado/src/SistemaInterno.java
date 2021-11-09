
public class SistemaInterno {
	
	private int senha = 2222;
	
	public void autentica(FuncionarioAtenticavel funcionario) {
		boolean autenticou = funcionario.autentica(this.senha);
		if (autenticou) {
			System.out.println("Autenticou!");
		} else {
			System.out.println("Acesso negado!");
		}
		
	}
}
