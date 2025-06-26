def calculo_de_descuentos(precioC, descuentoC):
    return   (descuentoC / 100) * precioC


def calcular_precio_con_iva(precioC):

  precio_con_iva = precioC * tasa_iva
  return precio_con_iva



tasa_iva = 0.16
lista_de_precios_y_descuentos = {"pan": {"precio": 1.50, "descuento": 16},
                                "mayonesa":{"precio": 2.99, "descuento": 32}, 
                                "harina":{"precio": 3.00, "descuento":43},
                                "arroz":{"precio": 2.00,"descuento": 50},
                                "leche":{"precio":4.00, "descuento": 10},
                                "pasta":{ "precio":2.30, "descuento": 23},
                                "zucaritas": {"precio":5.00,"descuento": 15},
                                "cocacola": {"precios":2.00,"descuento":60},
                                "pepsi": {"precio":2.00, "descuento":70}}


def precio(objeto):
   if objeto in carrito:
        return carrito[objeto]["precio"]
   else:
        return None

def descuento(objeto):
   if objeto in carrito:
        return carrito[objeto]["descuento"]
   else:
        return None
carrito = {}
objetos_comprados = {}

en_la_caja_con_descuento = {}
en_la_caja = {}

def pagar(carrito_de_compras):
   print("———————————————————————————————————————————————————RESUMEN DE SU COMPRA———————————————————————————————————————————————————")
   for producto, detalles in carrito_de_compras.items():
      
   
      the_precio = precio(detalles)
      porcentaje_de_descuento = descuento(detalles)
      descuento_aplicado = calculo_de_descuentos(the_precio, porcentaje_de_descuento)
      precio_con_descuento = the_precio - descuento_aplicado
      en_la_caja_con_descuento[producto] = precio_con_descuento
      total_sin_iva += precio_con_descuento
   while True:
      print("desea ver el precio de sus compras con descuento sin descuento")
      print("1. con descuento")
      print("2. sin descuento y porcentaje")
      precio_caja = input("ingrese su opcion:   ")
      opciones_validas = ("1", "2")
      if precio_caja not in opciones_validas:
        print(f"{precio_caja} ← no es una opcion existente")
      elif precio_caja == "1":
          print(en_la_caja)
          while True:
            print("desea ver el precio de sus compras con descuento sin descuento")
            print("1. con descuento")
            print("2. sin descuento y porcentaje")
            precio_caja = input("ingrese su opcion:   ")
            opciones_validas = ("2")
            if precio_caja not in opciones_validas:
               print(f"{precio_caja} ← no es una opcion existente")
      
            elif precio_caja == "2":
               print(carrito)   
               break
      precio_total_con_iva = calcular_precio_con_iva(total_sin_iva)
      print(f"\nsubtotal: {total_sin_iva:.2f} bs")
      print(f"IVA ({tasa_iva * 100:.0f}%): {precio_total_con_iva - total_sin_iva:.2f}bs")
      print(f"**total a pagar: {precio_total_con_iva:.2f}bs")
      print("————————————————————————————————————————————————————————————VUELVA PRONTO—————————————————————————————————————————————————————————————")
      
      
   
   









def llena_el_carrito():

   print("                         TENEMOS TODOS ESTOS PRODUCTOS PREPARADOS PARA SU DISFRUTE, ELIJA EL QUERRA COMPRAR")
   while True:
      while True:
        print("\nnos quedan estos productos:")
        for clave, valor in lista_de_precios_y_descuentos.items():
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
            print(f"{clave}: {valor}%")
            
         
        
        objeto_al_carrito = input("\ningrese el objeto que quiere colocar en el carrito o 'pagar' para ir a la caja a pagar cuando ya tenga lo que necesita:  ").lower()

        if objeto_al_carrito == 'pagar':
            break

        if objeto_al_carrito in lista_de_precios_y_descuentos:
            carrito[objeto_al_carrito] = lista_de_precios_y_descuentos[objeto_al_carrito]
            del lista_de_precios_y_descuentos[objeto_al_carrito]
            print(f"\n'{objeto_al_carrito}' se añadió al carrito.")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
            
        else:
            print(f"\nLo siento, '{objeto_al_carrito}' no esta en nuestra lista de productos, por favor, verifique la ortografia.")
      if objeto_al_carrito == 'pagar':
            break
      
      
   print("")
   print("ahora tiene en el carrito: ")
   print("")
   for clave, valor in carrito.items():
            
      print(f"{clave}: {valor}% en el carrito")
      print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
   





llena_el_carrito()

pagar(carrito)
