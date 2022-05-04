productos = 0 

def Vecinos(G, a):
    Nodos = ['Entrada', 'Farmacia', 'Panaderia', 'Pescados', 'Frutas-Verduras', 'Abarrotes', 'Lácteos', 'Carnes', 'Cajas', 'Salida']
    vecinos = []
    for i in range(len(G)):
        if G[Nodos.index(a)][i] == 1:
            vecinos.append(Nodos[i])
    return vecinos

def BFS(G, a):
    canasta = 0
    conteo1 = 0
    conteo2 = 0
    conteo3 = 0
    conteo4 = 0
    conteo5 = 0
    conteo6 = 0
    conteo7 = 0
    respuesta = 1
    c = 0
    Cola = []
    Usados = []
    Cola.append(a)
    print("\nDebe comprar minimo 4 productos\n")
    print("Cuantos productos necesitas?")
    productos = int(input())
    if productos>3:
        while canasta < productos:
            if Cola[0]=="Entrada":
               print("\nLugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
            elif Cola[0]=="Farmacia":
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Cubrebocas", "Medicamentos", "Alcohol", "Algodon", "Agua Oxigenada", "Gel Antibacterial"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo1 = canasta
                       if (productos - 1) <= conteo1:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                   else:
                       print("No contamos con ese producto")
                   
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
                
            elif Cola[0]=="Panaderia":
               respuesta = 1
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Bolillo", "Donas", "Pan Chino", "Barquillo", "Oreja", "Concha"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo2 = conteo2 + 1
                       if (productos - 1) <= conteo2:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                       elif(canasta == productos):
                           break;
                   else:
                       print("No contamos con ese producto")
                   
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
            elif Cola[0]=="Frutas-Verduras":
               respuesta = 1
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Manzana", "Fresa", "Mango", "Chayote", "Calabaza", "Jitomate"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo3 = conteo3 + 1
                       if (productos - 1) <= conteo3:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                       elif(canasta == productos):
                           break;
                   else:
                       print("No contamos con ese producto")
                   
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
            elif Cola[0]=="Pescados":
               respuesta = 1
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Mojarras", "Sierra", "Camarones", "Pulpo", "Almejas", "Langosta"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo4 = conteo4 + 1
                       if (productos - 1) <= conteo4:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                       elif(canasta == productos):
                           break;
                   else:
                       print("No contamos con ese producto")
                       
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
            elif Cola[0]=="Abarrotes":
               respuesta = 1
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Atún", "Galletas", "Huevo", "Jabon", "Azucar", "Cafe"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo5 = conteo5 + 1
                       if (productos - 1) <= conteo5:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                       elif(canasta == productos):
                           break;
                   else:
                       print("No contamos con ese producto")
                
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
            elif Cola[0]=="Carnes":
               respuesta = 1
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Bisteck de Res", "Lomo de Cerdo", "Costillas", "Chorizo", "Longaniza", "Medallon de Res"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo6 = conteo6 + 1
                       if (productos - 1) <= conteo6:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                       elif(canasta == productos):
                           break;
                   else:
                       print("No contamos con ese producto")
                
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
            elif Cola[0]=="Lácteos":
               respuesta = 1
               print("\n\t\tCompra ", c)
               print("Lugar", Cola[0])
               v = Vecinos(G, Cola[0])
               print("Vecinos ", v)
               Usados.append(Cola.pop(0))
               while (respuesta == 1):
                   print("¿De la lista proporcionada anteriormente que deseas?")
                   pedido = input()
                   if pedido in ("Queso", "Leche", "Crema", "Yogurt", "Cajeta", "Queso amarillo"):
                       print("Su producto ha sido comprado\n")
                       canasta = canasta + 1
                       conteo7 = conteo7 + 1
                       if (productos - 1) <= conteo7:
                           print("Llegó al límite de productos comprados por Departamento. No puede comprar todos sus productos en un solo departamento, por favor complete sus compras en otro departamento.\n")
                           break;
                       elif(canasta == productos):
                           break;
                   else:
                       print("No contamos con ese producto")
            
                   print("¿Deseas comprar otro artículo de este departamento?\n")
                   print("\t1)SI\t2)N0")
                   respuesta = int(input())
            
               
            for i in range(len(v)):
                if (v[i] not in Cola and v[i] not in Usados):
                    Cola.append(v[i])
            print("Su canasta tiene "+str(canasta)+" producto(s) de "+str(productos)+" que necesita\n")
            print("Cola = ", Cola)
            c = 1+c
        
        print("\nRecorrido = ", Usados, "")
        print("\nPaga en Cajas y va a la Salida")
        print("\nGracias por su compra")
            
    else:
        print("Su carrito no puede contener menos de 4 productos\n")

grafo = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

class Vertice:
    def __init__(self, n):
        self.nombre = n;
        self.vecinos = list()
    
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    vertices = {}
    
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            
            return True
        else:
            return False
    
    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False
        
    def imprimeGrafo(self):
        for key in list(self.vertices.keys()):
            print("Lugar: "+key+", sus vecinos son:"+str(self.vertices[key].vecinos))

class Controladora:
    def main(self):
        #Se crea un objeto 'g' de la clase Grafo, el grafo
        g = Grafo()
        #Se crea un objeto 'a' de la clase vertice, un vertice
        a = Vertice('Entrada')

        #Se agrega el vertice al grafo
        g.agregarVertice(a)
        
        g.agregarVertice(Vertice('Farmacia'))
        g.agregarVertice(Vertice('Panaderia'))
        g.agregarVertice(Vertice('Pescados'))
        g.agregarVertice(Vertice('Frutas-Verduras'))
        g.agregarVertice(Vertice('Abarrotes'))
        g.agregarVertice(Vertice('Lácteos'))
        g.agregarVertice(Vertice('Carnes'))
        g.agregarVertice(Vertice('Cajas'))
        g.agregarVertice(Vertice('Salida'))
            
        #Se declara una lista que contiene las aristas del grafo
        arista1= 'EntradaFarmacia'
        arista2= 'EntradaPanaderia' 
        arista3= 'PanaderiaPescados'
        arista4= 'PanaderiaFrutas-Verduras'
        arista5= 'PanaderiaCajas'
        arista6= 'PescadosCajas'
        arista7= 'Frutas-VerdurasAbarrotes'
        arista8= 'Frutas-VerdurasCajas'
        arista9= 'AbarrotesLácteos'
        arista10= 'AbarrotesCarnes'
        arista11= 'AbarrotesCajas'
        arista12= 'LácteosCarnes'
        arista13= 'LácteosCajas'
        arista14= 'CarnesCajas'
        arista15= 'CajasSalida'
        
        g.agregarArista(arista1[:7], arista1[7:])
        g.agregarArista(arista2[:7], arista2[7:])
        g.agregarArista(arista3[:9], arista3[9:])
        g.agregarArista(arista4[:9], arista4[9:])
        g.agregarArista(arista5[:9], arista5[9:])
        g.agregarArista(arista6[:8], arista6[8:])
        g.agregarArista(arista7[:15], arista7[15:])
        g.agregarArista(arista8[:15], arista8[15:])
        g.agregarArista(arista9[:9], arista9[9:])
        g.agregarArista(arista10[:9], arista10[9:])
        g.agregarArista(arista11[:9], arista11[9:])
        g.agregarArista(arista12[:7], arista12[7:])
        g.agregarArista(arista13[:7], arista13[7:])
        g.agregarArista(arista14[:6], arista14[6:])
        g.agregarArista(arista15[:5], arista15[5:])
        #Se imprime el grafo, como una lista de adyacencia
        g.imprimeGrafo()
       
print("\nDiaz Ramirez Yoeli\n\n")
print("Bienvenid@ a su tienda de autoservicio favorita.\n")
print("La tienda cuenta con los siguientes departamentos y los siguientes productos:\n")
print("\t1)Farmacia:\n\t\tCubrebocas\n\t\tMedicamentos\n\t\tAlcohol\n\t\tAlgodon\n\t\tAgua Oxigenada\n\t\tGel Antibacterial\n")
print("\t2)Panaderia:\n\t\tBolillo\n\t\tDonas\n\t\tPan Chino\n\t\tBarquillo\n\t\tOreja\n\t\tConcha\n")
print("\t3)Frutas y Verduras:\n\t\tManzana\n\t\tFresa\n\t\tMango\n\t\tChayote\n\t\tCalabaza\n\t\tJitomate\n")
print("\t4)Pescados:\n\t\tMojarras\n\t\tSierra\n\t\tCamarones\n\t\tPulpo\n\t\tAlmejas\n\t\tLangosta\n")
print("\t5)Abarrotes:\n\t\tAtun\n\t\tGalletas\n\t\tHuevo\n\t\tJabon\n\t\tAzucar\n\t\tCafe\n")
print("\t6)Lacteos:\n\t\tQueso\n\t\tLeche\n\t\tCrema\n\t\tYogurt\n\t\tCajeta\n\t\tQueso amarillo\n")
print("\t7)Carnes:\n\t\tBisteck de Res\n\t\tLomo de cerdo\n\t\tCostillas\n\t\tChorizo\n\t\tLonganiza\n\t\tMedallon de Res\n")
	
print("\nCada Departamento o Entrada-Salida siguen un camino para llegar a un Departamento, a continuación se ejemplifica de la siguiente manera:\n")
print("\n\t\t\t-------Camino-------")
obj = Controladora()
obj.main()
print("\n\n\t\t\t¡¡¡¡EMPECEMOS LAS COMPRAS!!!!\t\t\t")
BFS(grafo, 'Entrada')