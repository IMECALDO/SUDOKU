def mostrar():
    for i in range (9):
        for y in range (9):
            if posibles_nums[i][y] == "":
                print("-",end="")
            else:
                print(posibles_nums[i][y],end="")
        print("")

def chido3X3():
    for i in range(3):
        if i == 0:
            count_ren = 0
        elif i == 1:
            count_ren = 3
        else:
            count_ren = 6
        count_col = 0
        for o in range (3):
            for a in range (3):
                for b in range(3):
                    if len(posibles_nums[a + count_ren][b + count_col]) != 1:
                        mover = posibles_nums[a + count_ren][b + count_col]
                        for c in range(3):
                            for d in range(3):
                                if c != a and d != b:
                                    if len(posibles_nums[c + count_ren][d + count_col]) is not 1:
                                        for e in range(len(posibles_nums[c + count_ren][d + count_col])):
                                            if posibles_nums[c + count_ren][d + count_col][e] in mover:
                                                mover.remove(posibles_nums[c + count_ren][d + count_col][e])
                        if len(mover) == 1:
                            posibles_nums[a + count_ren][b + count_col] = mover
        count_col = count_col + 3

def chido():
    for i in range(9):
            for y in range(9):
                if len(posibles_nums[i][y]) is not 1: 
                    for q in range(len(posibles_nums[i][y])):
                        count = 0
                        counter = 0 

                        # checar ren
                        for w in range(9):
                            if len(posibles_nums[i][w]) is not 1:
                                for r in range(len(posibles_nums[i][w])):
                                    if (posibles_nums[i][y][q]) == posibles_nums[i][w][r]:
                                        count = count + 1
                            elif posibles_nums[i][y][q] == posibles_nums[i][w][0]:
                                counter = counter + 1
                        # checar col     
                        for e in range(9):
                            if len(posibles_nums[e][y]) is not 1:
                                for r in range(len(posibles_nums[e][y])):
                                    if posibles_nums[i][y][q] == posibles_nums[e][y][r]:
                                        counter = counter + 1
                            elif posibles_nums[i][y][q] == posibles_nums[e][y][0]:
                                counter = counter + 1

                        if count == 1 or counter == 1:
                            n = []
                            n.append(posibles_nums[i][y][q])
                            posibles_nums[i][y] = n
                            valor = True
                            return()

def X3X3():
    d = []
    for i in range(3):
        if i == 0:
            count_ren = 0
        elif i == 1:
            count_ren = 3
        else:
            count_ren = 6
        count_col = 0
        for o in range (3):
            numeros = [1,2,3,4,5,6,7,8,9]
            f = []
            for a in range (3):
                for b in range(3):
                    if len(posibles_nums[a + count_ren][b + count_col]) == 1:
                        f.append(posibles_nums[a + count_ren][b + count_col])
                        if posibles_nums[a + count_ren][b + count_col][0] in numeros:
                            numeros.remove(posibles_nums[a + count_ren][b + count_col][0])
                    elif len(posibles_nums[a + count_ren][b + count_col]) is not 1:
                        for e in range(len(posibles_nums[a + count_ren][b + count_col])):
                            if posibles_nums[a + count_ren][b + count_col][e] in numeros:
                                numeros.remove(posibles_nums[a + count_ren][b + count_col][e])
            h = []
            for g in range (len(f)):
                if f[g] in h:
                    pass
                else:
                    h.append(f[g])
            if h != f or numeros != d:
                print("")
                mostrar()
                print("no yey")
                print(posibles_nums)
                exit()
            count_col = count_col + 3

def horizontal():
    d = []
    # que no se repitan y que esten todos
    for b in range(9):
        c = [1,2,3,4,5,6,7,8,9]
        f = []
        for a in range(9):
            if len(posibles_nums[a][b]) == 1:
                f.append(posibles_nums[a][b])
                if posibles_nums[a][b][0] in c:
                    c.remove(posibles_nums[a][b][0])
            elif len(posibles_nums[a][b]) is not 1:
                for e in range(len(posibles_nums[a][b])):
                    if posibles_nums[a][b][e] in c:
                        c.remove(posibles_nums[a][b][e])
        h = []
        for g in range (len(f)):
            if f[g] in h:
                pass
            else:
                h.append(f[g])
        if h != f or c != d:
            print("")
            mostrar()
            print("se jodió")
            print(posibles_nums)
            exit()

def vertical():
    global posibles_nums
    d = []
    # que no se repitan y que esten todos
    for a in range(9):
        c = [1,2,3,4,5,6,7,8,9]
        f = []
        for b in range(9):
            if len(posibles_nums[a][b]) == 1:
                f.append(posibles_nums[a][b])
                if posibles_nums[a][b][0] in c:
                    c.remove(posibles_nums[a][b][0])
            elif len(posibles_nums[a][b]) is not 1:
                for e in range(len(posibles_nums[a][b])):
                    if posibles_nums[a][b][e] in c:
                        c.remove(posibles_nums[a][b][e])
        h = []
        for g in range (len(f)):
            if f[g] in h:
                pass
            else:
                h.append(f[g])
        if h != f or c != d:
            print("")
            mostrar()
            print("se jodió")
            print(posibles_nums)
            exit()

def solucion_vertical():
    #checar verticalmente
    for i in range (9):
        for y in range (9):                       
            if len(posibles_nums[i][y]) != 1:
                num_remover = []
                for x in range (9):
                    # si uno en la col esta determinado
                    if len(posibles_nums[x][y]) == 1:
                        #checar si lo tiene en sus pos
                        for n in range (len(posibles_nums[i][y])):
                            # quitarlo si es que esta
                            if posibles_nums[i][y][n] == posibles_nums[x][y][0]:
                                num_remover.append(posibles_nums[i][y][n])  
                for e in num_remover:
                    if e in posibles_nums[i][y]:
                        posibles_nums[i][y].remove(e)

def solucion_horizontal():
    # checar horizontal
    for i in range (9):
        for y in range (9):                       
            if len(posibles_nums[i][y]) != 1:
                num_remover = []
                for x in range (9):
                    # si uno en la col esta determinado
                    if len(posibles_nums[i][x]) == 1:
                        #checar si lo tiene en sus pos
                        for n in range (len(posibles_nums[i][y])):
                            # quitarlo si es que esta
                            if posibles_nums[i][y][n] == posibles_nums[i][x][0]:
                                num_remover.append(posibles_nums[i][y][n])  
                for e in num_remover:
                    if e in posibles_nums[i][y]:
                        posibles_nums[i][y].remove(e)
            
def tresXtres():
    for v in range(3):
        if v == 0:
            count_ren = 0
        elif v == 1:
            count_ren = 3
        else:
            count_ren = 6
        count_col = 0
        for o in range (3):
            for i in range (3):
                for y in range(3):
                    if len(posibles_nums[count_ren + i][count_col + y]) != 1:
                        num_remover = []
                        for w in range (count_ren,count_ren + 3):
                            for q in range (count_col,count_col + 3):
                                # si uno en la 3x3 esta determinado
                                if len(posibles_nums[w][q]) == 1:
                                    #checar si lo tiene en sus pos
                                    if posibles_nums[w][q] in posibles_nums[count_ren + i][count_col + y]:
                                        posibles_nums[count_ren + i][count_col + y].remove(posibles_nums[w][q])
                                    for n in range (len(posibles_nums[count_ren + i][count_col + y])):
                                        # quitarlo si es que esta    
                                        if posibles_nums[count_ren + i][count_col + y][n] == (posibles_nums[w][q][0]):
                                            num_remover.append(posibles_nums[count_ren + i][count_col + y][n])  
                        for e in num_remover:
                            if e in posibles_nums[count_ren + i][count_col + y]:
                                posibles_nums[count_ren + i][count_col + y].remove(e)
            count_col = count_col + 3

def buscar_arreglos():
    equisde = False
    for i in range (9):
        for y in range (9):
            if len(posibles_nums[i][y]) is not 1:
                equisde = True
    if equisde == False:
        mostrar()
        print("yey")
        exit() 
    else:
        return()

def checarchido():
    global valor
    if kounter > 40:
        valor = False
        chido()  
        if valor != False:
            chido3X3()        
                            
def mal():
    vertical()
    horizontal()
    X3X3()
            
def solucion():
    global kounter
    global posibles_nums
    # busca errores
    mal()
    kounter += 1
    solucion_vertical()
    solucion_horizontal()
    tresXtres()
    # resolver unica posibilidad del numero en una linea
    checarchido()
    # buscar arreglos
    buscar_arreglos()
    
def main():

    global valor
    global posibles_nums
    global kounter 
    kounter = 0
    
    sudoku =[[[5],[],[],[],[4],[],[],[7],[]],
            [[],[4],[],[],[],[1],[2],[],[]],
            [[],[1],[],[9],[],[],[],[],[]],
            [[],[],[],[],[5],[8],[3],[],[]],
            [[1],[],[6],[],[],[],[7],[],[2]],
            [[],[],[9],[7],[6],[],[],[],[]],
            [[],[],[],[],[],[7],[],[9],[]],
            [[],[],[1],[6],[],[],[],[2],[]],
            [[],[7],[],[],[3],[],[],[],[4]]]

    posibles_nums = [[[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], 
                    [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]], [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]]  
    
    #reemplazar posibles_nums con valores ya puestos
    for i in range (9):
        for y in range (9):
            if sudoku[i][y] != []:
                posibles_nums[i][y] = sudoku[i][y]  
    while 1 != 2:
        solucion()
main()
