punten = 0


print('!welkom bij de minecraft quiz!')

speler = input('wat is je naam? ')

print(f'hallo {speler}, we gaan testen hoeveel jij weet over minecraft') 
print('')
print('Vraag 1')
print('op welk tijdstip spawnen monsters')
antwoord1 = input('dag of nacht? ').lower()
if antwoord1 == 'nacht' :
    print('bravo')
    punten +=1
else :
    print('volgende keer beter')

print('')
print('Vraag 2')
print('waar kunnen zombies niet tegen?:\n a)water\n b)zon\n c)melk')
antwoord2 = input('typ a, b of c ').lower()
if antwoord2 == 'b' :
    print('bravo')
    punten +=1
else :
    print('volgende keer beter')

print('')
print('Vraag 3')
print('hoeveel houten blokjes heb je nodig voor vier stokken?')
antwoord3 = input('typ het getal of letters ').lower()
if antwoord3 == '2' or antwoord3=='twee' :
    print('bravo')
    punten +=1
else :
    print('volgende keer beter')

print('')
print('Vraag 4')
print('wat moet je doen om het spel uit te spelen?:\n a)een kasteel bouwen\n b)een kist vol diamant verzamelen\n c)de ender dragon verslaan ')
antwoord4 = input('typ a, b of c ').lower()
if antwoord4 == 'c':
    print('bravo')
    punten +=1
else :
    print('volgende keer beter')

print('')
print('Vraag 5')
print('tot hoeveel blokjes hoog kan je bouwen?')
antwoord5 = input('typ het getal ')
if antwoord5 == '256' or antwoord5 == '255':
    print('bravo')
    punten +=1
else :
    print('volgende keer beter')

print('')
vraag = input('je hebt het einde gehaald, wil je je resultaten zien? ja of nee ').lower()
if vraag == 'ja' :
    if punten <= 1 :
        print(f'ga onmiddelijk minecraft spelen je hebt maar {punten} punten gehaald!')

    elif punten <=3 :
        print(f"misschien een uurtje minder aan huiswerk en meer aan minecraft je hebt {punten} punten gehaald.")

    else :
        print(f'jij hebt je leven genoeg tijd besteed aan minecraft nu kan je je huiswerk maken je hebt {punten} punten.')

else :
    print('')
    print(f'{speler} dacht je nou echt dat je je score kon ontvluchten je hebt {punten} punten.')
