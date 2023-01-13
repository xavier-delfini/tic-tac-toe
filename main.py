def tic_tac_toe():
    import time
    morp = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    player1 = ""
    player2 = ""
    v=0
    from players import player
    while v==0:
        print("Au tour du premier joueur de se connecté")
        time.sleep(1)
        player1 = player.start()
        if player1 is None:
            player1 = "Joueur 1"

        prompt = input("Souhaitez-vous jouer contre un bot ?(YN):")
        if prompt == "Y":
            import ai
            ai.ia(morp,2)
        else:
            print("Au tour du second joueur de se connecté")
            time.sleep(1)
            player2 = player.start()
            if player2 is None:
                player2 = "Joueur 2"
            if player1 == player2:
                print("Les 2 nom d'utilisateur sont les mêmes, veuillez recommencer")
                time.sleep(3)
            else:
                v=1
    import random
    t = bool(random.getrandbits(1))

    if t == 0:
        print(player1+" commence")
    else:
        print(player2+" commence")

    t += 1

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
                if morp[k][l] > 0:
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

    def insert_value(value, letter, inser):
        u = 0
        value = int(value)
        value = value - 1
        if letter == "A":
            letter = 0
        elif letter == "B":
            letter = 1
        elif letter == "C":
            letter = 2
        while u == 0:
            if morp[value][letter] < 1:
                morp[value][letter] = inser
                u = 1
            else:
                v = 0
                while v == 0:
                    restart = input("Cette case est déjà remplie, veuillez entrer une autre case:")
                    if (restart[0] == "1" or restart[0] == "2" or restart[0] == "3") and restart[1] == "A" or restart[
                        1] == "B" or restart[1] == "C":
                        insert_value(restart[0], restart[1], inser)
                        u = 1
                        v = 1

    i = 0  # Compteur tour
    def input_verif_insert(player):
        w= player
        print(w)
        z=0
        while z==0:

            if w == 1:
                phrase = "C'est au tour de "+ player1 +" de jouer veuillez écrire une lettre et un nombre au format suivant 1A allant de 1 à 3 et de A a C:"
            else:
                phrase = "C'est au tour de " + player2 + " de jouer veuillez écrire une lettre et un nombre au format suivant 1A allant de 1 à 3 et de A a C:"
            inputX = input(phrase)
            if (inputX[0] == "1" or inputX[0] == "2" or inputX[0] == "3") and (inputX[1] == "A" or inputX[1] == "B" or inputX[1] == "C"):
                if w == 1:
                    w = 2
                    symbol = 1
                else:
                    w = 1
                    symbol = 2
                insert_value(inputX[0], inputX[1], symbol)
                z=1
                return w

    while i < 9 and verif_plateau() == 0:
        print_plateau()
        t=input_verif_insert(t)
        i += 1
    print_plateau()
    if verif_plateau() > 0:

        if verif_plateau() == 1:
            print("Victoire de "+player1)
            player.player_count(player1, player2,0)
        elif verif_plateau() == 2:
            print("Victoire de "+player2)
            player.player_count(player2, player1,0)
    else:
        print("égalité")
        player.player_count(player2, player1, 1)



tic_tac_toe()
