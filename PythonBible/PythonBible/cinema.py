films ={
    'Finding Dory': [3,5],
    'Bourne' : [18,5],
    'Tarzan' :[15,5],
    'Ghost Busters' : [12,5]
    }
while True:

    choice= input('what film would you like to watch?: ').strip().title()

    if choice in films:
        age = int(input('how old are you?: ').strip())

        #check user age
        if age>= films[choice][0]:

            #check enough seats
            
            num_seats = films[choice][1]
                
            if num_seats>0:
                print('Enjoy the film')
                films[choie][1]= films[choice][1]-1
            else:
                print('Sorry we are sold out')
        else:
            print('You are too young to watch that film')
        
    else:
        print('we dont have that film...')
