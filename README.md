# Caesar
Cifrado César/Caesar's cipher.

Cifrado César implementado en Python v3.0. Otro sistema criptográfico de la Antigüedad (y por tanto obsoleto) pero que sirve como divertimento y para aplicar conceptos básicos. 

En esencia el cifrado consiste en tomar una letra del alfabeto, por ejemplo B, y "girarla" o desplazarla hacia la derecha tantas veces como indique la clave numérica. O expresado matemáticamente: f(x) = (x+n) mod26, donde x es el mensaje a transmitir, n es la clave o número de veces que debemos desplazar cada letra y mod26 indica que debemos aplicar aritmética modular para esto, ya que obviamente el alfabeto (27 en el español, 26 en el inglés) tiene un número limitado de caracteres, por lo que debemos "dar la vuelta" como si fuera las horas en un reloj. Así, si dividimos el resultado de x+n entre 26, nos interesa el RESTO, que va a ser finalmente el numero que usemos para la rotación.
