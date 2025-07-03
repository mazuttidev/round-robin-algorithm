import argparse
import random
from cpu.cpu import CPU
from processos.processo import Processo
import sys

RANGE_INI = 1
RANGE_FIM = 50

def simular(quantum, num_processos, use_random, delay):
    cpu = CPU(quantum=quantum)

    processos_iniciais = []
    for i in range(num_processos):
        if use_random:
            tempo = random.randint(RANGE_INI, RANGE_FIM)
            tipo_processo = random.choice(["CPU-Bound", "I/O-Bound"])
            processos_iniciais.append(Processo(f"P{i+1}", tempo, tipo=tipo_processo))
        else:
            tempo = int(input(f"Tempo de execução do processo P{i+1}: "))
            tipo_processo = input(f"Tipo do processo P{i+1} (CPU-Bound/I/O-Bound, padrão CPU-Bound): ")
            if not tipo_processo:
                tipo_processo = "CPU-Bound"
            processos_iniciais.append(Processo(f"P{i+1}", tempo, tipo=tipo_processo))

    for p in processos_iniciais:
        cpu.adicionar_processo(p)
    
    cpu.executar_processos(delay=delay)

def main():
    parser = argparse.ArgumentParser(description="Simulador Round Robin")
    parser.add_argument("--quantum", type=int, required=True, help="Tempo de quantum da CPU")
    parser.add_argument("--processos", type=int, required=True, help="Quantidade de processos")
    parser.add_argument("--random", action="store_true", help="Gerar tempos de execução e tipos de processo aleatórios")
    parser.add_argument("--delay", type=float, default=0.1, help="Delay entre execuções (em segundos)")

    args = parser.parse_args()

    try:
        simular(args.quantum, args.processos, args.random, args.delay)
    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário.")
        sys.exit(0)

if __name__ == "__main__":
    main()