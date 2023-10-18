def run():
    treasure_dis = False
    key_dis = False

    choice = input("you are in old castle and want to find treasure where to go right or left? ")
    while True:
        if choice == 'right':
            choice1 = input("wow, swords how they are beauful! oh, look stairs and window, what to do jump though window or go on upstairs? ")
            if choice1 == 'jump though window':
                print('oh no, you died!')
                print("GAME OVER!")
                break
            elif choice1 == 'go on upstairs':
                print('there is king and he said that you must go!')
                print('GAME OVER!')
                break

        elif choice == 'left':
            choice2 = input('you are in big room and there are two rooms left and right, where to go? ')
            if choice2 == 'left':
                choice3 = input('Door is locked, what to do break the door or break the floor? ')
                if choice3 == 'break the door':
                    if key_dis:
                        print("you found treasure and anlocked it!")
                        print("you winn! ")
                        break
                    else:    
                        choice4 = input('You broke door, oh there is treasure but it locked, what to do go back or end game? ')
                        treasure_dis = True

                    if choice4 == 'end game':
                        print('OK then, Game Over!')
                        break
                    elif choice4 == 'go back':
                        choice5 = input('OK, what to do break the floor or end game? ')
                        if choice5 == 'end game':
                            print('OK then, Game Over!')
                            break
                        elif choice5 == 'break the floor':
                            if treasure_dis:
                                print("you found key! and you opened treasure!")

                                print('You win')
                                break
                            else:
                                print("you found key!")
                                key_dis = True
                elif choice3 == 'break the floor':
                    if treasure_dis:
                        print("you found key! and you opened treasure!")
                        print('You win')
                        break
                    else:
                        print("you found key!")
                        key_dis = True

                                    
            elif choice2 == 'right':
                choice6 = input('There is stairs, what to do go on upstairs or end game? ')
                if choice6 == 'end game':
                    print('OK then, Game Over!')
                    break
                elif choice6 == 'go on upstairs':
                    print('there is king and he said that you must go!')
                    print('GAME OVER!')
                    break

                                                
