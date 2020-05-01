#Clase 1
class Aprendizaje():
    def __init__(self,libro,lapiz,hojas):
        self.libro=libro
        self.lapiz=lapiz
        self.hojas=hojas
        self.aprender=True
        self.material=False
    def Leer(self,material):
        self.leer1=material
        if(self.leer1):
            return 'Tiene los Materiales'
        else:
            return 'Le falta Materiales'
    def Estudiar(self):
        self.aprender=True
        if(self.aprender==True):
            print( 'Entendiende el Aprendizaje' )
        else:
            print( 'Le falta entendimiento')
    def Comprension(self):
        print("Libro: {} \nLapiz: {} \nHojas: {}".format(self.libro,self.lapiz,self.hojas))

persona=Aprendizaje("Ingles",'Sabonis','Winner')     
persona.Comprension()     
print(persona.Leer(True)) 
persona.Estudiar()
print()
#Clase 2 
class Auto():
    def __init__(self,marca,modelo,color):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.arranca=True
    def arrancar(self):
        self.arranca=True
        if(self.arranca==True):
            print('El auto esta encendido')
        else:
            print('El auto esta apagado')
    def  Componenentes(self):
        print('Marca: ',self.marca,'\nModelo:',self.modelo,'\nColor:',self.color )
a1 = Auto('Toyota','2020','Azul')
a1.Componenentes()
a1.arrancar()
        
        
        
       
        
    