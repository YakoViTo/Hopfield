import numpy as np
import matplotlib.pyplot as plt

# Función para actualizar la red de Hopfield de forma síncrona
def hopfield_update(weights, patterns, steps=100):
    memory_patterns = patterns.copy()
    N, P = patterns.shape
    for _ in range(steps):
        s = np.random.randint(0, N)
        memory_patterns[s] = np.sign(np.dot(weights[s], memory_patterns))
    return memory_patterns

# Función para calcular la matriz de pesos de Hopfield
def hopfield_weights(patterns):
    N, P = patterns.shape
    weights = np.zeros((N, N))
    for p in range(P):
        pattern = patterns[:, p].reshape(N, 1)
        weights += np.dot(pattern, pattern.T)
    np.fill_diagonal(weights, 0)
    return weights / N

# Función para mostrar patrones como letras
def plot_patterns_as_letters(patterns, title):
    N, P = patterns.shape
    letters = []
    for i in range(P):
        letter = ''
        for j in range(N):
            if patterns[j, i] == 1:
                letter += 'X'  # Letra 'X' para representar el patrón activado
            else:
                letter += ' '  # Espacio vacío para representar el patrón desactivado
        letters.append(letter)
    cols = int(np.ceil(np.sqrt(P)))
    _, ax = plt.subplots(cols, cols, figsize=(10, 10))
    for i in range(P):
        ax[i//cols, i%cols].text(0.5, 0.5, letters[i], fontsize=20, ha='center', va='center')
        ax[i//cols, i%cols].axis('off')
    plt.suptitle(title)
    plt.show()

# Patrones de letras (matriz de 25x3, cada columna es un patrón)
patterns = np.array([[1, 1, 1, -1, 1,  # Letra A
                      1, -1, -1, 1, 1,
                      1, 1, 1, 1, 1,
                      1, -1, -1, 1, 1,
                      1, -1, -1, 1, 1],
                     [-1, 1, 1, 1, -1,  # Letra B
                      -1, 1, -1, 1, -1,
                      -1, 1, 1, 1, -1,
                      -1, 1, -1, 1, -1,
                      -1, -1, -1, 1, -1],
                     [1, 1, 1, 1, 1,   # Letra C
                      1, -1, -1, -1, -1,
                      1, -1, -1, -1, -1,
                      1, -1, -1, -1, -1,
                      1, 1, 1, 1, 1]])

# Crear matriz de pesos de la red de Hopfield
weights = hopfield_weights(patterns)

# Mostrar los patrones originales
plot_patterns_as_letters(patterns, 'Patrones Originales')

# Almacenar los patrones en la red de Hopfield para recuperarlos
memory_patterns = hopfield_update(weights, patterns.copy())

# Mostrar los patrones recuperados
plot_patterns_as_letters(memory_patterns, 'Patrones Recuperados')

# Contar cuántos patrones ha recordado la red
matching_patterns = np.sum(np.all(memory_patterns == patterns, axis=0))
print(f"La red ha recordado {matching_patterns} patrones.")
