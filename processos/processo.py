class Processo:
    def __init__(self, nome, tempo_execucao):
        self.nome = nome
        self.tempo_restante = tempo_execucao

    def executar(self, quantum):
        if self.tempo_restante > quantum:
            print(f"{self.nome} executa por {quantum} unidades (resta {self.tempo_restante - quantum})")
            self.tempo_restante -= quantum
            return False
        else:
            print(f"{self.nome} executa por {self.tempo_restante} unidades (finaliza)")
            self.tempo_restante = 0
            return True
