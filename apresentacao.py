import numpy as np
import pandas as pd

#mudancas = np.array([["Ijexa - 4/4 - 105", 0, 4, 105]])
#mudancas = np.append(mudancas, [["Transiçao Ijexa - 6/8 - 210", 8, 6, 210]], axis=0)
#mudancas = np.append(mudancas, [["Barravento - 6/8 - 210", 9, 6, 210]], axis=0)
#mudancas = np.append(mudancas, [["Retomada barravento - 4/4 - 140", 14, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Samba - 4/4 - 140", 24, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["XL - 4/4 - 140", 32, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Salmonela - 4/4 - 140", 63, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Treansicion - 4/4 - 140", 82, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Noveoito - 9/8 - 280", 86, 9, 280]], axis=0)
#mudancas = np.append(mudancas, [["Retomada - 4/4 - 140", 100, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Aquarela Chamada - 4/4 - 140", 112, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Aquarela Solo - 4/4 - 140", 138, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Bhangra desengatada - 3/4 - 140", 164, 3, 140]], axis=0)
#mudancas = np.append(mudancas, [["Bhangra makonha - 4/4 - 187", 167, 4, 187]], axis=0)
#mudancas = np.append(mudancas, [["Bhangra Solo - 4/4 - 187", 185, 4, 187]], axis=0)
#mudancas = np.append(mudancas, [["UUUMMM DOIS - 4/4 - 187", 205, 4, 187]], axis=0)
#mudancas = np.append(mudancas, [["Samba - 4/4 - 140", 218, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Tois - 4/4 - 140", 224, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Samba em 6 - 6/4 - 140", 261, 6, 140]], axis=0)
#mudancas = np.append(mudancas, [["Brastemp - 4/4 - 140", 263, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Jongo - 4/4 - 140", 283, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Pare - 4/4 - 140", 298, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Flamenco Intro - 7/4 - 140", 305, 7, 140]], axis=0)
#mudancas = np.append(mudancas, [["Flamenco REAL - 4/4 - 93", 306, 4, 93]], axis=0)
#mudancas = np.append(mudancas, [["Flamenco CERNE - 12/8 - 93", 317, 12, 93]], axis=0)
#mudancas = np.append(mudancas, [["Flamenco FINAL - 3/4 - 140", 339, 3, 140]], axis=0)
#mudancas = np.append(mudancas, [["Samba - 4/4 - 140", 335, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["N sei - 4/4 - 140", 349, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Solo pinico - 4/4 - 140", 363, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Makulele - 4/4 - 140", 390, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Whiskas - 4/4 - 140", 402, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Whiskas LENTO - 4/4 - 93", 406, 4, 93]], axis=0)
#mudancas = np.append(mudancas, [["SOLO DE SEXO - 4/4 - 196", 421, 4, 196]], axis=0)
#mudancas = np.append(mudancas, [["BLACK HAHAHA - 4/4 - 196", 435, 4, 196]], axis=0)
#mudancas = np.append(mudancas, [["Frevo - 4/4 - 196", 451, 4, 196]], axis=0)
#mudancas = np.append(mudancas, [["Saksifufu - 4/4 - 140", 468, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Hunter - 4/4 - 140", 485, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Bilu intro - 3/4 - 140", 523, 3, 140]], axis=0)
#mudancas = np.append(mudancas, [["Bilu - 4/4 - 140", 527, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Makumba - 5/4 - 140", 556, 5, 140]], axis=0)
#mudancas = np.append(mudancas, [["Makumba - 4/4 - 140", 557, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Makumba - 5/4 - 140", 559, 5, 140]], axis=0)
#mudancas = np.append(mudancas, [["Makumba - 4/4 - 140", 560, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Timpanos - 4/4 - 140", 570, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Caveça - 4/4 - 140", 586, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Dinossauro - 4/4 - 140", 622, 4, 140]], axis=0)
#mudancas = np.append(mudancas, [["Pre final - 3/4 - 140", 639, 3, 140]], axis=0)
#mudancas = np.append(mudancas, [["CABO - 4/4 - 140", 641, 4, 140]], axis=0)

#                     Nome - Anotaçoes uteis            posicao   metrica  andamento  duraçao
mudancas = np.array([["Ijexa - 4/4 - 105",                  0,      4,      105,    8],
                     ["Transiçao Ijexa - 6/8 - 210",        8,      6,      210,    2],
                     ["Barravento - 6/8 - 210",             9,      6,      210,    4],
                     ["Barravento seco - 4/4 - 140",        9,      6,      210,    2],
                     ["Retomada barravento - 4/4 - 140",    14,     4,      140,    7],
                     ["Samba - 4/4 - 140",                  24,     4,      140,    8],
                     ["XL - 4/4 - 140",                     32,     4,      140,    31],
                     ["Salmonela - 4/4 - 140",              63,     4,      140,    19],
                     ["Treansicion - 4/4 - 140",            82,     4,      140,    4],
                     ["Noveoito - 9/8 - 280",               86,     9,      280,    14],
                     ["Retomada - 4/4 - 140",               100,    4,      140,    12],
                     ["Aquarela Chamada - 4/4 - 140",       112,    4,      140,    26],
                     ["Aquarela Solo - 4/4 - 140",          138,    4,      140,    26],    # daqui pra cima acho q ta check
                     ["Bhangra desengatada - 3/4 - 140",    164,    3,      140,    3],
                     ["Bhangra makonha - 4/4 - 187",        167,    4,      187,    17],    
                     ["Bhangra Solo - 4/4 - 187",           185,    4,      187,    20],    
                     ["Bhangra Resto - 4/4 - 187",          185,    4,      187,    14],                        
                     ["Samba - 4/4 - 140",                  218,    4,      140,    7],     # daqui pra baixo check
                     ["Tois - 4/4 - 140",                   224,    4,      140,    37],
                     ["Samba em 6 - 6/4 - 140",             261,    6,      140,    2],
                     ["Brastemp - 4/4 - 140",               263,    4,      140,    19],
                     ["Jongo - 4/4 - 140",                  283,    4,      140,    13],
                     ["Pare - 4/4 - 140",                   296,    4,      140,    12],
                     #["Flamenco Intro - 7/4 - 140",         308,    7,      140,    1],     # PUTARIO NAO SEI
                     #["Flamenco REAL - 4/4 - 93",           309,    4,      93,     11],    # PUTARIA
                     #["Flamenco CERNE - 12/8 - 93",         320,    12,     93,     22],    # PUTARIA
                     #["Flamenco FINAL - 3/4 - 140",         342,    3,      140,    0],     # PUTARIA
                     ["Samba - 4/4 - 140",                  335,    4,      140,    4],     # daqui pra baixo ta certo
                     ["N sei - 4/4 - 140",                  349,    4,      140,    14],
                     ["Solo pinico - 4/4 - 140",            363,    4,      140,    27],
                     ["Makulele - 4/4 - 140",               390,    4,      140,    12],
                     ["Whiskas - 4/4 - 140 (apito)",        402,    4,      140,    3],     # errado
                     ["Whiskas LENTO - 4/4 - 93",           406,    4,      93,     15],    # errado
                     ["SOLO DE SEXO - 4/4 - 196",           421,    4,      196,    16],    # errado
                     ["BLACK HAHAHA - 4/4 - 196",           435,    4,      196,    16],    # errado
                     ["Frevo - 4/4 - 196",                  451,    4,      196,    17],    # começa qnd o chocalho entra
                     ["Saksifufu - 4/4 - 140",              468,    4,      140,    17],    # acho q ta certo
                     ["Hunter - 4/4 - 140",                 485,    4,      140,    31],
                     ["Samba - 4/4 - 140",                  485,    4,      140,    6],
                     ["Bilu intro - 3/4 - 140",             523,    3,      140,    5],
                     ["Bilu - 4/4 - 140 (com samba)",       527,    4,      140,    29],
                     ["Makumba - 5/4 - 140",                556,    5,      140,    1],
                     ["Makumba - 4/4 - 140",                557,    4,      140,    2],
                     ["Makumba - 5/4 - 140",                559,    5,      140,    1],
                     ["Makumba - 4/4 - 140",                560,    4,      140,    10],
                     ["Timpanos - 4/4 - 140",               570,    4,      140,    16],
                     ["Caveça - 4/4 - 140",                 586,    4,      140,    32],
                     ["Samba - 4/4 - 140",                  622,    4,      140,    8],
                     ["Dinossauro - 4/4 - 140",             622,    4,      140,    19],
                     #["Pre final - 3/4 - 140",              639,    3,      140,    2],
                     ["CABO - 4/4 - 140",                   641,    4,      140,    1]
                     ]) 

df = pd.DataFrame(mudancas)
print(mudancas)

df.to_csv("apresentacao.csv", header=False, index=False)