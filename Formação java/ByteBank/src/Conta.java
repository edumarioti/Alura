public class Conta {
	double saldo;
	int agencia;
	int numero;
	String titular;

	public void deposita(double valor) {
		this.saldo += valor;
	}

	public boolean saca(double valor) {
		if (valor <= this.saldo) {
			this.saldo -= valor;
			return true;
		}
		return false;

	}

	public boolean transfere(double valor, Conta destino) {
		boolean saqueRealizado = this.saca(valor);
		if (saqueRealizado) {
			destino.deposita(valor);
			return true;
		}
		return false;

	}

}
