## Challengue 01 ###

"""
Enunciado: Crea una función que sea capaz de encriptar y desencriptar texto utilizando el
algoritmo de encriptación de Karaca (debes buscar información sobre él).
"""

"""
Informacion adicional:

Algoritmo de encriptacion de Karaca:

1. Reverse the input.
2. Replace all vowels with the following rules: a: 0, e: 1, i: 2, o:3, u:4
3. Add "aca" to the end of the word.

"""
#hola: aloh---1l4h
#william: mailliw--m13ll3w

import re

vocals=["a","e","i","o","u"]
numbers=[]
word=input("Ingresa la palabra: ")
word=word[::-1]
word_2=""
n=0
vocals_found=[]
#vocals_found=re.findall("[aeiou].",word)

for letter in word:
    if letter in vocals:
        vocals_found.append(letter)


for x in vocals_found:
    if x in vocals:
        numbers.append(vocals.index(x)+1)


for letter in word:
    if letter in vocals:
        word_2+=str(numbers[n])
        n+=1
        continue
    word_2+=letter

print(word_2)

