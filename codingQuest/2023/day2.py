from utility import *

### Dato che devo effettuare molte conversioni e deconversioni, una tipica pratica che si utilizza è quella di considerare gli elementi come stringhe
### questa pratica è poco efficente ma la dimensione del problema è tale da rispondere perfettamente alle nostre esigenze

### Ho quindi creato due funzioni per convertire e deconvertire i decimali in binario, nello specifico la funzione di conversione binaria viene paddata per avere sempre 16 bit espliciti



# print(fromIntegerToBinary('255'))



# print(fromBinaryToInteger('100000000'))

def isParity(binary):
  countOnes=0
  for element in binary:
    if (element=='1'):
      countOnes=countOnes+1
  return countOnes%2==0


def solve():
  rows= openFile("input.txt")

  filteredElements=[]

  for row in rows:
    binaryRow=fromIntegerToBinary(row)
    if(isParity(binaryRow)):
      filteredElements.append(binaryRow)

  # print(filteredElements)

  # Filtro monolinea sfruttando la list comprehension di python
  # filteredElementsInteger=[fromBinaryToInteger(x[1:]) for x in filteredElements]

  filteredElementsInteger=[]

  for element in filteredElements:
    filteredElementsInteger.append(fromBinaryToInteger(element[1:]))
  
  # print(filteredElementsInteger)

  sumOfValues=0
  for element in filteredElementsInteger:
    sumOfValues=sumOfValues+int(element)

  return(round(sumOfValues/len(filteredElementsInteger)))

print(solve())