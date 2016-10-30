print("Algoritmo de perguntas e respostas para se descobrir qual animel está sendo requisitado.\n"
      "Digite (s)Sim ou (n)Não!\nOs primcipais reinos animais a serem selecionados são: Mamífero, Ave, Réptil.")
carni,herb,oniv,frut,voador,aquatico,tropic,polar,nadador,rapina,casco,reptCarn,semPatas = "Leão","Cavalo","Homem","Macaco","Morcego","Baleia","Avestruz","Pinguim","Pato","Águia","Tartaruga","Crocodilo","Cobra"
mamifero = input("É mamífero? Digite (S)Sim ou (n)Não:")
quadrupede=''
if mamifero=="s" or mamifero=="Sim" or mamifero=="sim":
        quadrupede = input("É quadrupede? Digite (S)Sim ou (n)Não:")
        if quadrupede=="s" or quadrupede=="Sim" or quadrupede=="sim":
            invalido = "s"
            while invalido == "s":
                carnivoro = input("É carnívoro? Digite (S)Sim ou (n)Não:")
                if carnivoro != "s" or carnivoro != "Sim" or carnivoro != "sim" or carnivoro !="n" or carnivoro!="Não" or carnivoro!="não":
                    if carnivoro == "s" or carnivoro=="Sim" or carnivoro=="sim":
                        print("O escolhido foi o %s!"%carni)
                        break
                    elif carnivoro =="n" or carnivoro=="Não" or carnivoro=="não":
                        while carnivoro=="n":
                            herbivoro = input("É herbívoro? Digite (S)Sim ou (n)Não:")
                            if herbivoro == "s" or herbivoro == "Sim" or herbivoro == "sim":
                                print("O escolhido foi o %s!"%herb)
                                break
                            elif herbivoro =="n" or herbivoro == "Não" or herbivoro == "não":
                                print("Resposta Invélida, o animal tem que ser Herbívoro. Digite sim para descobrir o tipo de animal Herbívoro")
                        carnivoro="n"
                    break
                else:
                    print("Caracter ou palavra informada inválida.")
            invalido = "s"
        elif quadrupede=="n" or quadrupede=="Não" or quadrupede=="não":
            bipede = input("É bipede? Digite (S)Sim ou (n)Não.")
            if bipede=="s" or bipede=="Sim" or bipede=="sim":
                onivoro = input("É onívoro? Digite (S)Sim ou (n)Não:")
                if onivoro=="s" or onivoro=="Sim" or onivoro=="sim":
                    print("O escolhido foi o %s!"%oniv)
                elif onivoro =="n" or onivoro=="Não" or onivoro=="não":
                    while onivoro == "n":
                        frutivoro = input("É frutívoro? Digite (S)Sim ou (n)Não:")
                        if frutivoro=="s" or frutivoro=="Sim" or frutivoro=="sim":
                            print("O escolhido foi o %s!"%frut)
                            break
                        elif frutivoro =="n" or "Não" or "não":
                            print("Resposta Invélida, o animal tem que ser Frutívoro. Digite sim para descobrir o tipo de animal Frutívoro:")
                    onivoro="n"
            elif bipede=="n" or bipede=="Não" or bipede=="não":
                    voadores = input("É Voador? Digite (S)Sim ou (n)Não:")
                    if voadores=="s" or voadores=="Sim" or voadores=="sim":
                        print("O escolhido foi o %s!"%voador)
                    elif voadores =="n" or voadores=="Não" or voadores=="não":
                        while voadores=="n":
                            aquaticos = input("É aquatico? Digite (S)Sim ou (n)Não:")
                            if aquaticos=="s" or aquaticos=="Sim" or aquaticos=="sim":
                                print("O escolhido foi o %s!"%aquatico)
                            elif aquaticos=="n" or aquaticos=="Não" or aquaticos=="não":
                                print("Resposta Invélida, o animal tem que ser Aquático. Digite sim para descobrir o tipo de animal Aquatico:")
                        voadores="n"
elif mamifero=="n" or mamifero=="Não" or mamifero=="não":
        ave = input("É ave?")
        if ave=="s" or ave=="Sim" or ave=="sim":
            naoVoadoras = input("É Não-voadora? Digite (S)Sim ou (n)Não:")
            if naoVoadoras=="s" or naoVoadoras=="Sim" or naoVoadoras=="sim":
                    tropicais = input("É Tropical? Digite (S)Sim ou (n)Não:")
                    if tropicais == "s" or tropicais == "Sim" or tropicais == "sim":
                        print("O escolhido foi o %s!" % tropic)
                    elif tropicais =="n" or tropicais == "Não" or tropicais == "não":
                        while tropicais == "n":
                            polares = input("É polar? Digite (S)Sim ou (n)Não:")
                            if polares == "s" or polares == "Sim" or polares == "sim":
                                print("O escolhido foi o %s!" % polar)
                                break
                            elif polares =="n" or polares == "Não" or polares =="não":
                                print("Resposta Invélida, o animal tem que ser Polar. Digite sim para descobrir o tipo de animal Polar:")
                        tropicais = "n"
            elif naoVoadoras=="n" or naoVoadoras=="Não" or naoVoadoras=="não":
                nadadoras = input("É Nadadora? Digite (S)Sim ou (n)Não:")
                if nadadoras=="s" or nadadoras=="Sim" or nadadoras=="sim":
                    print("O escolhido foi o %s!"%nadador)
                elif nadadoras=="n" or nadadoras=="Não" or nadadoras=="não":
                    while nadadoras=="n":
                        deRapina = input("É de rapina? Digite (S)Sim ou (n)Não:")
                        if deRapina=="s" or deRapina=="Sim" or deRapina=="sim":
                            print("O escolhido foi o %s!" % rapina)
                            break
                        elif deRapina=="n" or deRapina=="Não" or deRapina=="não":
                            print("Resposta Invélida, o animal tem que ser De Rapina. Digite sim para descobrir o tipo de animal De Rapina:")
                    nadadoras="n"
        elif ave=="n" or ave=="Não" or ave=="não":
            reptil = input("É réptil?Digite (S)Sim ou (n)Não:")
            if reptil=="s" or reptil=="Sim" or reptil=="sim":
                comCasco = input("Tem casco? Digite (S)Sim ou (n)Não:")
                if comCasco== "s" or comCasco== "Sim" or comCasco== "sim":
                    print("O escolhido foi o %s!" % casco)
                elif comCasco=="n" or comCasco== "Não" or comCasco== "não":
                    repCarn = input("É réptil carnívoro? Digite (S)Sim ou (n)Não:")
                    if repCarn=="s" or repCarn=="Sim" or repCarn=="sim":
                        print("O escolhido foi o %s!" % reptCarn)
                    elif repCarn =="n" or repCarn=="Não" or repCarn=="não":
                        while repCarn=="n":
                            repSemPatas = input("Não tem patas? Digite (S)Sim ou (n)Não:")
                            if repSemPatas == "s" or repSemPatas == "Sim" or repSemPatas == "sim":
                                print("O escolhido foi o %s!" % semPatas)
                                break
                            elif repSemPatas =="n" or repSemPatas == "Não" or repSemPatas == "não":
                                print("Resposta Invélida, o animal tem que ser da categoria 'Sem patas'. Digite sim para descobrir o tipo de animal da categoria 'Sem patas':")
                        repCarn = "n"
            elif reptil =="n" or reptil =="Não" or reptil =="não":
                    print("Resposta Invélida, você não selecionou nenhum animal, reinicie o programa para descobrir o animal")