# Höfundur: Milos Petrovic
# Dagsetning: 17.10.2023
# Verkefni: Forritun 1B - Spurning 1

def farenheitToCelsius(floatingpoint:float) -> float:
  return (5/9)*(floatingpoint-32)

def main():
  mamma = float(input("Hitastig á farengeit skala: "))
  print("Það eru : {:4.2f} gráður á Celsius".format(farenheitToCelsius(mamma)))

main()