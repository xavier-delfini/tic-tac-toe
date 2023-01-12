from datetime import datetime
date_now = datetime.now()
standart_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
f = open("history.txt", "a")
phrase=standart_date+":Joueur 1 a remporter la victoire sur Joueur 2\n"
f.write(phrase)
f.close()
