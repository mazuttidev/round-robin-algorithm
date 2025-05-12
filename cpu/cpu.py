import time 

class CPU:
    def __init__(self, quantum):
        self.quantum = quantum
        self.fila_processos = []

    def adicionar_processo(self, processo):
        self.fila_processos.append(processo)

    def executar_processos(self, delay=0):
        tempo_total = 0
        tempos_individuais = {}
        print("\nIniciando simulação Round Robin:\n")

        while self.fila_processos:
            processo = self.fila_processos.pop(0)
            exec_time = min(processo.tempo_restante, self.quantum)
            tempo_total += exec_time

            if processo.nome not in tempos_individuais:
                tempos_individuais[processo.nome] = 0
            tempos_individuais[processo.nome] += exec_time

            finalizado = processo.executar(self.quantum)

            if delay != 0:
                time.sleep(delay)

            if not finalizado:
                self.fila_processos.append(processo)

        print(f"\nTempo total de execução: {tempo_total}")
        tempo_medio = tempo_total / len(tempos_individuais)
        return tempo_medio
