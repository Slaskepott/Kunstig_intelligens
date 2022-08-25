import random

leksikon = {}
parringer = {}
setningslengde = []

def main():
    response = input()
    evaluate_response(response)
    generate_reply()

def evaluate_response(response):
    assert isinstance(response,str)
    response_list = response.split()
    setningslengde.append(len(response_list))
    i = 0
    for word in response_list:
        word = word.lower()
        if word in leksikon:
            leksikon[word] += 1
        else:
            if i < len(response_list) - 1:
                    parringer[word] = response_list[i+1]
            leksikon[word] = 1
        i += 1

def generate_reply():
    reply = ""
    if len(parringer) > 0:
        for i in range(get_setningslengde()):
            randomizer = random.randint(0,1)
            if randomizer == 0:
                reply += random_word() + " "
            else:
                list = random_pair()
                reply += list[0] + " " + list[1] + " "
    else:
        for i in range(get_setningslengde()):
            reply += random_word() + " "
    reply.capitalize()
    print(reply + "\n")
    main()

def get_setningslengde():
    lengdesnitt = 1
    i = 0
    for entry in setningslengde:
        lengdesnitt += setningslengde[i]
        i += 1
    lengdesnitt = int(lengdesnitt / len(setningslengde))
    return lengdesnitt

def random_word():
    picked_word_index = random.randint(0,len(leksikon)) - 1
    word_list = list(leksikon.keys())
    picked_word = word_list[picked_word_index]
    return picked_word

#Funksjonen bruker ordboken "parringer". Den skal finne et tall mellom 0 og lengden på "parringer"-ordboken.
def random_pair():
    #Finn en tilfeldig index innen lengden på parringer
    picked_pair_index = random.randint(0,len(parringer)-1)
    #Gjør om parringene til en liste
    parringer_liste = list(parringer)
    #Lagre tilfeldig valgt key i en variabel
    ord1 = parringer_liste[picked_pair_index]
    #Lagre dens value i en variabel
    ord2 = parringer[ord1]
    #Returner en tilfeldig parring
    return [ord1,ord2]

main()
