import string

def encrypte_aux(lettre,cle,c):
    etape1 = (ord(lettre)-ord(c)+cle)%26
    etape2 = etape1+ord(c)
    return chr(etape2)

def encrypte_lettre(lettre, cle):
  """
  >>> encrypte_lettre('a',10), encrypte_lettre('a',26)
  ('k', 'a')
  >>> encrypte_lettre('z',1), encrypte_lettre('a',260)
  ('a', 'a')
  >>> encrypte_lettre('A',10), encrypte_lettre('A',26)
  ('K', 'A')
  >>> encrypte_lettre('w',10), encrypte_lettre('W',10)
  ('g', 'G')
  """

  if not lettre.isalpha():
    return lettre
  if lettre.islower():
    return encrypte_aux(lettre,cle,'a')
  return encrypte_aux(lettre,cle,'A')
    

def encrypte(en_clair, cle):
  """
  >>> encrypte(string.ascii_lowercase,10)
  'klmnopqrstuvwxyzabcdefghij'
  >>> encrypte(string.ascii_uppercase,100)
  'WXYZABCDEFGHIJKLMNOPQRSTUV'
  >>> encrypte('Toto est une girafe, avec des petites jambes.',12)
  'Fafa qef gzq sudmrq, mhqo pqe bqfufqe vmynqe.'
  """
  chaine_crypte = str()
  for lettres in en_clair:
    chaine_crypte += encrypte_lettre(lettres,cle)
  return chaine_crypte


def decrypte(texte_cache, cle):
  """
  >>> cle = 12
  >>> decrypte(encrypte(string.ascii_lowercase,cle),cle) == string.ascii_lowercase
  True
  >>> decrypte(encrypte(string.ascii_uppercase,cle),cle) == string.ascii_uppercase
  True
  >>> decrypte('Fafa qef gzq sudmrq, mhqo pqe bqfufqe vmynqe.',12)
  'Toto est une girafe, avec des petites jambes.'
  """
  return encrypte(texte_cache,26-cle)


def devine_cle(texte_cache):
  """
  >>> devine_cle('a e dd e eeee d')
  0
  >>> devine_cle('x b aa b bbbb a')
  23
  """
  lst = []
  for i in range(0,26):
    compteur = decrypte(texte_cache,i).count('e')
    lst.append(compteur)
  return lst.index(max(lst))


    
def devine_cle2(texte_cache):
  """
  >>> devine_cle2('a e dd e eeee d')
  0
  >>> devine_cle2('x b aa b bbbb a')
  23
  """
  return devine_cle(texte_cache)    #C'est pour ledoctest
  
def encrypte_mieux(texte, cle):
  """
  >>> encrypte_mieux('abc de f ghijk lmnopqrstuvw xyz',3)
  'def hi k mnopq stuvwxyzabcd fgh'
  >>> encrypte_mieux('Toto est une girafe, avec des petites jambes.', 3)
  'Wrwr iwx zsj moxglk, hclj lma yncrcnb tkwloc.'
  """
  mot = ""
  cle2 = cle
  for i in range(len(texte)):
    mot += encrypte_lettre(texte[i],cle2)
    if texte[i] == " ":
      cle2 += 1
  return mot

 
def decrypte_mieux(texte, cle):
  """
  >>> decrypte_mieux('def hi k mnopq stuvwxyzabcd fgh',3)
  'abc de f ghijk lmnopqrstuvw xyz'
  >>> decrypte_mieux('Wrwr iwx zsj moxglk, hclj lma yncrcnb tkwloc.',3)  
  'Toto est une girafe, avec des petites jambes.'
  """
  mot = ""
  cle2 = cle
  for i in range(len(texte)):
    mot += encrypte_lettre(texte[i],26-cle2)
    if texte[i] == " ":
      cle2 += 1
  return mot
   
def encrypte_encore_mieux(texte, cle, decal):
  """
  >>> encrypte_encore_mieux('abc de f ghijk lmnopqrstuvw xyz',3,7)
  'def no w efghi qrstuvwxyzab jkl'
  >>> encrypte_encore_mieux('Toto est une girafe, avec des petites jambes.',3,7)
  'Wrwr ocd lev egpydc, fajh pqe ixmbmxl jambes.'
  """
  mot = ""
  cle2 = cle
  for i in range(len(texte)):
    mot += encrypte_lettre(texte[i],cle2)
    if texte[i] == " ":
      cle2 += decal
  return mot
 
def decrypte_encore_mieux(texte, cle, decal):
  """
  >>> decrypte_encore_mieux('def no w efghi qrstuvwxyzab jkl',3,7)
  'abc de f ghijk lmnopqrstuvw xyz'
  >>> decrypte_encore_mieux('Wrwr ocd lev egpydc, fajh pqe ixmbmxl jambes.',3,7)
  'Toto est une girafe, avec des petites jambes.'
  """
  mot = ""
  cle2 = cle
  for i in range(len(texte)):
    mot += encrypte_lettre(texte[i],26-cle2)
    if texte[i] == " ":
      cle2 += decal
  return mot

     

if __name__ == '__main__':
  import doctest
  doctest.testmod()

  premier_essai = """Cdzm, e'vd hvibz piz kjhhz. 
  Vkmzn, e'vd zp yzn cvggpxdivodjin, kgzdi y'cvggpxdivodjin. 
  Ez qjtvdn yzn zgzkcvion, yzn gdxjmizn zo yzn kviyvn. Zo dgn zovdzio mjnzn, ojpn mjnzn.
  """    
      
  deuxieme_essai = """Jli c'rsrkkrek ul mrjzjkrj, le rezdrc rl kyfiro zeuzxf, r c'rzxlzccfe jrwire, ez le trwriu, 
  ez le tyriretfe, drzj gclkfk le rikzjfe, j'rmretrzk, kirzerek le size u'rcwr. 
  Zc j'rggiftyr, mflcrek c'rgcrkzi u'le tflg mzw, drzj c'rezdrc gizk jfe mfc, uzjgrirzjjrek 
  urej cr elzk rmrek hl'zc rzk gl c'rjjrzcczi.
  """    
  print(decrypte(premier_essai,devine_cle(premier_essai)))     