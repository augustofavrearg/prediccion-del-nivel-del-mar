import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
   # Create scatter plot
  figura, ax = plt.subplots(figsize=(16, 9))
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


  # Create first line of best fit
  
  result2 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  start_year2 = df["Year"].min()
  end_year2 = 2050

   


    
  #diccionario que contiene clave valor y se va a rellenar con los valores qeu toma una funcion lineal que queremos diagramar
  best_fit_data2 = {
          "Year": [],
          "y_value": []
      }
  #relleno de los valores de las claves en el diccionario
  for year in range(start_year2, end_year2):
          
          #funcion lineal f(x)=mx+b
          
          #primer relleno= f(x)
    best_fit_data2["Year"] = [year for year in range(start_year2, end_year2)]
    #segundo relleno= mx+b
    best_fit_data2["y_value"] = [result2.slope * year + result2.intercept for year in range(start_year2, end_year2)]
  #'r' color rojo
  #linea de diccionario clave valor [0](f(x)) y clave valor [1] (mx+b)
  plt.plot(best_fit_data2["Year"], best_fit_data2["y_value"], 'r')


    # Create second line of best fit
  start_year3 = 2000
  end_year3 = 2050
  result3 = linregress(df.loc[df["Year"]>= start_year3]["Year"], df.loc[df["Year"]>= start_year3]["CSIRO Adjusted Sea Level"])
  
  best_fit_data3 = {
          "Year": [],
          "y_value": []
      }
  #relleno de los valores de las claves en el diccionario
  for year in range(start_year3, end_year3):
          
          #funcion lineal f(x)=mx+b
          
          #primer relleno= f(x)
    best_fit_data3["Year"] = [year for year in range(start_year3, end_year3)]
    #segundo relleno= mx+b
    best_fit_data3["y_value"] = [result3.slope * year + result3.intercept for year in range(start_year3, end_year3)]
  #'r' color rojo
  #linea de diccionario clave valor [0](f(x)) y clave valor [1] (mx+b)
  plt.plot(best_fit_data3["Year"], best_fit_data3["y_value"], 'y')

    # Add labels and title
  ax.set_title("Rise in Sea Level")
  ax.set_xlabel("Year")
  ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()