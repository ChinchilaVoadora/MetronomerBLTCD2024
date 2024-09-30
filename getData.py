import keyboard
import time

import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# Variável para armazenar o tempo da última tecla pressionada
last_time = None

durations = np.array([])

df = pd.read_csv("apresentacao.csv", header=None)
mudancas = df.to_numpy()

partituraMeas = np.empty([0, 1])
partituraTempo = np.empty([0, 1])
for i in range(len(mudancas)):
    num = int(mudancas[i][4])
    partituraMeas = np.append(partituraMeas, num*[int(mudancas[i][2])])
    partituraTempo = np.append(partituraTempo, num*[int(mudancas[i][3])])

refAnterior = 0
beatReference = np.array([])
for mudanca in mudancas:
    num = int(mudanca[4])
    nCompasso = num+refAnterior
    refAnterior += num
    beatReference = np.append(beatReference, np.sum(partituraMeas[:int((nCompasso))]))  

print(beatReference)
count = 0
mudancasCount = 0
# Função para calcular o tempo entre cliques do teclado
def on_key_event(event):
    global last_time
    current_time = time.time()
    
    global count
    global durations
    global mudancasCount
    global beatReference
    global mudancas

    if last_time is not None:
        time_between_clicks = current_time - last_time
        durations = np.append(durations, time_between_clicks)
        count += 1
        if (count > beatReference[mudancasCount]):
            mudancasCount += 1
        print("\n\n\n")
        print(f"Tempo entre cliques: {time_between_clicks:.4f} segundos")
        print(f"Proxima mudanca em {beatReference[mudancasCount] - count} - {mudancas[mudancasCount+1, 0]}")
    
    # Atualiza o tempo da última tecla pressionada
    last_time = current_time

# Configura o listener para capturar qualquer tecla pressionada
keyboard.on_press(on_key_event)

# Mantém o programa em execução
keyboard.wait('esc')  # O programa vai parar ao pressionar 'esc'

np.savetxt('data.csv', durations, delimiter=',')