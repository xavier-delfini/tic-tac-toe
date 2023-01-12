def start():
    import json
    def player_create():
        prompt = input("Veuillez entrer votre nom d'utilisateur")
        if prompt != "":
            try:
                user = {
                    "name": prompt,
                    "score": 0
                }
                json_value = json.dumps(user)
                fichier="players/"+prompt+".json"
                f = open(fichier,"x")
                f.close()
                f = open(fichier,"a")
                f.write(json_value)
                f.close()
                print("Utilisateur créée avec succés")
            except Exception:
                print("L'utilisateur existe déjà")
                start()

        else:
            player_create()
    # def player_load():

    # def player_count():

    # def history():

    prompt=input("Souhaitez vous crée un utilisateur,vous connecter ou jouer en tant qu'invité ?(U,C,I):")
    match prompt:
        case "U": return player_create()

        #case "C":
            #player_load()
        case "I":
            pass
        case _:
            start()
