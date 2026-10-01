class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"Cuenta {self.numero_cuenta} - {self.titular} - Saldo: S/ {self.__saldo:.2f}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0.0, tasa_interes=4.0):
        super().__init__(numero_cuenta, titular, saldo)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        return self.consultar_saldo() * self.tasa_interes / 100

    def __str__(self):
        return super().__str__() + f" - Tasa: {self.tasa_interes}% - Interes: S/ {self.calcular_interes():.2f}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, saldo=0.0, limite_sobregiro=600.0):
        super().__init__(numero_cuenta, titular, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        if monto > self.consultar_saldo() + self.limite_sobregiro:
            raise ValueError("Excede el limite de sobregiro")
        super().retirar(min(monto, self.consultar_saldo()))
        if monto > self.consultar_saldo():
            excedente = monto - self.consultar_saldo()
            self._CuentaBancaria__saldo = -excedente

    def permite_sobregiro(self):
        return self.consultar_saldo() < 0


if __name__ == "__main__":
    ahorros = CuentaAhorros("AH-001", "Jorge Alvaro", 1000.0, 4.0)
    ahorros.depositar(500)
    ahorros.retirar(200)
    print(ahorros)
    print(f"Interes ganado: S/ {ahorros.calcular_interes():.2f}")

    corriente = CuentaCorriente("CC-001", "Jorge Alvaro", 300.0, 500.0)
    corriente.retirar(600)
    print(corriente)
    print(f"Permite sobregiro: {corriente.permite_sobregiro()}")