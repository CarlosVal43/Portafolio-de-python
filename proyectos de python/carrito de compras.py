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
                                "cocacola": {"precio":2.00,"descuento":60},
                                "pepsi": {"precio":2.00, "descuento":70}}


def precio(objeto):
        return objeto["precio"]
   
      

def descuento(objeto):
        return objeto["descuento"]

carrito = {}
objetos_comprados = {}

en_la_caja_con_descuento = {}
en_la_caja = {}
def reinicio():
    total_sin_iva = 0
    llena_el_carrito()


def pagar(carrito_de_compras):
   total_sin_iva = 0
   print("")
   print("n\———————————————————————————————————————————————————RESUMEN DE SU COMPRA———————————————————————————————————————————————————")
   for producto, detalles in carrito_de_compras.items():
      
   
      the_precio = precio(detalles)
      porcentaje_de_descuento = descuento(detalles)
      descuento_aplicado = calculo_de_descuentos(the_precio, porcentaje_de_descuento)
      precio_con_descuento = the_precio - descuento_aplicado
      en_la_caja_con_descuento[producto] = precio_con_descuento
      total_sin_iva += precio_con_descuento
   while True:
      print("desea ver el precio de sus compras con descuento sin descuento")
      print("\n1. con descuento")
      print("\n2. sin descuento y porcentaje")
      print("\n3. pagar")
      precio_caja = (input("ingrese su opcion(1, 2, 3):   ")).lower().strip()
      opciones_validas = ("1", "2", "3")
      if precio_caja not in opciones_validas:
        print(f"{precio_caja} ← no es una opcion existente")
        continue
      elif precio_caja == "1":
          for clave, valor in en_la_caja_con_descuento.items():
                
                print(f"{clave}: {valor}1 en el carrito")
                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        
                 
          continue
          
      
      elif precio_caja == "2":
               for clave, valor in carrito.items():
                
                    print(f"{clave}: {valor}% en el carrito")
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        
               continue   
               
      elif precio_caja == "3":
          
      
      
        precio_total_con_iva = calcular_precio_con_iva(total_sin_iva)
        print(f"\nsubtotal: {total_sin_iva:.2f} bs")
        print(f"IVA ({tasa_iva * 100:.0f}%): {tasa_iva * total_sin_iva:.2f}bs")
        print(f"**monto total a pagar**: {total_sin_iva + (tasa_iva * total_sin_iva):.2f}bs")
        
        while True:
            volver = input("ingrese not/n para ir a los estantes o yes/y para pagar:  ").lower().strip()
            opciones_validas3 = ("yes", "y", "not", "n")
            if volver not in opciones_validas3:
                print("opcion invalida")
                continue
            
            elif volver == "n" or volver == "not":
                reinicio()
            elif volver == "y" or volver == "yes":
                print(f"\nsubtotal: {total_sin_iva:.2f} bs")
                print(f"IVA ({tasa_iva * 100:.0f}%): {tasa_iva * total_sin_iva:.2f}bs")
                print(f"**desea realizar la compra?**: {total_sin_iva + (tasa_iva * total_sin_iva):.2f}bs")
                            
                while True:
                        print("y/yes para comprar, n/not para volver")
                        volver2 = input("yes/y or not/n:  ").lower().strip()
                        opciones_validas4 = ("yes", "y", "not", "n")
                        if volver2 not in opciones_validas4:
                            print("opcion invalida")
                            continue
                        elif volver2 == "n" or volver2 == "not":
                            return "volver_a_estantes"



                        elif volver2 == "y" or volver2 == "yes":
                            print("usted a pagado:")
                            print(f"el cargo IVA es: {precio_total_con_iva:.2f}bs")
                            print("por los productos:")
                            for clave in en_la_caja_con_descuento.items():
                
                                print(f"{clave} en el carrito")
                                print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                                print("————————————————————————————————————————————————————————————VUELVA PRONTO—————————————————————————————————————————————————————————————")
                            return "pagado"                            
                        elif volver2 == "n" or volver2 == "not":
                            break
        

   
   









def llena_el_carrito():
    while True:





        print("                         TENEMOS TODOS ESTOS PRODUCTOS PREPARADOS PARA SU DISFRUTE, ELIJA EL QUERRA COMPRAR")
        while True:
            while True:
                print("\nnos quedan estos productos:")
                for clave, valor in lista_de_precios_y_descuentos.items():
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                    print(f"{clave}: {valor}%")
                
            
            
                objeto_al_carrito = input("\ningrese el objeto que quiere colocar en el carrito o 'pagar' para ir a la caja a pagar cuando ya tenga lo que necesita:  ").lower().strip()

                if objeto_al_carrito == 'pagar':
                    break

                if objeto_al_carrito in lista_de_precios_y_descuentos:
                    carrito[objeto_al_carrito] = lista_de_precios_y_descuentos[objeto_al_carrito]
                    del lista_de_precios_y_descuentos[objeto_al_carrito]
                    print(f"\n'{objeto_al_carrito}' se añadió al carrito.")
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                
                else:
                    print(f"\nlo siento, '{objeto_al_carrito}' no esta en nuestra lista de productos, por favor, verifique la ortografia.")
                print("\n———————————————————————————————————————————————————Estado actual del carrito———————————————————————————————————————————————————")
                if carrito:
                    
                    for clave, valor in carrito.items():
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                        print(f"- {clave}: Precio {valor['precio']:.2f} bs, Descuento {valor['descuento']}%")
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                    
                else:
                    print("El carrito está vacío.")
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

            
            
            if objeto_al_carrito == 'pagar':
                    break
        
        
        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

        print("ahora tiene en el carrito: ")
        print("")
        for clave, valor in carrito.items():
                
            print(f"{clave}: {valor}% en el carrito")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
        
        
        
        while True:
            while True:
                print("desea devolver algun produco del carrito?")
                
            
                validacion_de_devolucion = ("yes","y", "not", "n")
                devolver_producto = input("yes or y, not or n:  ").lower().strip()
                if devolver_producto not in validacion_de_devolucion:
                    print("opcion inexistente")
                    continue
                if devolver_producto == "not" or devolver_producto == "n":
                    break
                elif devolver_producto == "yes" or devolver_producto == "y":
                    
                    for clave, valor in carrito.items():
                        
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                        
                        print(f"{clave}: {valor}%")
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                    
                    producto_a_devolver = input("ingrese el producto que quiere devolver:  ").lower().strip()
                    if producto_a_devolver in carrito:
                        lista_de_precios_y_descuentos[producto_a_devolver] = carrito[producto_a_devolver]
                        del carrito[producto_a_devolver]
                        print(f"\n'{producto_a_devolver}' se devolvio a los estantes.")
                        print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                
                    else:
                        print(f"\nlo siento, '{producto_a_devolver}' no esta en el carrito,  revise la ortografia.")
            
            print("\n———————————————————————————————————————————————————CARRITO PARA PAGAR———————————————————————————————————————————————————")
            if carrito:

                for clave, valor in carrito.items():
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

                    print(f"- {clave}: Precio {valor['precio']:.2f} bs, Descuento {valor['descuento']}%")
                    print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

            else:
                print("El carrito está vacío. No hay nada que pagar.")
            print("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")

            
            while True:
                print("\n¿Desea volver a los estantes o pagar?")
                vol_pag = input("Ingrese 'volver' para ir a los estantes o 'pagar' para ir a las cajas: ").lower().strip()
                if vol_pag not in ("volver", "pagar"):
                    print("Opción inexistente.")
                    continue
                break  

   
            return vol_pag


def compras():        
    while True:
        while True:
            accion_principal = llena_el_carrito()
            if accion_principal == "pagar":
                if not carrito:
                    print("El carrito está vacío, no se puede proceder al pago. volviendo a los estantes.")
                    continue 
                estado_pago = pagar(carrito)
                if estado_pago == "pagado":
                    while True:
                        otra_compradict = ("no", "n", "y", "yes")
                        otra_compra = input("¿Desea realizar otra compra? (yes/not): ").lower().strip()
                        if otra_compra not in otra_compradict:
                            print("opcion inexistente")
                            continue
                        elif otra_compra == "yes" or otra_compra == "y":
                            
                            break
                        elif otra_compra == "not" or otra_compra == "n":
                            print("————————————————————————————————————————————————————————————VUELVA PRONTO———————————————————————————————————————————————————————————")
                            break
                      
                    break 
                elif estado_pago == "volver_a_estantes":
                    
                    pass
            elif accion_principal == "volver":
                
                pass
        if otra_compra == "yes" or otra_compra == "y":
            carrito.clear
            continue            
        elif otra_compra == "not" or otra_compra == "n":
                            print("————————————————————————————————————————————————————————————VUELVA PRONTO———————————————————————————————————————————————————————————")
                            break

compras()





