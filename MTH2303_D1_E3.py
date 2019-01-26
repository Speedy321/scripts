#Christophe-André Gassmann [1906846]

#Trying to generate all possibilities of odd numbers of <1> up to x
#knowing we have Results:{<1>,<0>}, for x dices where P[xi=<1>] = ai = 1/(2i+1)
import itertools
from fractions import Fraction
from decimal import Decimal

#Génere une liste de toutes les permutations uniques de la liste en entrée.
# ex: si <t=[1,0,0]> la fonction retourne la liste: <[[1,0,0],[0,1,0],[0,0,1]]>
def unique_permutations(t):
    lt = list(t)
    lnt = len(lt)
    if lnt == 1:
        yield lt
    st = set(t)
    for d in st:
        lt.remove(d)
        for perm in unique_permutations(lt):
            yield [d]+perm
        lt.append(d)

#Génere une liste de toutes les possibilitées pour <n=x> d'avoir un nombre impaire de <1> dans <x> "cases".
# On génere, à chaque nombre impaire entre <i=1> et <i=x>, une liste de <x> "cases" 
#   qui contiend <i> cases avec des <1> et le reste <x-i> cases avec des <0>.
#   Puis on donne cette liste à "unique_permutations()" qui nous retourne toutes les permutations uniques de la dite liste.
# Enfin on assemble toutes les listes pour chaque <i> impaire en une grande liste qui représente toutes les possibilitées 
#   pour que si <n=x> on aie un nombre impaire de <1>.
def generateNx(x):
    nx = list()
    for i in range(1, x+1, 2):
        nxlocal = []
        for ii in range(0, i):
            nxlocal += [1]
        for ii in range(i, x):
            nxlocal += [0]
        #print(nxlocal)
        nx+=list(unique_permutations(nxlocal))
    #print(nx)
    return nx

#Calcule la probabilité que la liste <X> existe.
#
#Soit, si <X=[[1,0,0],[0,1,0],[0,0,1],[1,1,1]]=[A,B,C,D]> pour <n=4>
# la fonction calcule <P[A U B U C U D]=P[A]+P[B]+P[C]+P[D]-(xx)>
# où <(xx)> est combosé de combinaisons d'intersections entre <A>, <B>, <C> et <D>
# et ne peut que <= 0> car <A>, <B>, <C> et <D> sont incompatibles.
#De plus, si <alpha.i> est la probabilité d'avoir un <1> dépandant de <i>:
#   alors P[A]= (alpha.i=1)     *(1-alpha.i=2)  *(1-alpha.i=3),
#         P[B]= (1-aplha.i=1)   *(alpha.i=2)    *(1-alpha.i=3),
#         P[C]= (1-aplha.i=1)   *(1-alpha.i=2)  *(alpha.i=3),  
#      et P[D]= (aplha.i=1)     *(alpha.i=2)    *(alpha.i=3),
#  Soit <xi> dans <[x1,x2,x3]> où <x1> est à la position <i=1>, <x2> à <i=2>, etc.
#   si <xi=1> alors <P[xi] = alpha.i> et sinon <xi=0> et <P[xi] = (1-alpha.i)>
# On multiplie les <P[xi]> au sein d'un même block (ex:<P[A]>) et on additionne les blocs (ex:<P[A]+P[B]>)
def calculateProb(X):
    lnx = len(X)
    n = len(X[0])
    prob = Fraction(0, 1)
    for elem in X:
        localProb=Fraction(1, 1)
        for i in range(n):
            if(elem[i]==1):
                localProb*=Fraction(1, (2*(i+1)+1))
                #print(Fraction(1, (2*(i+1)+1)))
            elif(elem[i]==0):
                localProb*=(1-Fraction(1, (2*(i+1)+1)))
                #print(1-Fraction(1, (2*(i+1)+1)))
        prob+=localProb

    print("P[n"+str(n)+"]: "+str(prob))
    return prob

#Tests avec dataset fait à la main.
#(Tentatives originales, non-automatisées)
n1 = list(unique_permutations([1]))
print(n1)

n2 = list(unique_permutations([1,0]))
print(n2)
print("n2:"+str(len(n2)))

n3 = list(unique_permutations([1,0,0]))+list(unique_permutations([1,1,1]))
print(n3)
print("n3:"+str(len(n3)))

n4 = list(unique_permutations([1,0,0,0]))+list(unique_permutations([1,1,1,0]))
print(n4)
print("n4:"+str(len(n4)))

n5 = list(unique_permutations([1,0,0,0,0]))+list(unique_permutations([1,1,1,0,0]))+list(unique_permutations([1,1,1,1,1]))
print(n5)
print("n5:"+str(len(n5)))

n6 = list(unique_permutations([1,0,0,0,0,0]))+list(unique_permutations([1,1,1,0,0,0]))+list(unique_permutations([1,1,1,1,1,0]))
#print(n6)
#print("n6:"+str(len(n6)))

n7 = list(unique_permutations([1,0,0,0,0,0,0]))+list(unique_permutations([1,1,1,0,0,0,0]))+list(unique_permutations([1,1,1,1,1,0,0]))+list(unique_permutations([1,1,1,1,1,1,1]))

n8 = list(unique_permutations([1,0,0,0,0,0,0,0]))+list(unique_permutations([1,1,1,0,0,0,0,0]))+list(unique_permutations([1,1,1,1,1,0,0,0]))+list(unique_permutations([1,1,1,1,1,1,1,0]))

n9 = list(unique_permutations([1,0,0,0,0,0,0,0,0]))+list(unique_permutations([1,1,1,0,0,0,0,0,0]))+list(unique_permutations([1,1,1,1,1,0,0,0,0]))+list(unique_permutations([1,1,1,1,1,1,1,0,0]))+list(unique_permutations([1,1,1,1,1,1,1,1,1]))

print("--")
calculateProb(n1)
calculateProb(n2)
calculateProb(n3)
calculateProb(n4)
calculateProb(n5)
calculateProb(n6)
calculateProb(n7)
calculateProb(n8)
calculateProb(n9)

print("******")
#Tests avec les datasets automatic, de <n=1> à <n=x>, soit <n=30> dans la boucle suivante.
#
#Attention, l'algorithme prend exponentiellement plus de ressources plus <n> augmente, 
# l'environement d'execution de python par default ne donne la mémoire que pour se rendre a <n=25>, 
# et ce après plusieurs heures d'execution, mais les fonctions peuvent théoriquement calculer 
# pour n'importe quel <n> tant que la machine qui fait le calcule dispose des ressource nécessaires.
for k in range(1,30,1):
    nk = generateNx(k)
    calculateProb(nk)

