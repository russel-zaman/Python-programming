import shuffle
import pg

def check_gusess(mylist,guess):
    if mylist[guess] == "O":
        print("Guess Correct")
    else:
        print("wrong predection")
        print(mylist)


# initial lsit
mylist = [" ", "O"," "]

#shuffle list
mixedup_list = shuffle.shuffle_list(mylist)
print(mixedup_list)

#User guess
guess = pg.player_guess()


game_on = True
while game_on:
    #Check Guess
    check_gusess(mixedup_list,guess)
    user_input = input("Do you want to play again: ")
    if user_input == "n":
        break
    else:
        guess = pg.player_guess()
        # shuffle list
        mixedup_list = shuffle.shuffle_list(mylist)
        print(mixedup_list)

