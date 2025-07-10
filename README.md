# Simulador de Escalonamento - Round Robin

Este projeto é uma simulação do algoritmo de escalonamento **Round Robin**, amplamente utilizado em sistemas operacionais para gerenciar múltiplos processos em uma CPU.

A implementação é feita com **Python orientado a objetos**, organizando o código em classes (`CPU`, `Processo`) e módulos para melhor estrutura e manutenção.

---

## Funcionalidades

- Simulação do algoritmo Round Robin no terminal.
- Adição e execução de múltiplos processos com tempos distintos.
- Saída clara e passo a passo da execução de cada processo.
- Código modular e extensível para outros algoritmos de escalonamento.
- Entradas do usuário via terminal:
    - tempo do quantum;
    - quantidade de execuções; 
    - --random para gerar valores aleatórios de processos;
- Exibição de média de tempo de execução.
- Interrupção do programa.

---

## Como rodar

--quantum 3: Define o quantum da CPU como 3 unidades de tempo.

--processos 3: O programa solicitará a entrada para 3 processos.

--delay 0.05: Um pequeno atraso para acompanhar o fluxo.

--random: Ativa a geração aleatória de tempos de execução E tipos de processo (CPU-Bound ou I/O-Bound).

python main.py --quantum 5 --processos 10 --random --delay 0.1
python main.py --quantum 3 --processos 3 --delay 0.05
python main.py --quantum 8 --processos 15 --random

### Pré-requisitos
- Python 3.8 ou superior

### Executando a simulação:

```bash
git clone https://github.com/mazuttidev/round-robin-algorithm.git
cd round-robin-algorithm
