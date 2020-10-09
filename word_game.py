def word_game(s):

    vowels = ['A', 'E', 'I', 'O', 'U']

    RamuS = 0  #Vowels
    AbhiS = 0  #Consonants
    for i, c in enumerate(s):

        if c in vowels:
            RamuS += len(s) - i
        else:
            AbhiS += len(s) - i

        
    if AbhiS == RamuS:
        print("Draw")
    elif(AbhiS > RamuS):
        print('Abhi {}'.format(AbhiS))
    else:
        print('Ramu {}'.format(RamuS))

#Driver code

s = input()

