from reinomonera import monera
from reinofungi import fungi
from reinoanimal import animal
from reinoprotista import protista
from reinomonera import monera
from reinovegetal import vegetal
from especie import especies
listareinos = []
listaespefungi = []
listaespeanimal = []
listaespemonera = []
listaespeprotista = []
listaespevegetal = []


def reinos():
    print("Estos son los reinos en los que se dividen los seres vivos ")
    print("Reino Animal")
    print("*")
    print("Reino Vegetal")
    print("*")
    print("Reino Fungi")
    print("*")
    print("Reino Protoctista")
    print("*")
    print("Reino Monera")
    menu()


def selreino():
    mireinoanimal = animal('pluricelulares', 'eucariotas', 'alimentación=heterótrofa',
                           'respiración=aeróbica', 'reproducción=sexual', 'capacidad des plazamiento')
    listareinos.append(mireinoanimal)

    mireinofungi = fungi('pluricelulares', 'aerobios', 'eucariotas',
                         'alimentacion=heterótrofos', 'reproducen mediante esporas')
    listareinos.append(mireinofungi)

    mireinomonera = monera(' heterotrofas', 'aerobias')
    listareinos.append(mireinomonera)

    mireinoprotista = protista('procariotas', 'unicelulares')
    listareinos.append(mireinoprotista)

    mireinovegetal = vegetal('naturaleza=inmóvil', 'pluricelular',
                             'eucariota', 'autótrofos', 'reproduccion=sexuala o asexual')
    listareinos.append(mireinovegetal)
    print("Seleccione el reino que desea conocer")
    print("1 - Reino Animal")
    print("*")
    print("2 - Reino Vegetal")
    print("*")
    print("3 - Reino Fungi")
    print("*")
    print("4 - Reino Protoctista")
    print("*")
    print("5 - Reino Monera")
    sel = int(input(":"))
    print("*")
    print("*")
    if sel == 1:
        mireinoanimal.PasaAcadena()
    elif sel == 2:
        mireinovegetal.pAsaacadena()
    elif sel == 3:
        mireinofungi.PasaacaDena()
    elif sel == 4:
        mireinoprotista.PasaaCadena()
    elif sel == 5:
        mireinomonera.PasaacadEna()
    else:
        print("opción invalida")
    menu()


def listaespecies():
    print("Reino Animal")
    print("*")
    print("Reino Vegetal")
    print("*")
    print("Reino Fungi")
    print("*")
    print("Reino Protoctista")
    print("*")
    print("Reino Monera")
    # reino fung
    listaespefungi.append("Ascomicetos")
    listaespefungi.append("Basidiomicetos")
    # reino vegetal
    listaespevegetal.append("Equisetos")
    listaespevegetal.append("Licopodios")
    listaespevegetal.append("Gimnospermas")
    listaespevegetal.append("Angiospermas")
    listaespevegetal.append("Helechos")
    listaespevegetal.append("Musgos")
    # reiono animal
    listaespeanimal.apped("Poríferos")
    listaespeanimal.apped("Cnidarios")
    listaespeanimal.apped("Plantelmintos")
    listaespeanimal.apped("Moluscos")
    listaespeanimal.apped("Anélidos")
    listaespeanimal.apped("Equinodermos")
    listaespeanimal.apped("Insectos")
    listaespeanimal.apped("Crustáceos")
    listaespeanimal.apped("Arácnidos")
    listaespeanimal.apped("Peces")
    listaespeanimal.apped("Anfibios")
    listaespeanimal.apped("Aves")
    listaespeanimal.apped("Reptiles")
    listaespeanimal.apped("Mamiferos")
    # reino monera
    
listaespecies()
    


def menu():
    print("**")
    print("**")
    print("**")
    print("seleccione la acción que desea realizar")

    print("1-  Listar los reinos en los que se clasifican los seres vivos")
    print("2-  Seleccionar reino")
    print("3-  Seleccionar cualquiera de los 5 reinos y listar las especies por la que está compuesto")
    print("4-  alimentación, respiración, reproducción y locomoción")

    opcion = int(input(":"))
    if opcion == 1:
        reinos()
    elif opcion == 2:
        selreino()
    elif opcion== 3:
        listaespecies()
        print("1 - Reino Animal")
        print("*")
        print("2 - Reino Vegetal")
        print("*")
        print("3 - Reino Fungi")
        print("*")
        print("4 - Reino Protoctista")
        print("*")
        print("5 - Reino Monera")
        print("*")
        print("*")
        print("Seleccione el reino que desea conocer las especies")
        sel = int(input(":"))
        if sel==1:
            for i in listaespeanimal:
                print(i)
        elif sel==2:
            for i in listaespevegetal:
                print(i)
        elif sel==3:
            for i in listaespefungi:
                print(i)
        elif sel==4:
            for i in listaespeprotista:
                print(i)
        elif sel==5:
            for i in listaespemonera:
                print(i)
        


menu()
