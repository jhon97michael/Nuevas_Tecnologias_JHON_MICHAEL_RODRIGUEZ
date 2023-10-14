

from persona import Persona #estp importa la clase persona para ser usada en otra clase

# En test persona hemos importado la clase persona creamos una instancia de persona

persona1 = Persona(1,"Pepito","Perez","pepito@mail.com","xyz123")

#id = 1

#persona1._id(id) # Esto genera un error porque el valor esta protegido

persona1.imprimir_persona()
