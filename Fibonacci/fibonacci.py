# Gerador de sequência Fibonacci
# Autor: mfs9 - github.com/mfs9

def generate_fibonacci_sequence(n):
    sequence = [0, 1]  # Inicializa a sequência com os primeiros dois números
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]  # Calcula o próximo número na sequência
        sequence.append(next_number)  # Adiciona o próximo número à sequência
    return sequence

# Teste do gerador da sequência de Fibonacci
n = 10
fibonacci_sequence = generate_fibonacci_sequence(n)
print(f"A sequência de Fibonacci com {n} números é:")
print(fibonacci_sequence)
