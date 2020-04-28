nomFitxer = input("Entra el nom de l'arxiu que vols analitzar")
print("Gràcies!")
Fitxer = open("noticies/"+nomFitxer+".txt")
#Exercici2
def comptarParaules(text):
  paraules = 0
  for lletra in nomFitxer:
    if nomFitxer[lletra]+1 == " ":
      paraules = paraules + 1
  return paraules
  #TODO Heu de retornar el nombre de paraules que té un text
  #Com podeu detectar una paraula, que el separa les paraules?

def comptarFrases(text):
  frases = 0
  for lletra in nomFitxer:
    if nomFitxer[lletra] == ".":
      frases = frases + 1
  return frases
  #TODO Heu de retornar el nombre de frases. 
  #Com es separen les frases?

def mitjanaParaulesPerFrase(text):
  paraules = 0
  for lletra in nomFitxer:
    if nomFitxer[lletra]+1 == " ":
      paraules = paraules + 1
  frases = 0
  for lletra in nomFitxer:
    if nomFitxer[lletra] == ".":
      frases = frases + 1
  mitjana = paraules / frases
  return mitjana
    
  #TODO Heu de retornar la mitjana de paraules per frases?

#Exercici 3
def numeroParulesComplexes(text):
  paraulesComplexes = 0
  for lletra in nomFitxer:
    if lletra == " ":
      if nomFitxer[lletra]+5 != " ":
        paraulesComplexes = paraulesComplexes+1
  #TODO Heu de retornar el nombre de paraules complexes que té el text
  #Són aquelles que tenen més de cinc lletres

def percetantgeParaulesComplexes(text):
  percentatgeParaulesComplexes = 0
  for lletra in nomFitxer:
    if lletra == " ":
      if nomFitxer[lletra]+5 != " ":
        paraulesComplexes = paraulesComplexes+1
  paraules = 0
  for lletra in nomFitxer:
    if nomFitxer[lletra]+1 == " ":
      paraules = paraules + 1
  percentatgeParaulesComplexes = paraules / paraulesComplexes * 100
  return percentatgeParaulesComplexes

#TODO Fer-ho al final de tot el 5.
#Exericic 5 llegir configuració

#Exercici 1


#TODO heu de completar el codi perquè la variable text tingui el contingut del fitxer

text = nomFitxer

#Per provar exercici 2 i 3 podeu posar-vos print aquíí per comprovar si es compta béé paraules, si compta frases, si es fa la mitja i si es detecten les complexes.
print(paraules)
print(frases)
print(paraulesComplexes)
print(percentatgeParaulesComplexes)
#Exercici 4
#càlcul de la fórmula

#TODO  Pinteu index per pantalla 
index = 

#TODO Classifiqueu exercici segons índex
# Digueu com és el text seguint la taula https://en.wikipedia.org/wiki/Gunning_fog_inde

#TODO
#Heu de tancar el fitxer


