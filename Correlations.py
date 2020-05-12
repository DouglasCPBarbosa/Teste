# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:00:08 2018

@author: dougl
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #Incluido pra conflito

dataset = pd.read_excel('BD - RealZin_2Classes.xlsx')
X = dataset.iloc[:,:1001].values
#y = dataset.iloc[:,2002:2004].values
#y = dataset.iloc[:,1001].values

#Nome_Haste = dataset.iloc[:,2004]

Corr_Max = []
Ind_Max = []
Corr_Min = []
Ind_Min = []
Correlations = []

menor = 0
maior = 2

for i in range(menor, maior):
    print("passo " + str(i))
    linha = []
    a = X[i]
    for j in range(menor, maior):
        b = X[j]
        corr = np.corrcoef(a, b)
        linha.append(corr[0][1])
#ALTERADO AQUI (DELETE)
    Correlations.append(linha[:])
    Corr_Min.append(min(linha))
    Ind_Min.append(np.argmin(linha)+menor)
    linha[i-menor] = 0
    Corr_Max.append(max(linha))
    Ind_Max.append(np.argmax(linha)+menor)


    


