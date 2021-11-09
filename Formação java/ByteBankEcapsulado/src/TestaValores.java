
public class TestaValores {

	public static void main(String[] args) {
		
		Conta conta = new Conta(7226, 65113);
		System.out.println(conta.getAgencia());
		
		Conta conta2 = new Conta(7226, 65114);
		Conta conta3 = new Conta(7226, 65115);
		
		
		System.out.println("\nTotal de contas: " + Conta.getTotal());
		
	}
}
