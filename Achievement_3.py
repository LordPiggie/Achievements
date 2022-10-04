# Setting i to the value of one keeps my loop active
i = 1

#This keeps the program looping
while i == 1:
    
    #This asks for user input and then strips the user input
    user = (input('Hello, what is your username?: ').strip())


    #This ensures the username is greater than 1
    if len(user) <= 1:
        print('This username is too short')

    #This ensures the username is less than or equal to 20
    elif len(user) > 20:
        print('This username is over 20 characters')

    #This is what happens if the user has entered a proper number of characters for their username
    else:
        
        #This ensures the user has entered a number and a capital letter. This also is the only path that breaks the loop. This also solved a bug where the number 20 would go through the loop.
        if user.islower() == False and user.isalpha() == False and user.isnumeric() == False:
            print('Username accepted\n\n')
            print(user)
            break

        #This path will instruct the user what they have done wrong in inputting their username.
        else:
            print("Username must contain one capital letter and one number. [i.e. Abc123]")