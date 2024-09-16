def calcular_arepas(harina, agua, sal):
  """Calcula la cantidad aproximada de arepas que se pueden hacer.

  Ingredientes:
    harina: Cantidad de harina en gramos.
    agua: Cantidad de agua en mililitros.
    sal: Cantidad de sal en gramos.

  Return:
    La cantidad de arepas.
  """

  # Ajusta estos factores de conversión según tu receta
  gramos_harina_por_arepa = 100
  mililitros_agua_por_arepa = 50

  # Calcula el número de arepas que se pueden hacer con la harina, el agua y la sal
  arepas_por_harina = harina / gramos_harina_por_arepa
  arepas_por_agua = agua / mililitros_agua_por_arepa
  
  # Toma el mínimo para asegurarnos de no exceder la cantidad de ningún ingrediente
  numero_arepas = min(arepas_por_harina, arepas_por_agua)

  return numero_arepas

if __name__ == "__main__":
  harina_str = input("Ingrese la cantidad de harina en gramos: ")
  agua_str = input("Ingrese la cantidad de agua en mililitros: ")
  sal_str = input("Ingrese la cantidad de sal en gramos: ")

  # Convertir los strings a números
  harina = int(harina_str)
  agua = int(agua_str)
  sal = int(sal_str)

  # Calcular el número de arepas
  numero_arepas = calcular_arepas(harina, agua, sal)

  print("Al usar esta cantidad de ingredientes y cocinarlos en un budare con aceite obtenemos lo siguiente")

  print(f"Con los ingredientes ingresados, puedes hacer aproximadamente {numero_arepas} arepas.")

  input("Presiona enter para cerrar y finalizar el programa")