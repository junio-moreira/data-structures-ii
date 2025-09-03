import random

def generate_arrays():
    sizes = [10, 100, 1000]
    arrays = []  # Criamos uma lista para armazenar os vetores
    
    for size in sizes:
        array = random.sample(range(size * 10), size)
        arrays.append(array)  # Adicionamos o vetor à lista
        print(f"Vetor com {size} itens criado com sucesso!")
        
    return arrays # Retornamos a lista de vetores

# Dicionário contendo todos os arrays de teste
test_arrays = {
    "array": [10, 7, 3, 9, 4, 1, 6, 0, 2, 8, 5],
    "array_slides": [11, 4, 30, 22, 7, 26],
    "any_numbers": random.sample(range(1, 1000), 42),
    "already_sorted": [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 32, 34, 39, 40, 42, 76, 87, 99, 112],
    "inversed": [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1],
    "repeated": [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1],
}