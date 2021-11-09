
public class TestaMetodo {

	public static void main(String[] args) {
		Conta conta = new Conta();
		conta.saldo = 100;
		conta.deposita(100);
		
		System.out.println(conta.saldo);
		
		boolean conseguiuRetirar = conta.saca(50);
		if (conseguiuRetirar) {
			System.out.println(conta.saldo);
		} else {
			System.out.println("Saldo insuficiente!");
		}
		
		Conta contaDoEdu = new Conta();
		contaDoEdu.deposita(2000);
		if(contaDoEdu.transfere(2500, conta)) {
			System.out.println("transferencia realizada, saldo atual: " + conta.saldo);
		} else {
			System.out.println("Saldo insuficiente!");
		}
		
	}
}
