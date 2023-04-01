
class persona:
    
    
    def __init__(self):
        self.nivel_energia=80
        self.cont = 0

    def jugar(self):
        
        while self.cont==0:
            res = input("ingrese 'S' para volver a jugar o 'N' para terminar: ").lower()
            if res == "s":
                self.nivel_energia = 80
                self.accion()
            elif res == "n":
                print("Juego terminado")
                self.cont+=1

    def datos(self):
        nombre=input("Digite el Nombre: ")
        edad=int(input("Digite tu edad: "))
        cc=int(input("Digite su cedula "))
        self.nombre=nombre
        self.edad=edad
        self.cc=cc
        self.accion()
           
    
    def accion(self):
        usuario= int(input("Elige y escribe el numero de la accion que desea realizar  \n 1) Comer sano \n 2) Dormir \n 3) Comer sin restricciones \n 4) Correr \n 5) Ver TV \n 6) Caminar \n 7) Salir \n"))
        if usuario == 1:
            self.comsersano()
        elif usuario == 2:
            self.Dormir()
        elif usuario == 3:
            self.ComerSinRestriccion()
        elif usuario == 4:
            self.Correr()
        elif usuario == 5:
            self.vertv()
        elif usuario == 6:
            self.caminar() 
        elif usuario == 7:
            self.jugar()      
          
            
    
    def comsersano(self):
        print(f"{self.nombre} esta comiendo sano")
        self.nivel_energia+=30
        print("Su nivel de energia subio a: ",self.nivel_energia)
        self.val() 
        while self.nivel_energia >= 20 and self.nivel_energia <= 255:
            self.accion()
        
        
    
    def Dormir(self):
        print(f"{self.nombre} esta Durmiendo")
        self.nivel_energia+=100
        print("Su nivel de energia subio a: ", self.nivel_energia)
        self.val()
        while self.nivel_energia >= 20 and self.nivel_energia <= 255:
            self.accion()
       

        
    def ComerSinRestriccion(self):
        print(f"{self.nombre} esta comiendo sin restriccion")
        self.nivel_energia+=75
        print("Su nivel de energia subio a: ",self.nivel_energia)
        self.val()
        while self.nivel_energia >= 20 and self.nivel_energia <= 255:
            self.accion()
        

    
    def Correr(self):
        print(f"{self.nombre} esta Corriendo")
        self.nivel_energia-=20
        print("Su nivel de energia Disminuido a: ",self.nivel_energia)
        self.val()
        while self.nivel_energia >= 20 and self.nivel_energia <= 255:
            self.accion()
        

        
    def vertv(self):
        print(f"{self.nombre} esta viendo tv")
        self.nivel_energia-=5
        print("Su nivel de energia Disminuido a: ",self.nivel_energia)
        self.val()
        while self.nivel_energia >= 20 and self.nivel_energia <= 255:
            self.accion()
        

    
    def caminar(self):
        print(f"{self.nombre} esta caminando")
        self.nivel_energia-=10
        print("Su nivel de energia Disminuido a: ",self.nivel_energia)
        self.val()
        while self.nivel_energia >= 20 and self.nivel_energia <= 255:
            self.accion()

    def val(self):
        
        if(self.nivel_energia>=20 and self.nivel_energia<=40):
            print("Su nivel de energia esta muy bajo por favor aumenta tu energia")
                
        elif(self.nivel_energia<20):
            print(f"{self.nombre} con el numero de cedula: {self.cc}, murio a sus: {self.edad} Años de edad")
            print("Su nivel de energia esta muy baja su personaje murio")
            self.jugar()
                
        
        elif(self.nivel_energia>=250 and self.nivel_energia<=255):
            print(f"Su personaje tiene o supera los 250 de energia, tiene {self.nivel_energia} esto provocara que se desmaye")
                
        elif(self.nivel_energia>255):
            print(f"{self.nombre} con el numero de cedula: {self.cc}, murio a sus: {self.edad} Años de edad")
            print("Su personaje murio")
            self.jugar()
   
        else:
            print("Su personaje tiene buen nivel de energia") 
        



ejercutar = persona()
ejercutar.datos()
    
     
    

           
       

 
    



            

           


    


