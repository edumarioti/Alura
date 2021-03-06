

public abstract class Conta {
	protected double saldo;
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int total;
	
	public Conta(int agencia, int numero) {
		total++;
		//System.out.println("O total de contas ?: " + total);
		//System.out.println("Criando a Conta " + numero);
		this.agencia = agencia;
		this.numero = numero;
	}

	public abstract void deposita(double valor);

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
	
	public double getSaldo() {
		return this.saldo;
	}	
	
	public int getNumero() {
		return this.numero;
	}
	
	public void setNumero(int numero) {
		if (numero <= 0) {
			System.out.println("N?o pode valor menor ou igual a zero!");
			return;
		}
		this.numero = numero;
	}

	public int getAgencia() {
		return this.agencia;
	}

	public void setAgencia(int agencia) {
		if (agencia <= 0) {
			System.out.println("N?o pode valor menor ou igual a zero!");
			return;
		}
		this.agencia = agencia;
	}

	public Cliente getTitular() {
		return this.titular;
	}

	public void setTitular(Cliente titular) {
		this.titular = titular;
	}
	
	public static int getTotal() {
		return total;
	}
	
	
	
}
