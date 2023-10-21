class suma:
    def __init__(self, numero1, numero2):
        self.num1 = numero1
        self.num2 = numero2
    def resu_suma(self):
        print(self.num1 + self.num2)
    def resu_restas(self):
        print(self.num1 - self.num2)
    def resu_multi(self):
        print(self.num1 * self.num2)
    def resu_div(self):
        print(self.num1 / self.num2 if self.num2 > 0 else 'no se puede dividir para 0')
suma1 = suma(5, 2)
suma1.resu_suma()
resta1 = suma(5,2)
resta1.resu_restas()
multi1 = suma(5,2)
multi1.resu_multi()
div1 = suma(5,2)
div1.resu_div()

#encontrar el area y perimetro por separado en un cuadrado utilizando una clase
class cuadrado:
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        print(self.lado * self.lado)
    def perimetro(self):
        print(self.lado * 4)
cuadradoa = cuadrado(5)
cuadradoa.area()
cuadradol = cuadrado(10)
cuadradol.perimetro()

print("Ejercicio de banco")
#registrar un nombre y un capital de la persona y tiene que el usuario depositar o retirar dinero y muestremem el saldo
class banco:
    def __init__(self, nombre, capital):
        self.name = nombre #el self es hacer referencia a lo que el objeto tiene
        self.capital = capital
    def depositar(self, deposito):
        self.capital += deposito
    def retirar(self, retiro):
        self.capital -= retiro #if self.capital >= retiro else 'no tiene saldo suficiente'
    def saldo(self):
        print(self.capital)
usuario1 = banco('Juan', 100)
usuario1.depositar(100)
usuario1.retirar(50)
print("El saldo de", usuario1.name, "es", usuario1.capital)

#Quiero registrar el titulo de un libro y su autor y que me permita cambiar el nombre del autor del libro
class libro:
    def __init__(self, titulo, autor):
        self.title = titulo
        self.author = autor
    def mostrar_libro(self):
        print("El libro ", self.title,"es ", self.author)
    def cambiar_autor(self, nuevo_autor):
        self.author = nuevo_autor
        
libro1 = libro('El rey leon', 'de Juan Aviles')
libro1.mostrar_libro()
libro1.cambiar_autor = 'El autor (Juan Aviles) sera cambiado a -> Maria Aviles'
print(libro1.cambiar_autor)









