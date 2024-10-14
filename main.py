import logic

if __name__ == '__main__':
    # Declare mat
    mat = logic.start_game()

    #Main loop
    while True:
        logic.clear_screen()
        # Print mat
        logic.print_grid(mat)
        choice = input("WASD: ")
        
        if choice == 'w' or choice == 'W':
            mat, flag = logic.move_up(mat)
        elif choice == 'a' or choice == 'A':
            mat, flag = logic.move_left(mat)
        elif choice == 's' or choice == 'S':
            mat, flag = logic.move_down(mat)
        elif choice == 'd' or choice == 'D':
            mat, flag = logic.move_right(mat)
        else:
            continue  # Invalid input, continue the loop

        # After each move, check the game state
        status = logic.game_state(mat)

        # If the game is not over, try adding a new 2
        if status == '' and flag:
            logic.add_new_2(mat)
        elif status == 'LOST':
            print("Game Over: You lost!")
            break
        elif status == 'WON':
            print("Congratulations, you won!")
            break
