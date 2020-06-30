# primer clase de modulos tutorial (24)
# modulo = son archivos con exrenciones py los cuales se utilizan dentro de otro archivo.
# archivo compilado (pyc) asi es mas rapido, se encuntra en la carpeta creada __pycache__
import calculadora

resultado = calculadora.suma(30,45)
pass#print(resultado)
# clase 2 modulo tutorial (25)
# importar funcionalidades de un modulo (suma es una funcion)


from calculadora import suma
from calculadora import resta
resultado = suma(30,45)
resultado1 = resta(30,4)
pass#print(resultado)

