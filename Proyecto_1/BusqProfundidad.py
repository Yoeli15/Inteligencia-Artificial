productos = 0 

class Vertice:
    def __init__(self, n):
        self.nombre = n;
        self.vecinos = list()
        
        self.d = 0
        self.f = 0
        self.color = 'white'
        self.pred = -1
    
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafo:
    vertices = {}
    tiempo = 0
    
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
                #if key == v:
                    #value.agregarVecino(u)
            return True
        else:
            return False
        
    def imprimeGrafo(self):
        for key in list(self.vertices.keys()):
            print("Lugar: "+key)
            print("Búsqueda: "+str(self.vertices[key].d)+" Cerrado: "+str(self.vertices[key].f))
    
    def imprimeGrafo2(self):
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
        print("\nDebe comprar minimo 4 productos\n")
        print("Cuantos productos necesitas?")
        productos = int(input())
        if productos>3:
            while canasta < productos:
                for key in list(self.vertices.keys()):
                    if canasta == productos:
                        break;
                        
                    elif key == "Entrada":
                        print("Lugar: "+key)
                        
                    elif key == "Farmacia":
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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
                        
                    elif key == "Panaderia":
                       respuesta = 1
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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
                           
                    elif key == "Frutas-Verduras":
                       respuesta = 1
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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
                           
                    elif key == "Abarrotes":
                       respuesta = 1
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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
                           
                    elif key == "Carnes":
                       respuesta = 1
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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

                    elif key == "Lácteos":
                       respuesta = 1
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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
                    
                    elif key == "Pescados":
                       respuesta = 1
                       print("\n\t\tCompra ", c)
                       print("Lugar: "+key)
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
                    
                    print("Su canasta tiene "+str(canasta)+" producto(s) de "+str(productos)+" que necesita\n")
                    c = 1+c
            print("\nPaga en Cajas y va a la Salida")
            print("\nGracias por su compra")
                    
        else:
            print("Su carrito no puede contener menos de 4 productos\n")
        
    
    def dfs(self,vert):
        global tiempo
        tiempo = 0
        for u in list(self.vertices.keys()):
            if self.vertices[u].color == 'white':
                self.dfsVisitar(self.vertices[u])
    
    def dfsVisitar(self,vert):
        global tiempo
        tiempo = tiempo + 1
        vert.d = tiempo
        vert.color = "gris"
        
        for v in vert.vecinos:
            if self.vertices[v].color == "white":
                self.vertices[v].pred=vert
                self.dfsVisitar(self.vertices[v])
        vert.color = "black"
        tiempo = tiempo + 1
        vert.f = tiempo
        
class Controladora:
    def topologicalSort(self, G):
        a = Vertice('A')
        lista = G.dfs(a)
        print(lista)
        
    def main(self):
        g = Grafo()
        a = Vertice('Entrada')
        g.agregarVertice(a)
        
        g.agregarVertice(Vertice('Entrada'))
        g.agregarVertice(Vertice('Farmacia'))
        g.agregarVertice(Vertice('Panaderia'))
        g.agregarVertice(Vertice('Frutas-Verduras'))
        g.agregarVertice(Vertice('Abarrotes'))
        g.agregarVertice(Vertice('Lácteos'))
        g.agregarVertice(Vertice('Carnes'))
        g.agregarVertice(Vertice('Cajas'))
        g.agregarVertice(Vertice('Salida'))
        g.agregarVertice(Vertice('Pescados'))
        
        arista1= 'EntradaFarmacia'
        arista2= 'EntradaPanaderia' 
        arista4= 'PanaderiaPescados'
        arista3= 'PanaderiaFrutas-Verduras'
        arista5= 'Frutas-VerdurasAbarrotes'
        arista6= 'AbarrotesLácteos'
        arista7= 'AbarrotesCarnes'
        arista8= 'AbarrotesCajas'
        arista9= 'LácteosCarnes'
        arista10= 'CarnesCajas'
        arista11= 'CajasSalida'
        
        g.agregarArista(arista1[:7], arista1[7:])
        g.agregarArista(arista2[:7], arista2[7:])
        g.agregarArista(arista3[:9], arista3[9:])
        g.agregarArista(arista4[:9], arista4[9:])
        g.agregarArista(arista5[:15], arista5[15:])
        g.agregarArista(arista6[:9], arista6[9:])
        g.agregarArista(arista7[:9], arista7[9:])
        g.agregarArista(arista8[:9], arista8[9:])
        g.agregarArista(arista9[:7], arista9[7:])
        g.agregarArista(arista10[:6], arista10[6:])
        g.agregarArista(arista11[:5], arista11[5:])
        
        g.dfs(a)
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
	
print("\nCada Departamento o Entrada-Salida siguen un camino para llegar a otro Departamento, a continuación se ejemplifica de la siguiente manera:\n")
print("\n\t\t\t-------Camino-------")
obj = Controladora()
obj.main()
print("\n\n\t\t\t¡¡¡¡EMPECEMOS LAS COMPRAS!!!!\t\t\t")
obj2 = Grafo()
obj2.imprimeGrafo2()