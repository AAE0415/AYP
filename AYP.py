#Funciones

def Dish(dish, menu):
  with open(menu, "a") as inventory:
    inventory.write(f"{dish}\n")

#Funcion de los platos
def Add_dish(archive, ingredients_can):

  #Ciclo para agregar los ingredientes
  for i in range (1, ingredients_can + 1):
    ingredient = input(f"Ingrese el ingrediente {i}: ")
    can_ingredient = input("Ingrese la cantidad del ingrediente por porciones: ")
    ingredient_price = input("Ingrese el precio de la porcion del ingrediente: ")
    #Validador de digito
    if can_ingredient.isdigit() and ingredient_price.isdigit():
      with open(archive, "a") as inv:
        inv.write(f"{ingredient}:{can_ingredient}:{ingredient_price}\n")
    else:
      print("Ingrese valores validos!!")
      break

#Consulta, que sirve como validador
def Consult(menu):
  consult = False

  try:
    with open(menu, "r") as inventory:
      print(inventory.read())
    consult = True
  except FileNotFoundError:
    print("No se encuentra platos en el menu, debera agregar uno para crear la carpeta")
  return consult

def Avaliability(dish, dish_menu):
  avaliability = True
  try:
    with open(dish_menu, "r") as inventory:
      #ciclo para buscar 
      for i in inventory:
        ingredient, ingredient_can, ingredient_price = i.strip().split(":")
        if int(ingredient_can) == 0:
          avaliability = False
          break
  except FileNotFoundError:
    print("No se encuentra el plato que solicito!")

  return avaliability

def Total_cost(dish, dish_menu):
  subtotal = 0
  total = 0
  try:
    with open(dish_menu, "r") as inventory:
      #ciclo para buscar 
      for i in inventory:
        ingredient, ingredient_can, ingredient_price = i.strip().split(":")
        subtotal += float(ingredient_price) 
      #El total sera el costo de los ingredientes mas el 10% de ese valor
      total = subtotal * 1.1
      print(f"El precio del plato {dish} es: {total}")  

  except FileNotFoundError:
    print("No se encuentra el plato que solicito!")

#Compra

def Buy(dish, dish_menu):
    avaliability = Avaliability(dish, dish_menu)

    if avaliability == True:
      try:
          # Leer el archivo del plato
          with open(dish_menu, "r") as inventory:
              # Guardar cada linea como lista en la variable "lines"
              lines = inventory.readlines()
              print(lines)
          # Actualizar la cantidad de ingredientes
          updated_lines = []
          for line in lines:
              ingredient, ingredient_can, ingredient_price = line.strip().split(":")
              # restar 1 la cantidad de cada ingrediente
              # Hacer que el valor maximo que pueda llegar es 0
              updated_can = max(0, int(ingredient_can) - 1)
              updated_lines.append(f"{ingredient}:{updated_can}:{ingredient_price}\n")
          print(updated_lines)
          # Escribir los cambios al archivo del plato
          with open(dish_menu, "w") as inventory:
              inventory.writelines(updated_lines)
          
          print(f"Compra de {dish} realizada con éxito. Se ha actualizado el inventario.")
      
      except FileNotFoundError:
          print("No se encuentra el plato que solicito!")

    else: 
      print("El plato no esta disponible!!")


#Codigo principal

while True:
  print("///Bienvenido a Rapid Food\\\\n")
  print("1. Agregar plato")
  print("2. Consultar")
  print("3. Salir")
  option = input("Ingrese una opcion: ")

  if option == "1":
    dish = input("Ingrese el plato de que desea agregar: ").lower()
    archive = dish + ".txt"
    ingredient_can = int(input("Ingrese la cantidad de ingredientes del plato: "))
    Add_dish(archive, ingredient_can)
    #Crear menu
    menu = "menu.txt"
    Dish(dish, menu)

  elif option == "2":
    menu = "menu.txt"
    consult = Consult(menu)
    #Validacion para seguir en el caso de que existan productos
    if consult == True:
      while True:
        print("Bienvenido a Consulta!! \n1. Ver disponibilidad de plato especifico \n2. Ver el precio de un plato \n3. Comprar un plato \n4. Salir")
        option = input("Ingrese la opcion deseada: ")
        #Ver dispinibilidad del producto con base a los ingredientes disponibles
        if option == "1":
          dish = input("Ingrese el plato a consultar")
          dish_menu = dish + ".txt"
          avaliability = Avaliability(dish, dish_menu)
          if avaliability == True:
            print(f"El plato {dish} se encuentra disponible")
          else:
            print(f"El plato {dish} no se encuentra disponible")  
        #Ver el precio total del plato que se desea seleccionar
        elif option == "2":
          dish = input("Ingrese el plato a consultar")
          dish_menu = dish + ".txt"
          Total_cost(dish, dish_menu)
        
        #Realizar la compra
        elif option == "3":
          
          dish = input("Ingrese el plato que desea comprar: ")
          dish_menu = dish + ".txt"
          Buy(dish, dish_menu)


        elif option == "4":
          break
        else:
          print("Seleccione una opcion correcta")

  elif option == "3":
    break

  else:
    print("Ingrese una opcion correcta") 
