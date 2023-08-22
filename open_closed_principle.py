from abc import ABC, abstractmethod

class InterfaceFunc(ABC):

    @classmethod
    @abstractmethod
    def processar_pagamento(valor: float):
        ...


class FuncionarioCLT(InterfaceFunc):

    def __init__(self, valor: float = 0.0) -> None:
        self.salario = valor

    def processar_pagamento(self, valor: float):
        """Implementar regra de nogocio"""
        self.salario = float(valor)


class FuncionarioPJ(InterfaceFunc):

    def __init__(self, valor: float = 0.0) -> None:
        self.salario = valor

    def processar_pagamento(self, valor: float):
        """Implementar regra de nogocio"""
        self.salario = float(valor)

if __name__ == '__main__':
    clt = FuncionarioCLT()
    clt.processar_pagamento(1000)
    print(f'clt: {clt.salario}')

    pj = FuncionarioPJ()
    pj.processar_pagamento(1000)
    print(f'pj: {pj.salario}')
