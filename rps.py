import random


    
class DommeTegenstander:

    def kiest(self):
        return 'papier'

class SlimmeSpeler:

    def kiest(self):
        return random.choice(['steen', 'papier', 'schaar'])




class Speler:

    def kiest(self):

        antwoord = input('kies je 1(steen), 2(papier) of 3(schaar) ')
        for i in range(50):
            print('')

        
        if(antwoord == 1):
            return 'steen'

        elif(antwoord == 2):
            return 'papier'

        else:
            return 'schaar'
            
def wie_wint(tegenstander_speelt, jij_speelt):
    print(f'tegenstander kiest {tegenstander_speelt}')
    print(f'jij kiest {jij_speelt}')
    print('')

    if(tegenstander_speelt == jij_speelt):
        print('gelijk spel')

    elif(tegenstander_speelt == 'steen' and jij_speelt == 'schaar'):
        print("tegenstander wint")

    elif(tegenstander_speelt == 'papier' and jij_speelt == 'steen'):
        print("tegenstander wint")

    elif(tegenstander_speelt == 'schaar' and jij_speelt == 'papier'):
        print("tegenstander wint")

    else:
        print("jij wint")

speler_wilt_door = "1"

while(speler_wilt_door == "1"):
    
    tegenstander = input('wil je tegen een domme speler(toets 1) of tegen een slimme speler(toets 2) of tegen elkaar(toets 3) ')
    print('')

    if(tegenstander == '1'):
        harry = DommeTegenstander()
        wat_doet_tegenstander = harry.kiest()

    elif(tegenstander == '3'):
        print("Je tegenstander mag eerst kiezen")
        persoon = Speler()
        wat_doet_tegenstander = persoon.kiest()

    else:
        piet = SlimmeSpeler()
        wat_doet_tegenstander = piet.kiest()
        

    jij = Speler()
    wat_doe_jij = jij.kiest()

    wie_wint(wat_doet_tegenstander, wat_doe_jij)

    speler_wilt_door = input('toets 1 om nog een keer te spelen. ')
    
