import random

class Processo:
    def __init__(self, nome, tempo_execucao, tipo="CPU-Bound"):
        self.nome = nome
        self.tempo_restante = tempo_execucao
        self.tipo = tipo
        self.tempo_total_executado = 0

    def executar(self, quantum):
        tempo_utilizado = 0
        if self.tipo == "CPU-Bound":
            tempo_utilizado = min(self.tempo_restante, quantum)
        elif self.tipo == "I/O-Bound":
            tempo_max_io = min(self.tempo_restante, quantum)
            tempo_utilizado = random.randint(1, tempo_max_io) if tempo_max_io > 0 else 0
        
        self.tempo_restante -= tempo_utilizado
        self.tempo_total_executado += tempo_utilizado

        if self.tempo_restante > 0:
            print(f"{self.nome} ({self.tipo}) executa por {tempo_utilizado} unidades (resta {self.tempo_restante})")
            return False
        else:
            print(f"{self.nome} ({self.tipo}) executa por {tempo_utilizado} unidades (finaliza)")
            return True