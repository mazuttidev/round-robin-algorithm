from cpu.cpu import CPU
from processos.processo import Processo

def simular():
    cpu = CPU(quantum=2)

    processos = [
        Processo("P1", 5),
        Processo("P2", 3),
        Processo("P3", 1)
    ]

    for p in processos:
        cpu.adicionar_processo(p)

    cpu.executar_processos()
