import json
def start():

    def player_create():
        prompt = input("Veuillez entrer votre nom d'utilisateur à créer:")
        if prompt != "":
            try:
                user = {
                    "name": prompt,
                    "game_number": 0,
                    "win_number": 0

                }
                json_value = json.dumps(user)
                fichier = "players/" + prompt + ".json"

                f = open(fichier, "x")
                f.close()

                f = open(fichier, "a")
                f.write(json_value)
                f.close()
                print("Utilisateur créée avec succés")
                return player_load()
            except Exception:
                print("L'utilisateur existe déjà")
                start()
        else:
            player_create()

    def player_load():
        prompt = input("Veuillez entrer votre nom d'utilisateur a utiliser:")
        try:
            fichier = "players/" + prompt + ".json"
            f = open(fichier)
            json_value = f.read()
            f.close
            dictio = json.loads(json_value)
            return dictio["name"]
        except Exception:
            print("Cet utilisateur n'existe pas")
            start()

    def history(winner,loser):
        from datetime import datetime
        date_now = datetime.now()
        standart_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
        f = open("history.txt", "a")
        phrase = standart_date + ":"+winner+" a remporter la victoire sur " +loser+"\n"
        f.write(phrase)
        f.close()

    prompt = input("Souhaitez vous créer un utilisateur,vous connecter ou jouer en tant qu'invité ?(U,C,I):")
    match prompt:
        case "U":
            return player_create()

        case "C":
            return player_load()
        case "I":
            pass
        case _:
            start()


def player_count(winner, loser,equality):

    players = [winner, loser]


    for r in players:
        file = "players/" + r + ".json"
        f = open(file)
        json_value = f.read()
        f.close
        dictio = json.loads(json_value)
        dictio["game_number"]+=1
        if equality ==0:
            if r == winner:
                dictio["win_number"]+=1
            json_value = json.dumps(dictio)
            f = open(file,"w")
            f.write(json_value)
            f.close()
    def history():
        from datetime import datetime
        date_now = datetime.now()
        standart_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
        f = open("history.txt", "a")
        if equality ==0:
            phrase = standart_date + ":"+winner+" a remporter la victoire sur " +loser+"\n"
        else:
            phrase = standart_date + ":" + winner + " et " + loser + " ont fait une egalite\n"
        f.write(phrase)
        f.close()
    history()