#Exercici2
def comptarParaules(text):
  paraules = text.split()
  nombreParaules = 0
  for paraula in paraules:
     nombreParaules = nombreParaules+1
  return nombreParaules
  #TODO Heu de retornar el nombre de paraules que té un text
  #Com podeu detectar una paraula, que el separa les paraules?

def comptarFrases(text):
  frases = text.split(".")
  nombreFrases = 0
  for frase in frases:
    nombreFrases = nombreFrases+1
  return nombreFrases
  #TODO Heu de retornar el nombre de frases. 
  #Com es separen les frases?

def mitjanaParaulesPerFrase(text):
  paraules = 0
  mitjana = comptarParaules(text) / comptarFrases(text)
  return mitjana
    
  #TODO Heu de retornar la mitjana de paraules per frases?

#Exercici 3
def numeroParaulesComplexes(text):
  paraulesComplexes = 0
  paraules = text.split()
  for paraula in paraules:
    if len(paraula) >= 5:
      paraulesComplexes = paraulesComplexes+1
  return paraulesComplexes
  #TODO Heu de retornar el nombre de paraules complexes que té el text
  #Són aquelles que tenen més de cinc lletres

def percetantgeParaulesComplexes(text):
  mitjanaComplexes = numeroParaulesComplexes(text) / comptarParaules(text) * 100
  return mitjanaComplexes

#TODO Fer-ho al final de tot el 5.
#Exericic 5 llegir configuració

#Exercici 1

mitjanaComplexes = 0
#TODO heu de completar el codi perquè la variable text tingui el contingut del fitxer

nomFitxer = input("Entra el nom de l'arxiu que vols analitzar")
print("Gràcies!")
Fitxer = open("noticies/"+nomFitxer+".txt","r")
contingut = Fitxer.read()

#Per provar exercici 2 i 3 podeu posar-vos print aquíí per comprovar si es compta béé paraules, si compta frases, si es fa la mitja i si es detecten les complexes.
print(comptarParaules(contingut))
print(comptarFrases(contingut))
print(mitjanaParaulesPerFrase(contingut))
print(percetantgeParaulesComplexes(contingut))
print(numeroParaulesComplexes(contingut))
#Exercici 4
#càlcul de la fórmula

#TODO  Pinteu index per pantalla 
Index = (0.4*comptarParaules(contingut)/comptarFrases(contingut))+(100*numeroParaulesComplexes(contingut)/comptarParaules(contingut))
print(Index)
#TODO Classifiqueu exercici segons índex
# Digueu com és el text seguint la taula https://en.wikipedia.org/wiki/Gunning_fog_inde
#TODO
#Heu de tancar el fitxer
Fitxer.close()