import keyboard
import time

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

durations = np.genfromtxt('data.csv', delimiter=',')

df = pd.read_csv("apresentacao.csv", header=None)
mudancas = df.to_numpy()

partituraMeas = np.empty([0, 1])
partituraTempo = np.empty([0, 1])
for i in range(len(mudancas)):
    num = int(mudancas[i][4])
    partituraMeas = np.append(partituraMeas, num*[int(mudancas[i][2])])
    partituraTempo = np.append(partituraTempo, num*[int(mudancas[i][3])])

beatReference = np.array([])
for mudanca in mudancas:
    num = int(mudanca[4])
    if (len(beatReference) > 0):
        beatReference = np.append(beatReference, np.sum(partituraMeas[:int((beatReference[-1]+num))]))
    else:
        beatReference = np.append(beatReference, np.sum(partituraMeas[:num]))    

beats = 0
temposPerMeasure = np.array([])
for measure in partituraMeas:
    bpm = 60/(np.average(durations[beats:int(beats+measure)]))
    beats += int(measure)
    temposPerMeasure = np.append(temposPerMeasure, bpm)
    
print(len(durations))


average = 6
mediaMovel = temposPerMeasure[:average]
for i in range(len(temposPerMeasure)):
    if i > (average-1):
        sum = 0
        n = 0
        for j in range(average):
            if (np.abs(temposPerMeasure[i-j] - partituraTempo[i]) < partituraTempo[i]*0.2):
                sum += temposPerMeasure[i-j]*(average-j)
                n += (average-j)
            elif (j == 0):
                sum += partituraTempo[i]*(average-j)
                n += (average-j)
        if(n != 0):
            sum = sum/n
            mediaMovel = np.append(mediaMovel, [sum])
        else:
            mediaMovel = np.append(mediaMovel, temposPerMeasure[i])            

x = range(len(partituraMeas))  # 100 pontos entre 0 e 10
y = temposPerMeasure  # Aplicando a função seno aos valores de x

fig, axs = plt.subplots(2)

#axs[0].plot(x, y)
axs[0].plot(x, partituraTempo)
axs[0].plot(x, mediaMovel)

# Adicionar título e rótulos aos eixos
plt.title('Gráfico da função Seno')
plt.xlabel('Compasso')

axs[0].set_ylim(50, 300)

axs[1].plot(x, (mediaMovel-partituraTempo)/partituraTempo)

axs[1].set_ylim(-0.3, 0.3)
axs[1].sharex(axs[0])

axs[1].hlines(0, 0, len(partituraTempo), linestyle='--', linewidth=0.6)


refAnterior = 0
for mudanca in mudancas:
    nCompasso = refAnterior
    num = int(mudanca[4])
    refAnterior += num
    axs[0].vlines(nCompasso, 0, 300, linestyle='--', linewidth=0.1, label="oi")
    axs[1].vlines(nCompasso, 0, 300, linestyle='--', linewidth=0.1, label="oi")
    axs[0].annotate(mudanca[0], [int(nCompasso), int(mudanca[3])], fontsize=5, rotation=60)

sumErro = 0
a = 0
for i in range(len(mediaMovel)):
    if(mediaMovel[i] < 1000 and np.abs((mediaMovel[i]-partituraTempo[i])/partituraTempo[i]) < 0.23):
        sumErro += (mediaMovel[i]-partituraTempo[i])/partituraTempo[i]
        a += 1
    
print("Erro total da apresentaçao:", sumErro/a*100, "%")
print("\nErro por virada:")
refAnterior = 0
for mudanca in mudancas:
    nCompasso = refAnterior
    num = int(mudanca[4])
    refAnterior += num
    
    erro = 0
    count = 0
    for i in range(nCompasso, refAnterior):
        if (np.abs((mediaMovel[i]-partituraTempo[i])/partituraTempo[i]) < 0.23):
            erro += (mediaMovel[i]-partituraTempo[i])/partituraTempo[i]
            count += 1
            
    erro = erro/count*100
    axs[1].annotate("Avg:"+str(erro)[:4] + "%", [(nCompasso+num/2)-2, 0.1], fontsize=7)
    
    print("Erro da", mudanca[0], "==", erro, "%")
    
    
    
# Exibir o gráfico
plt.show()
