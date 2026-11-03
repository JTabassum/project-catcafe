import argparse
import json
import tkinter as tk
import csv


#A player's informations including how many scores, special items, reset, and result funtcions. Also the level of difficulty the player chose. 
class Score():
    def __init__(self, points:int, score: int, level:int, total_special:int, enemy:int, player:int)->None:
        self.points=points
        self.score=score
        self.level=level
        self.total_special=total_special
        self.enemy=enemy
        self.player=player

    #points increase by 1 and score increases by 10, when bubbles is collected. 
    def bubble(self)->str:
        self.points+=1
        self.score+=10
        return(f'\n\nBubble:{self.points}')

    #score increases by 20 and special item increases by 1, when the player collect special item.
    def special_item_collection(self)->str:
        self.score+=20
        self.total_special+=1
        return(f'\n\nSpecial item:{self.total_special}')

    #for easy difficulty level score is reduced by 5 and enemy is increased by 1
    def easyEnemies_hit(self)->str:
        self.score-=5
        self.enemy+=1
        return(f'\n\nNumber of enimies:{self.enemy}')

    #for medium difficulty level score is reduced by 10 and enemy is increased by 1
    def mediumEnemies_hit(self)->str:
        self.score-=10
        self.enemy+=1
        return(f'\n\nNumber of enimies:{self.enemy}')

    #for hard difficulty level score is reduced by 15 and enemy is increased by 1
    def hardEnemies_hit(self)->str:
        self.score-=15
        self.enemy+=1
        return(f'\n\nNumber of enimies:{self.enemy}')

    #Display the current score of the player
    def current_score(self)->None:
        print(f'Current Score:{self.score}')

    #When moving to the next level reset the points, score, level, special score and enemy.
    def reset(self)->None:
        self.points=0
        self.score=0
        self.level=self.level+1
        self.total_special=0
        self.special_score=0
        #self.hit_fish=True
        self.enemy=0

    #Display a player's results.(score, points, enemy...)
    def result(self)->None:
        scores=[
            {'Player':self.player, 
             'Score':self.score, 
             'Points':self.points, 
             'Special_items':self.total_special, 
             'Number of enemy':self.enemy,
             'Level':self.level}
            ]
        with open('data.csv', 'a') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=['Player', 'Score', 'Points', 'Special_items', 'Number of enemy', 'Level' ])
            writer.writeheader()
            writer.writerows(scores)

#Checking the positinos of the player and coins, if it overlabs, increase score by 1           
def position()->None:
    score:int=0
    positions={
        "player":[{"x":10,"y":20}],
        "coins":[{"x":20,"y":45},{"x":35,"y":30}]
        }

    if positions["player"][0]["x"] == positions["coins"][0]["x"] and positions["player"][0]["y"] == positions["coins"][0]["y"] : 
        score+=1
    if positions["player"][0]["x"] == positions["coins"][1]["x"] and positions["player"][0]["y"] == positions["coins"][1]["y"] :
        score+=1

    return score


some=position()
print(f'{some}')

#moving to the next level
def next_level(level:int=0):
    if level==3:
        return 
    return next_level(level+1)

#Let the user to choose the difficulty level of the game
def difficulty():
        #want to find a way for case sensitive
        parser=argparse.ArgumentParser(description='Difficulty level of the game (easy, medium, hard)')
        parser.add_argument('-d','--difficulty', choices=['easy','medium','hard'], help='Enter the level of difficulty you want.' )
        return parser.parse_args()   

#In a GUI show who is the winner of the finished level
def winner(score:int)->None:
        root=tk.Tk()
        if(score>20):
            root.title('Win')
        else:
            root.title('Lost')
        label_1 = tk.Label(root, text=score, font=('Arial', 18))
        label_1.pack(padx=10, pady=5)
        root.mainloop()



###TESTING

player1 = Score(0, 0, 1, 0, 0, 1)
#player2 = Score(0, 0, 1, 0, 0, 2)

                                      
difficulty_level = difficulty().difficulty
def check_difficulty()->None:
    if difficulty_level=='easy' and player1:
        player1.easyEnemies_hit()
        #player2.easyEnemies_hit()
    elif difficulty_level=='medium' and player1:
        player1.mediumEnemies_hit()
        #player2.mediumEnemies_hit()
    elif difficulty_level=='hard' and player1:
        player1.hardEnemies_hit()
        #player2.hardEnemies_hit()
    else:
        print(f'Nothing')

check_difficulty()


player1.bubble()
player1.bubble()
player1.special_item_collection()

#player2.bubble()
#player2.easyEnemies_hit()



print("Player 1:")
player1.current_score()

print("Player 2:")
#player2.current_score()

#CSV test
player1.result()
#player2.result()

#winner
winner(player1.score)


#reset
player1.reset()
#player2.reset()

#csv
player1.result()
#player2.result()



           

    






       
'''

final_result:dict={"Player":self.player,"Score":self.score,"Points":self.points, "Special_items":self.total_special, "Number of enemy":self.enemy,"Level":self.level}
        with open('result.json','a')as results:
            json.dump(final_result,results,indent=2)
        with open("result.json") as results:
            data: dict = json.load(results)

        print(data["Player"],data["Score"],data["Points"],data["Special_items"],data["Number of enemy"],data["Level"])
        

#testing json
player = Score(0, 50, 1, 2, 3, 1)
player.result()

player2 = Score(0, 70, 1, 1, 2, 2)
player2.result()
 

#CSV test
player1 = Score(0, 50, 1, 2, 3, 1)
player2 = Score(0, 70, 1, 1, 2, 2)



print("Results saved!")                
'''








    


