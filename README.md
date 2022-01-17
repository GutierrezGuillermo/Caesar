# Caesar
Cifrado César/Caesar's cipher.

Cifrado César implementado en Python v3.0. Otro sistema criptográfico de la Antigüedad (y por tanto obsoleto) pero que sirve como divertimento y para aplicar conceptos básicos. 

En esencia el cifrado consiste en tomar una letra del alfabeto, por ejemplo B, y "girarla" o desplazarla hacia la derecha tantas veces como indique la clave numérica. O expresado matemáticamente: f(x) = (x+n) mod26, donde x es el mensaje a transmitir, n es la clave o número de veces que debemos desplazar cada letra y mod26 indica que debemos aplicar aritmética modular para esto, ya que obviamente el alfabeto (27 en el español, 26 en el inglés) tiene un número limitado de caracteres, por lo que debemos "dar la vuelta" como si fuera las horas en un reloj. Así, si dividimos el resultado de x+n entre 26, nos interesa el RESTO, que va a ser finalmente el numero que usemos para la rotación.

So, this cipher is really basic, but it can be used to better understand functions and basic criptography. 

What the program does is taking a letter, and "shift" to the right as many times as the numeric key says. Expressed as formula : f(x) = (x+n) mod26, where x is the message, n is the numeric key (i.e how many times you should shift the letter in the alphabet) and mod26 means we must "wrap around" the result.  So,  we have a finite number of characters and we can't assing just any value to a character. Ex in english alphabet there are 26 letters, so a = 33 makes no sense. Instead, using modulus we can wrap around and get a result that is within our table of letters. 
