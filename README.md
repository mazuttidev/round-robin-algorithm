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

### Pré-requisitos
- Python 3.8 ou superior

### Executando a simulação:

```bash
git clone https://github.com/mazuttidev/round_robin_simulador.git
cd round_robin_simulador
python main.py
