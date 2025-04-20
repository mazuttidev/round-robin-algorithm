class CPU:
    def __init__(self, quantum):
        self.quantum = quantum
        self.fila_processos = []

    def adicionar_processo(self, processo):
        self.fila_processos.append(processo)

    def executar_processos(self):
        tempo_total = 0
        print("\nIniciando simulação Round Robin:\n")

        while self.fila_processos:
            processo = self.fila_processos.pop(0)
            finalizado = processo.executar(self.quantum)
            if not finalizado:
                self.fila_processos.append(processo)
                tempo_total += self.quantum
            else:
                tempo_total += processo.tempo_restante

        print(f"\nTempo total de execução: {tempo_total}")
