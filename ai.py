def ia(board, signe):
    def convert_array():
        new_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        z = 0
        for x in board:
            for y in x:
                new_board[z] = y
                z += 1
#Si premier
    #Commencer en 0, 2,6 ou 8
#Si l'adversaire met un O autre part qu'au millieu
    #La game est normalement gagné
#Sinon il faut attendre une erreur de sa part