
public class ContaPoupanca extends Conta {

	public ContaPoupanca(int agencia, int numero){
		super(agencia, numero);
	}
	
	@Override
	public boolean saca(double valor) {
		double valorDoSaque = valor + 0.3;
		return super.saca(valorDoSaque);
	}
	
	@Override
	public void deposita(double valor) {
		super.saldo += valor;
		
	}
	

}
