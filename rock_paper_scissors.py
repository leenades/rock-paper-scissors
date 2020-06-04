import random
import sys

rockPaperScissors_list = [1, 2, 3]



def rockPaperScissors_game():
    user_points = 0
    comp_points = 0
    
    
    def winning_condition(user_points, comp_points):
        if user_points == 3:
            print("\n\t\tYou Won!")
            sys.exit()
        if comp_points == 3:
            print("\n\t\tYou Lost!")
            sys.exit()
    

    def game_choice(user_points, comp_points):
            
        user_choice = eval(input("\n1- rock \n2- paper \n3- scissors \nYou: "))
        computer_choice = random.choice(rockPaperScissors_list)
    
        if user_choice >= 4:
            print("\tChoose either rock, paper, or scissors!!")
            game_choice(user_points, comp_points)
            
        elif user_choice <=3:
            if computer_choice == 1:
                print("\nComputer: rock")
            if computer_choice == 2:
                print("\nComputer: paper")
            if computer_choice == 3:
                print("\nComputer: scissors")
            
            if user_choice == 1 and computer_choice == 1:  
                user_points = user_points
                comp_points = comp_points
                print("------------------")
                print("\nDraw. No points won. \n")
                print("------------------")
                game_choice(user_points, comp_points)

            if user_choice == 1 and computer_choice == 2:
                print("------------------")
                print("\nComputer wins a point. \n")
                print("------------------")
                comp_points += 1
    
                print("Computer total points: ",comp_points)
                print("Your total points: ",user_points)
                print("------------------")            
                winning_condition(user_points, comp_points)
    
                game_choice(user_points, comp_points)

            if user_choice == 1 and computer_choice == 3:
                print("------------------")
                print("\nYou win a point. \n")
                print("------------------")
                user_points += 1
                
                print("Computer total points: ",comp_points)
                print("Your total points: ",user_points)
                print("------------------")
                winning_condition(user_points, comp_points)
            
                game_choice(user_points, comp_points)


            if user_choice == 2 and computer_choice == 1:
                print("------------------")
                print("\nYou win a point. \n")       
                print("------------------")
                user_points += 1

                print("Computer total points: ",comp_points)
                print("Your total points: ",user_points)
                print("------------------")
                winning_condition(user_points, comp_points)
                
                game_choice(user_points, comp_points)

            if user_choice == 2 and computer_choice == 2:
                user_points = user_points
                comp_points = comp_points        
                print("------------------")   
                print("\nDraw. No points won. \n")  
                print("------------------")  
                game_choice(user_points, comp_points)

            if user_choice == 2 and computer_choice == 3:
                print("------------------")
                print("\nComputer wins a point. \n")
                print("------------------")              
                comp_points += 1
                
                print("Computer total points: ",comp_points)
                print("Your total points: ",user_points)
                print("------------------")
                winning_condition(user_points, comp_points)
                
                game_choice(user_points, comp_points)

    

            if user_choice == 3 and computer_choice == 1:
                print("------------------")
                print("\nComputer wins a point. \n")       
                print("------------------")         
                comp_points += 1
                
                print("Computer total points: ",comp_points)
                print("Your total points: ",user_points)
                print("------------------")
                winning_condition(user_points, comp_points)
                
                game_choice(user_points, comp_points)

            if user_choice == 3 and computer_choice == 2:
                print("------------------")
                print("\nYou win a point. \n")
                print("------------------")
                user_points += 1

                print("Computer total points: ",comp_points)
                print("Your total points: ",user_points)
                print("------------------")
                winning_condition(user_points, comp_points)
                
                game_choice(user_points, comp_points)

            if user_choice == 3 and computer_choice == 3:
                user_points = user_points
                comp_points = comp_points      
                print("------------------")   
                print("\nDraw. No points won. \n")  
                print("------------------")  
                game_choice(user_points, comp_points)

    game_choice(0, 0)
    
    

rockPaperScissors_game()