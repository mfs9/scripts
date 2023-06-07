import random
import string

def gerar_senha(comprimento=12):
    # Define os caracteres que serão usados para gerar a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera a senha aleatória, selecionando 'comprimento' caracteres da string 'caracteres'
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    # Retorna a senha gerada
    return senha

# Exemplo de uso:
# Chama a função 'gerar_senha' sem especificar o comprimento (usa o valor padrão 12)
senha_gerada = gerar_senha()
# Imprime a senha gerada
print(senha_gerada)
