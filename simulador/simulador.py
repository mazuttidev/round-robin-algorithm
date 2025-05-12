import argparse
import random
from cpu.cpu import CPU
from processos.processo import Processo
RANGE_INI = 1
RANGE_FIM = 50

def simular(quantum, num_processos, use_random, delay):
    cpu = CPU(quantum=quantum)

    processos = []
    for i in range(num_processos):
        tempo = random.randint(RANGE_INI, RANGE_FIM) if use_random else int(input(f"Tempo de execução do processo P{i+1}: "))
        processos.append(Processo(f"P{i+1}", tempo))

    for p in processos:
        cpu.adicionar_processo(p)

    tempo_medio = cpu.executar_processos(delay=delay)
    print(f"\nTempo médio por processo: {tempo_medio:.2f} unidades")

def main():
    parser = argparse.ArgumentParser(description="Simulador Round Robin")
    parser.add_argument("--quantum", type=int, required=True, help="Tempo de quantum da CPU")
    parser.add_argument("--processos", type=int, required=True, help="Quantidade de processos")
    parser.add_argument("--random", action="store_true", help="Gerar tempos de execução aleatórios")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay entre execuções (em segundos)")

    args = parser.parse_args()

    try:
        simular(args.quantum, args.processos, args.random, args.delay)
    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário.")

if __name__ == "__main__":
    main()