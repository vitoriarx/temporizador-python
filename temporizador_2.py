
import math

import time

def main():
  
  minutos = int(input("Informe os minutos: "))

  segundos = int(input("Informe os segundos: "))

  total_segundos = (minutos * 60) + segundos

  while total_segundos >= 0:
   
    minutos = math.floor(total_segundos / 60)
    
    segundos = total_segundos - (minutos * 60)
    print(minutos, "min", segundos, "s")
    
    total_segundos = total_segundos - 1

    
    time.sleep(1)

  if segundos == 0:
    print("Tempo esgotado")

if __name__== "__main__":
  main()
