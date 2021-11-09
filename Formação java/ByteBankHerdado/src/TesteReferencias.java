
public class TesteReferencias {

	public static void main(String[] args) {
		
		Gerente gerente = new Gerente();
		gerente.setNome("Eduardo");
		gerente.setSalario(5000);
		
	
		ControleBonificacao controle = new ControleBonificacao();
		controle.registra(gerente);	
		System.out.println(controle.getSoma());
		
	}
}
 