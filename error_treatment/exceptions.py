class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, saldo=None, valor=None, *args, **kwargs):
        self.saldo = saldo
        self.valor = valor
        self.msg = "Saldo insuficiente para efetuar a transação\n" \
              f"Saldo Atual: {self.saldo}, Valor a ser sacado: {self.valor}"
        super(SaldoInsuficienteError, self).__init__(self.msg, self.saldo, self.valor, *args)