from smallest_element import *

# Função única para testar qualquer algoritmo de ordenação
def test_sorting_algorithm(algorithm_name, sorting_function, array_to_sort):
    """
    Testa um algoritmo de ordenação com o array de teste.

    Args:
        algorithm_name (str): O nome do algoritmo a ser exibido.
        sorting_function (function): A função do algoritmo de ordenação (ex: bubble_sort).
    """
   
    print(f"--- Testando: {algorithm_name} ---")
    print("Desordenado:")
    print(array_to_sort)
    
    # Cria uma cópia do array para não modificar o original
    # pois os algoritmos de ordenação o fazem in-place.
    array_copy = list(array_to_sort)
    
    # Chama a função de ordenação passada como argumento
    sorting_function(array_copy)
    
    print("\nOrdenado:")
    print(array_copy)
    print("*******************************\n")

def test_find_smallest_algorithm(array_to_test):
    """
    Testa a função find_smallest e imprime o resultado.
    
    Args:
        array_to_test (list): O array a ser analisado.
    """
    print("--- Testando: find_smallest ---")
    print("Array de teste:")
    print(array_to_test)

    # Chama a função find_smallest
    smallest_index = find_smallest(array_to_test)
    
    # Imprime o índice e o valor do menor elemento
    print(f"\nO menor elemento está no índice: {smallest_index}")
    print(f"O valor do menor elemento é: {array_to_test[smallest_index]}")
    
    print("*******************************\n")
