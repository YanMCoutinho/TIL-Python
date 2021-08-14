class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}]"

conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

conta_do_gui.deposita(100)
print(conta_do_gui)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)

# tupla

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)
#paulo = (39, 'Paulo', 1979) wrong


#usar tuplas para listar coisas onde a posição importam