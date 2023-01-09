def tic_tac_toe():
    # import random
    # Premier = bool(random.getrandbits(1))
    morp = [0, 0, 0], \
        [0, 0, 0], \
        [0, 0, 0]
    morp = list(morp)
    def print_plateau():
        k = 0
        print("  ABC")
        c = 1
        while k < 3:
            l = 0

            case = ""
            résultat = str(c)
            résultat = résultat + " "
            while l < 3:
                if morp[k][l] >0:
                    if morp[k][l] == 1:
                        case = "X"
                    elif morp[k][l] == 2:
                        case = "O"
                else:
                    case = "."
                résultat = résultat + case
                l += 1
            c += 1
            print(résultat)
            k += 1

    def verif_plateau():
        test_up = morp[0][0]
        test_middle = morp[1][0]
        test_bottom = morp[2][0]
        test_middle_up = morp[0][1]
        test_right_up = morp[0][2]
        if (test_up > 0) and (
                (test_up == morp[1][0] and test_up == morp[2][0]) or
                (test_up == morp[1][1] and test_up == morp[2][2]) or
                (test_up == morp[0][1] and test_up == morp[0][2])
        ):
            return test_up

        elif (test_middle > 0) and (
                (test_middle == morp[1][1] and test_middle == morp[1][2])
        ):
            return test_middle

        elif (test_bottom > 0) and (
                (test_bottom == morp[2][1] and test_bottom == morp[2][2])
        ):
            return test_bottom

        elif (test_middle_up > 0) and (
                (test_middle_up == morp[1][1] and test_middle_up == morp[2][1])
        ):
            return test_middle_up

        elif (test_right_up > 0) and (
                (test_right_up == morp[1][2] and test_right_up == morp[2][2]) or
                (test_right_up == morp[1][1] and test_right_up == morp[2][0])
        ):
            return test_right_up

        else:
            return 0
    def insert_value(value,letter,inser):

        value = int(value)
        value = value - 1
        if letter == "A":
            letter = 0
        elif letter == "B":
            letter = 1
        elif letter == "C":
            letter = 2
        u=0
        while u==0:
            if morp[value][letter]<1:
                morp[value][letter]=inser
                u=1
            else:
                v=0
                while v==0:

                    if (inputX[0] == "1" or inputX[0] == "2" or inputX[0] == "3") and inputX[1] == "A" or inputX[1] == "B" or inputX[1] == "C":
                        restart=input("Cette case est déjà remplie, veuillez entrer une autre case:")
                        insert_value(restart[0],restart[1],inser)
                        u=1
                        v=1
                    else:
                        v=1



    i = 0  # Compteur tour
    t = 0


    while i < 9 and verif_plateau() == 0:
        print_plateau()
        if t == 0:
            inputX = input("Au joueur X de jouer veuillez écrire une lettre et un nombre au format suivant 1A allant de 1 à 3 et de A a C:")
            if (inputX[0] == "1" or inputX[0] == "2" or inputX[0] == "3") and inputX[1] =="A" or inputX[1] =="B" or inputX[1] =="C":
                insert_value(inputX[0],inputX[1], 1)
                t = 1
            else:
                i= i-1

        else:
            inputX = input("Au joueur O de jouer veuillez écrire un numéro et une lettre au format suivant 1A allant de 1 à 3 et de A a C:")
            if (inputX[0] == "1" or inputX[0] == "2" or inputX[0] == "3") and inputX[1] =="A" or inputX[1] =="B" or inputX[1] =="C":
                insert_value(inputX[0], inputX[1], 2)
                t = 0
        i += 1
    print_plateau()
    if verif_plateau() > 0:

        if verif_plateau() == 1:
            print("Victoire de X")
        elif verif_plateau() == 2:
            print("Victoire de O")
    else:
        print("égalité")

tic_tac_toe()
