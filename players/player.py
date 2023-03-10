import json
import glob, os
os.chdir("players/")

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
                fichier = "" + prompt + ".json"

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
        import glob, os
        for utilisateur in glob.glob("*.json"):
            print(utilisateur[:-5])
        prompt = input("Veuillez choisir un nom d'utilisateur parmis la liste ci-dessus:")
        print(prompt)

        try:
            fichier = "" + prompt + ".json"
            f = open(fichier)
            json_value = f.read()
            f.close
            dictio = json.loads(json_value)
            prompt= input("Bienvenue "+prompt+",souhaitez vous voir votre score ?(YN)")
        except Exception:
            print("Cet utilisateur n'existe pas")
            start()
        if prompt == "Y":
            games=dictio["game_number"]
            games=str(games)
            wins=dictio["win_number"]
            wins=str(wins)
            phrase="Votre nombre total de partie est de "+ games+" et votre nombre de victoire est de "+wins
            print(phrase)
        return dictio["name"]


    prompt = input("Souhaitez vous créer un utilisateur(U),vous connecter(C), jouer en tant qu'invité(I) ou juste afficher l'historique(H) ?(U,C,I,H):")
    match prompt:
        case "U":
            return player_create()

        case "C":
            return player_load()
        case "I":
            pass
        case "H":
            show_history()
            start()
        case _:
            start()


def player_count(winner, loser, equality):
    players = [winner, loser]

    for r in players:
        file = r + ".json"
        f = open(file)
        json_value = f.read()
        f.close
        dictio = json.loads(json_value)
        dictio["game_number"] += 1
        if equality == 0:
            if r == winner:
                dictio["win_number"] += 1
            json_value = json.dumps(dictio)
            f = open(file, "w")
            f.write(json_value)
            f.close()

    def history():
        from datetime import datetime
        date_now = datetime.now()
        standart_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
        f = open("history.txt", "a")
        if equality == 0:
            phrase = standart_date + ":" + winner + " a remporter la victoire sur " + loser + "\n"
        else:
            phrase = standart_date + ":" + winner + " et " + loser + " ont fait une egalite\n"
        f.write(phrase)
        f.close()

    history()

def show_history():
    print("Voici l'historique des parties affiché par ordre chronologique")
    f=open("history.txt")
    print(f.read())
    f.close()