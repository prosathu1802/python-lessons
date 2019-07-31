guess = "Guess a number 1-10"
nList = [2,5,8]

while True:
        print("Press q to quit")
            user = input(guess)
                if user == "q":
                            break
                            try:
                                        user=float(user)
                                                if user in nList:
                                                                print("Correct")
                                                                        else:
                                                                                        print("Wrong")
                                                                                            except ValueError:
                                                                                                        print("Type a number or q")

