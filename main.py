import logic

if __name__ == '__main__':
    #Declare mat
    mat = logic.start_game()

    #User choices
    
    while True:
        logic.clear_screen()
        #Print mat
        logic.print_grid(mat)
        choice = input("WASD: ")
        #Move up
        if choice == 'w' or choice == 'W':
            # call the move up function
            mat, flag = logic.move_up(mat)

            # get the current state and print it
            status = logic.game_state(mat)

            # if game not over add a new two
            if(status == ''):
                logic.add_new_2(mat)

            # else break the loop 
            else:
                print(status)
                break
        #Move left
        elif choice == 'a' or choice == 'A':
            #Call move left function
            mat, flag = logic.move_left(mat)
            # get the current state and print it
            status = logic.game_state(mat)

            # if game not over add a new two
            if(status == ''):
                logic.add_new_2(mat)

            # else break the loop 
            else:
                print(status)
                break
        #Move down
        elif choice == 's' or choice == 'S':
            #Call the move down function
            mat, flag = logic.move_down(mat)
            # get the current state and print it
            status = logic.game_state(mat)

            # if game not over add a new two
            if(status == ''):
                logic.add_new_2(mat)

            # else break the loop 
            else:
                print(status)
                break
        #Move right
        elif choice == 'd' or choice == 'D':
            #call the move right function
            mat, flag = logic.move_right(mat)
            # get the current state and print it
            status = logic.game_state(mat)

            # if game not over add a new two
            if(status == ''):
                logic.add_new_2(mat)

            # else break the loop 
            else:
                print(status)
                break
