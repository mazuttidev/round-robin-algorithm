import time
import math

class CPU:
    def __init__(self, quantum):
        self.quantum = quantum
        self.fila_processos = []
        self.tempo_simulacao_atual = 0
        self.processos_finalizados = []

    def adicionar_processo(self, processo):
        self.fila_processos.append(processo)

    def executar_processos(self, delay=0):
        print("\nIniciando simulação Round Robin:\n")

        while self.fila_processos:
            processo = self.fila_processos.pop(0)

            exec_time = min(processo.tempo_restante, self.quantum)
            
            if processo.tipo == "I/O-Bound" and exec_time > 0:
                exec_time = random.randint(1, exec_time) if exec_time > 0 else 0
            
            if exec_time > 0:
                self.tempo_simulacao_atual += exec_time
                finalizado = processo.executar(self.quantum)
            else:
                finalizado = True

            if delay != 0:
                time.sleep(delay)

            if finalizado:
                self.processos_finalizados.append(processo)
            else:
                self.fila_processos.append(processo)

        print(f"\n--- Simulação Finalizada ---")
        print(f"Tempo total de simulação: {self.tempo_simulacao_atual} unidades")
        print(f"Total de processos finalizados: {len(self.processos_finalizados)}")

        if len(self.processos_finalizados) > 0:
            tempos_execucao_reais = [p.tempo_total_executado for p in self.processos_finalizados if p.tempo_total_executado > 0]
            
            if tempos_execucao_reais:
                tempo_medio_execucao = sum(tempos_execucao_reais) / len(tempos_execucao_reais)
                tempo_max_execucao = max(tempos_execucao_reais)
                tempo_min_execucao = min(tempos_execucao_reais)

                print(f"\n--- Estatísticas de Execução por Processo ---")
                print(f"Tempo médio de execução (CPU): {tempo_medio_execucao:.2f} unidades")
                print(f"Maior tempo de execução (CPU): {tempo_max_execucao} unidades")
                print(f"Menor tempo de execução (CPU): {tempo_min_execucao} unidades")
            else:
                print("\nNenhum processo teve tempo de execução real para estatísticas.")
        
        return self.tempo_simulacao_atual