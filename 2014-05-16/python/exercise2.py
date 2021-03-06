from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, 'C:/Users/Valentina/lar-cc/lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import vertexSieve
from sysml import *
from architectural import *
from myfont import *
from splines import *

''' ***************************ESERCIZIO 1********************************* '''
master = assemblyDiagramInit([9,9,4])([[.3,3,.3,2,.3,4,.3,2,.3],[.3,3,.3,2,.3,1,.3,3,.3],[0.2,1,1,0.2]])
copertura = master

'''rimuovo le celle per definire la struttura complessiva '''
toRemove = [254,255,290,291,294,295,257,258,259,294,295,262,263,264,265,298,299,262,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,
			300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)

''' Aggiungo le porte '''
toMerge = 77
door = assemblyDiagramInit([1,3,2])([[.3],[2,1,2],[1.8,.3]])
door2 = assemblyDiagramInit([1,3,2])([[.3],[2,1,2],[0.2,0.3]])
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
toMerge =83
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
toMerge = 89
doorpic = assemblyDiagramInit([1,3,2])([[.3],[0.5,1.5,0.5],[1.8,.3]])
door2pic = assemblyDiagramInit([1,3,2])([[.3],[0.5,1.5,0.5],[0.2,0.3]])
master = diagram2cell(doorpic,master,toMerge)
master = diagram2cell(door2pic,master,toMerge)
toMerge = 159 
master = diagram2cell(doorpic,master,toMerge)
master = diagram2cell(door2pic,master,toMerge)
toMerge = 143
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
toMerge = 211
master = diagram2cell(door,master,toMerge)
master = diagram2cell(door2,master,toMerge)
door2 = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[.3],[1.8,.3]])
door2a = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[0.3],[0.2,0.3]])
toMerge=103
master = diagram2cell(door2,master,toMerge)
master = diagram2cell(door2a,master,toMerge)
toMerge=125
master = diagram2cell(door2,master,toMerge)
master = diagram2cell(door2a,master,toMerge)

''' aggiungo le finestre '''
toMerge = 168
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 38
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 198
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 69
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 130
finestra = assemblyDiagramInit([5,1,3])([[1.5,0.9,.2,.9,1.5],[.3],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)

toMerge = 14
finestra = assemblyDiagramInit([1,5,3])([[.3],[1.5,0.9,.2,.9,1.5],[1,1.4,.3]])
master = diagram2cell(finestra,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,0.5)
#VIEW(hpc)
'''elimino muri di troppo e le celle contenenti finestre e porte,lascio il tetto '''
toRemove =[166,167,170,171,172,174,175,183,182,186,187,188,190,191,102,103,106,107,108,110,111,114,115,116,118,119,124,125,39,40,47,48,55,56,59,60,61,63,64
			,303,304,309,377,371,401,407,386,392,416,422,321,315,316,341,347,291,292,297,315,316,321,243,244,249,255,256,261,267,268,273,327,328,333,279,280,285,356,362]
appartamentocontetto = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(appartamentocontetto)))
hpc = cellNumbering (appartamentocontetto,hpc)(range(len(appartamentocontetto[1])),CYAN,0.5)
#VIEW(hpc)
toRemove = [141,144,150,153,91,94,97,101,39,45,51,54,386,392]
strutturasenzatetto = appartamentocontetto[0], [cell for k,cell in enumerate(appartamentocontetto[1]) if not (k in toRemove)]
#VIEW(STRUCT(MKPOLS(appartamentosenzatetto)))

'''*******************************ESERCIZIO 2 **************************************'''

'''Realizzo l'ingresso in cui si accede all'edificio '''
ingresso =assemblyDiagramInit([3,3,3])([[0.3,2,0.3],[0.3,4,0.3],[0.2,2,0.2]])
toRemove = [13]
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
ingressosenzaporta = ingresso

'''CREO LA PORTA PER L'INGRESSO'''
toMerge = 21
door = assemblyDiagramInit([1,3,2])([[.2],[0.5,0.8,0.4],[1.8,.5]])
ingresso = diagram2cell(door,ingresso,toMerge)
toRemove = [27]
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]

'''creo la porta verso l'appartamento'''
toMerge = 15
door = assemblyDiagramInit([3,1,2])([[0.5,0.8,0.5],[.3],[1.8,.5]])
ingresso = diagram2cell(door,ingresso,toMerge)
ingressosenzaporta = diagram2cell(door,ingressosenzaporta,toMerge)
toRemove = [31]
toRemove2 = [27] #per senza porta
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
ingressosenzaporta = ingressosenzaporta[0], [cell for k,cell in enumerate(ingressosenzaporta[1]) if not (k in toRemove2)]
ingressosenzaportasenzascale = ingressosenzaporta

'''creo lo spazio per le scale nel pavimento superiore'''
vuoto = assemblyDiagramInit([3,3,3])([[0.1,1,0.3],[0.4,0.8,0.5],[0.2,2,0.2]])
toMerge = 13
ingresso = diagram2cell(vuoto,ingresso,toMerge)
ingressosenzaporta = diagram2cell(vuoto,ingressosenzaporta,toMerge)
toRemove = [45,46,47]
toRemove2 = [41,42,43]
ingresso = ingresso[0], [cell for k,cell in enumerate(ingresso[1]) if not (k in toRemove)]
ingressosenzaporta = ingressosenzaporta[0], [cell for k,cell in enumerate(ingressosenzaporta[1]) if not (k in toRemove2)]

toMerge = 12
ingressosenzaporta = diagram2cell(vuoto,ingressosenzaporta,toMerge)
toRemove = [64,65,66]
ingressosenzaporta = ingressosenzaporta[0], [cell for k,cell in enumerate(ingressosenzaporta[1]) if not (k in toRemove)]

V = [[3.8,-3.2,0],[4.8,-3.2,0],[4.8,-2.7,0],[3.8,-2.7,0],
	[3.8,-3.2,0.4],[4.8,-3.2,0.4],[4.8,-2.7,0.4],[3.8,-2.7,0.4]]
FV = [[0,1,2,3,4,5,6,7]]
a = V,FV
scala = Struct([a,larApply(t(0,0.2,0.3))(a),larApply(t(0,0.4,0.6))(a),larApply(t(0,0.6,0.9))(a),larApply(t(0,0.8,1.2))(a),
	larApply(t(0,1,1.5))(a),larApply(t(0,1.2,1.8))(a),larApply(t(0,1.4,2))(a)])

ingresso = larApply(t(3.3,-4.5,0))(ingresso)
ingresso = Struct([ingresso])
ingresso = AA(MKPOLS)(ingresso) + AA(MKPOLS)(scala) 
strutturasenzatetto = Struct([strutturasenzatetto])
ingressosenzaporta = larApply(t(3.3,-4.5,0))(ingressosenzaporta)
ingressosenzaporta = Struct([ingressosenzaporta])
ingressosenzaportasenzascale = ingressosenzaporta
ingressosenzaporta = AA(MKPOLS)(ingressosenzaporta)+ AA(MKPOLS)(scala)

strutturasenzaportasenzascale = AA(MKPOLS)(strutturasenzatetto) + AA(MKPOLS)(ingressosenzaportasenzascale)
struttura = AA(MKPOLS)(strutturasenzatetto) + ingresso
strutturasenzaporta = ingressosenzaporta + AA(MKPOLS)(strutturasenzatetto)
strutturasenzaporta =STRUCT(CAT(strutturasenzaporta))
appartamento = STRUCT(CAT(struttura)) #primo piani
appartamento2 = T(3)(2.4)(strutturasenzaporta) #secondo piano
appartamento3 = T(3)(4.8)(strutturasenzaporta) #terzo piano
strutturasenzaportasenzascale = STRUCT(CAT(strutturasenzaportasenzascale)) #quarto piano
appartamento4 = T(3)(7.2)(strutturasenzaportasenzascale)
copertura = assemblyDiagramInit([1,1,1])([[10.2],[10.5],[1]])
copertura = T(3)(9.6)(STRUCT(MKPOLS(copertura)))
copertura2 = assemblyDiagramInit([1,1,1])([[2.6],[4.5],[0.2]])
copertura2 = T([1,2,3])([3.3,-4.5,9.6])(STRUCT(MKPOLS(copertura2)))
palazzo = STRUCT([appartamento,appartamento2,appartamento3,appartamento4,copertura,copertura2])

palazzo2 = T([1,2])([12,5])(palazzo)
palazzo2 = R([1,2])(-PI/6)(palazzo2)
palazzo3 = T([1,2])([12,5])(palazzo)
palazzo3 = T([1,2])([16,3])(R([1,2])(-PI/2)(palazzo3))
#VIEW(STRUCT([palazzo,palazzo2,palazzo3]))


lardom1 =larIntervals([32])([1])
dom1 = INTERVALS(1)(20)
dom2 = PROD([dom1,dom1])
a = BEZIER(S1)([[0.52, 5.96], [0.6, 8.64], [2.23, 11.53], [6.44, 11.49]])
b = BEZIER(S1)([[6.44, 11.49], [8.96, 11.43], [11.88, 8.88], [11.45, 5.48]])
c = BEZIER(S1)([[11.45, 5.48], [11.41, 3.41], [9.49, 0.43], [5.72, 0.5]])
d = BEZIER(S1)([[5.72, 0.5], [3.62, 0.51], [0.53, 2.37], [0.52, 5.96]])
obj1 = MAP(a)(dom1)
obj2 = MAP(b)(dom1)
obj3 = MAP(c)(dom1)
obj4 = MAP(d)(dom1)
prato = COLOR(GREEN)(SOLIDIFY(STRUCT([obj1,obj2,obj3,obj4])))
prato = T([1,2])([-20,-40])(S([1,2])([5,5])(prato))
#VIEW(STRUCT([palazzo,palazzo2,palazzo3,prato]))


#realizzo le macchine parcheggiate..
domain = INTERVALS(1)(30)
xy1 = BEZIER(S1)([[0.29, 0.46], [0.01, 1.44], [0.25, 1.82], [1.7, 2.1]])
xy2 = BEZIER(S1)([[1.7, 2.1], [3.51, 2.95], [3.78, 3.44], [6.87, 2.92]])
xy3 = BEZIER(S1)([[6.87, 2.92], [7.59, 2.04], [7.93, 0.87], [7.29, 0.63]])
xy4 = BEZIER(S1)([[0.29, 0.46], [1, 0.47], [1.01, 0.46], [1.01, 0.52]])
xy5 = BEZIER(S1)([[2.42, 0.52], [2.57, 1.68], [0.95, 1.84], [1, 0.52]])
xy6 = BEZIER(S1)([[2.42, 0.52], [5.66, 0.54], [2.42, 0.53], [5.69, 0.54]])
xy7 = BEZIER(S1)([[7.15, 0.68], [7.19, 1.51],[5.78, 1.96], [5.69, 0.54]])
xy8 = BEZIER(S1)([[7.15, 0.68], [7.18, 0.64], [7.29, 0.63]])

aaa = STRUCT([MAP(xy1)(domain),MAP(xy2)(domain),MAP(xy3)(domain),MAP(xy4)(domain),MAP(xy5)(domain),MAP(xy6)(domain),MAP(xy7)(domain),MAP(xy8)(domain)])
AAA = SOLIDIFY(aaa)
modello = PROD([AAA,Q(3)])
def ruota():
    cyG = CYLINDER([0.6,0.5])(100)
    cyP = CYLINDER([0.4,0.5])(100)
    r = DIFF([cyG,cyP])
    return R([1,2])(PI/4)(r)

r1 =COLOR(BLACK)(T([1,2])([1.7,0.8])(ruota()))
r2 = COLOR(BLACK)(T([1,2])([6.5,0.8])(ruota()))
r3 =COLOR(BLACK)(T([1,2,3])([1.7,0.8,2.5])(ruota()))
r4 = COLOR(BLACK)(T([1,2,3])([6.5,0.8,2.5])(ruota()))
f1= BEZIER(S1)([[2.26, 1.9], [3.05, 2.65], [3.78, 2.98], [5.01, 2.93]])
f2= BEZIER(S1)([[5.02, 2.93], [5, 2.84], [4.91, 2.07], [4.91, 2.14]])
f3= BEZIER(S1)([[4.91, 2.14], [4.43, 2.05], [3, 1.87], [2.26, 1.9]])

finestrino = STRUCT([MAP(f1)(domain),MAP(f2)(domain),MAP(f3)(domain)])
FIN = COLOR(BLUE)(SOLIDIFY(finestrino))
FIN2 = COLOR(BLUE)(T(3)(3)(FIN))
APP = COLOR(RED)(STRUCT([modello,r1,r2,r3,r4]))
APP2 =COLOR(YELLOW)(STRUCT([modello,r1,r2,r3,r4]))
car = R([2,3])(PI/2)(STRUCT([FIN,FIN2,APP]))
car2 = R([2,3])(PI/2)(STRUCT([FIN,FIN2,APP2]))
car = T([1,2,3])([10,-16,-0.25])(car)
car2 = T([1,2,3])([10,-16,-0.25])(car2)
car = S([1,2,3])([0.5,0.5,0.5])(car)
car2 = S([1,2,3])([0.5,0.5,0.5])(car2)
car2 = T([1,2])([10,-10])(car2)
#modelloFIN = COLOR(RED)(PROD([FIN,Q(0.5)]))

VIEW(STRUCT([palazzo,palazzo2,palazzo3,prato,car,car2]))
