#DESCRIPTIVE STATISTICS
#ejercicio 1
 
import numpy as np  

np.random.normal(loc=0, scale =1, size = 100)

#PRIMERA PARTE
arraynormal = np.random.normal(loc=0, scale =1, size = 100)
print(arraynormal)

#SEGUNDA PARTE
arraychisquare = np.random.chisquare(df = 3, size = 100)
print(arraychisquare)

#TERCERA PARTE
#PARA LA DISTRIBUCION NORMAL

np.mean(arraynormal)
np.std(arraynormal)
np.median(arraynormal)
np.min(arraynormal)
np.max(arraynormal)
rango1 = np.max(arraynormal) - np.min(arraynormal)
percentil_251 = np.percentile(arraynormal, 25)
print("Los datos para la distribucion normal seria una media de",np.mean(arraynormal), "una desviacion standar de", np.std(arraynormal), "una mediana de", np.median(arraynormal), "un rango de",rango1, "percentil 25 de", percentil_251) 

#PARA LA DISTRIBUCION CHI-SQUARE

np.mean(arraychisquare)
np.std(arraychisquare)
np.median(arraychisquare)
np.min(arraychisquare)
np.max(arraychisquare)
rango2 = np.max(arraychisquare) - np.min(arraychisquare)
percentil_252 = np.percentile(arraychisquare, 25)
print("Los datos para la distribucion chisquare seria una media de",np.mean(arraychisquare), "una desviacion standar de", np.std(arraychisquare), "una mediana de", np.median(arraychisquare), "un rango de",rango2, "percentil 25 de", percentil_252) 


#ejercicio 2

data = [4, 2, 5, 8, 6]

np.std(data)






