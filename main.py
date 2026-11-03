
import argparse
import csv
import os
import tkinter as tk


# CHARACTER OPTIONS
c1 = "Calico"
c2 = "Siamese"
c3 = "Ragdoll"

t1 = "Hoodie"
t2 = "Apron"
t3 = "T-shirt"

b1 = "Jeans"
b2 = "Skirt"
b3 = "Shorts"


# CHARACTER CLASS
class Character:
    def __init__(self, name: str, breed: str, top: str,
                 bottoms: str, x: int = 0, y: int = 0):
        self.name = name
        self.breed = breed
        self.top = top
        self.bottoms = bottoms
        self.x = x
        self.y = y

    def display(self) -> None:
        print(f"\nYou are a {self.breed} cat named {self.name}!")
        print(f"You are wearing a {self.top} with {self.bottoms}.")


# RECURSIVE CHARACTER SELECTION
def choose_character() -> Character:
    print("\nCHOOSE YOUR CAT!")
    print("1.", c1)
    print("2.", c2)
    print("3.", c3)

    breed_choice = input("Choose your cat breed (1-3): ").strip()

    if breed_choice == "1":
        breed = c1
    elif breed_choice == "2":
        breed = c2
    elif breed_choice == "3":
        breed = c3
    else:
        print("Invalid choice. Try again.")
        return choose_character()

    name = input("Enter your cat's name: ").strip()

    if name == "":
        print("Your cat needs a name!")
        return choose_character()

    print("\nCHOOSE YOUR TOP!")
    print("1.", t1)
    print("2.", t2)
    print("3.", t3)

    top_choice = input("Choose your top (1-3): ").strip()

    if top_choice == "1":
        top = t1
    elif top_choice == "2":
        top = t2
    elif top_choice == "3":
        top = t3
    else:
        print("Invalid choice. Try again.")
        return choose_character()

    print("\nCHOOSE YOUR BOTTOMS!")
    print("1.", b1)
    print("2.", b2)
    print("3.", b3)

    bottoms_choice = input("Choose your bottoms (1-3): ").strip()

    if bottoms_choice == "1":
        bottoms = b1
    elif bottoms_choice == "2":
        bottoms = b2
    elif bottoms_choice == "3":
        bottoms = b3
    else:
        print("Invalid choice. Try again.")
        return choose_character()

    cat = Character(name, breed, top, bottoms)
    cat.display()

    return cat


# MOVEMENT CLASS
class Motion:
    def __init__(self, character: Character):
        self.character = character

    def reset(self) -> None:
        self.character.x = 0
        self.character.y = 0

    def left(self) -> None:
        if self.character.x > 0:
            self.character.x -= 1

        self.character.y = 0
        print("Swimming left!")

    def right(self) -> None:
        self.character.x += 1
        self.character.y = 0
        print("Swimming right!")

    def jump(self) -> None:
        self.character.x += 1
        self.character.y = 5
        print("Swimming upwards!")

    def crouch(self) -> None:
        self.character.x += 1
        self.character.y = -5
        print("Swimming downwards!")


# SCORE CLASS
class Score:
    def __init__(self, points: int, score: int, level: int,
                 total_special: int, enemy: int, player: int):

        self.points = points
        self.score = score
        self.level = level
        self.total_special = total_special
        self.enemy = enemy
        self.player = player

        self.health = 3
        self.max_health = 3
        self.pearls = 0

    # COLLECTING BUBBLES
    def bubble(self, difficulty: str) -> None:
        self.points += 1
        self.score += 10

        if difficulty == "easy":
            if self.health < self.max_health:
                self.health += 1

        elif difficulty == "medium":
            if self.points % 3 == 0:
                if self.health < self.max_health:
                    self.health += 1

        # Hard difficulty does not restore health.

        print("\nYou collected a bubble!")
        print("+10 points!")
        print(f"Health: {self.health}/{self.max_health}")

    # COLLECTING TREASURE
    def treasure(self) -> None:
        self.total_special += 1
        self.score += 20
        self.pearls += 20

        print("\nYou found a treasure!")
        print("+20 points!")
        print("+20 pearls!")

    # GETTING HIT BY AN ENEMY
    def enemy_hit(self, difficulty: str) -> None:
        self.enemy += 1
        self.health -= 1

        if difficulty == "easy":
            self.score -= 5

        elif difficulty == "medium":
            self.score -= 10

        elif difficulty == "hard":
            self.score -= 15

        print("\nYou were hit by an enemy!")
        print("You lost 1 health.")
        print(f"Health: {self.health}/{self.max_health}")

    # HITTING AN OBSTACLE
    def obstacle_hit(self, difficulty: str) -> None:
        self.score -= 5

        print("\nYou hit an obstacle!")

        if difficulty == "hard":
            self.health -= 1
            print("You lost 5 points and 1 health.")
        else:
            print("You lost 5 points.")

        print(f"Health: {self.health}/{self.max_health}")

# UNDERWATER LEVEL CLASS
class UnderwaterLevel:
    def __init__(self, character: Character, score: Score,
                 difficulty: str):

        self.character = character
        self.score = score
        self.difficulty = difficulty

        self.motion = Motion(character)

        self.game_over = False
        self.visited = set()

        # EASY DIFFICULTY
        if difficulty == "easy":
            self.length = 14

            self.bubbles = [1, 3, 5, 9, 11, 13]
            self.treasures = [4, 8]

            self.enemies = {
                6: "crouch"
            }

            self.obstacles = {
                2: "jump",
                10: "jump",
                12: "crouch"
            }

            self.required_bubbles = 5
            self.required_treasures = 1

        # MEDIUM DIFFICULTY
        elif difficulty == "medium":
            self.length = 20

            self.bubbles = [1, 3, 5, 7, 9, 11, 13, 15, 17]
            self.treasures = [4, 8, 12]

            self.enemies = {
                6: "crouch",
                14: "jump"
            }

            self.obstacles = {
                2: "jump",
                10: "crouch",
                16: "jump",
                18: "crouch"
            }

            self.required_bubbles = 6
            self.required_treasures = 2

        # HARD DIFFICULTY
        else:
            self.length = 26

            self.bubbles = [
                1, 3, 5, 7, 9, 11,
                13, 15, 17, 19, 21, 23
            ]

            self.treasures = [4, 8, 12, 16]

            self.enemies = {
                6: "crouch",
                14: "jump",
                20: "crouch"
            }

            self.obstacles = {
                2: "jump",
                10: "crouch",
                18: "jump",
                22: "crouch",
                24: "jump"
            }

            self.required_bubbles = 8
            self.required_treasures = 3

    # WARN THE PLAYER ABOUT WHAT IS AHEAD
    def show_warning(self) -> None:
        next_position = self.character.x + 1

        if next_position in self.enemies:
            print("\nWARNING! An enemy is approaching!")
            print("You can avoid it by:", self.enemies[next_position].upper())

        elif next_position in self.obstacles:
            print("\nWARNING! An obstacle is approaching!")
            print("You can avoid it by:", self.obstacles[next_position].upper())

    # CHECK WHAT THE PLAYER ENCOUNTERS
    def check_location(self, action: str) -> None:
        position = self.character.x

        if position in self.visited:
            return

        self.visited.add(position)

        # BUBBLES
        if position in self.bubbles:
            self.score.bubble(self.difficulty)

        # TREASURE
        elif position in self.treasures:
            self.score.treasure()

        # ENEMIES
        elif position in self.enemies:
            required_action = self.enemies[position]

            if action == required_action:
                print("\nYou successfully avoided the enemy!")

            else:
                self.score.enemy_hit(self.difficulty)

                if self.score.health <= 0:
                    self.game_over = True

        # OBSTACLES
        elif position in self.obstacles:
            required_action = self.obstacles[position]

            if action == required_action:
                print("\nYou successfully avoided the obstacle!")

            else:
                self.score.obstacle_hit(self.difficulty)

                if self.score.health <= 0:
                    self.game_over = True

    # DISPLAY GAME INFORMATION
    def show_status(self) -> None:
        print("\n-------------------------")
        print("UNDERWATER ADVENTURE")
        print("-------------------------")
        print(f"Position: {self.character.x}/{self.length}")
        print(f"Health: {self.score.health}/{self.score.max_health}")
        print(f"Score: {self.score.score}")
        print(f"Bubbles: {self.score.points}")
        print(f"Treasures: {self.score.total_special}")
        print(f"Pearls: {self.score.pearls}")
        print("-------------------------")

    # PLAY THE LEVEL
    def play(self) -> bool:
        print("\nWelcome to the Underwater Adventure!")
        print("Swim through the ocean and collect bubbles and treasure.")
        print("Avoid enemies and obstacles to reach the end!")

        print("\nMOVEMENT:")
        print("R = Right")
        print("L = Left")
        print("J = Jump")
        print("C = Crouch")

        self.motion.reset()

        while self.character.x < self.length and not self.game_over:

            self.show_status()
            self.show_warning()

            action = input("\nWhat would you like to do?\n" "R = Right\n" "L = Left\n"  "J = Jump\n" "C = Crouch\n""Enter your choice: ").strip().lower()

            if action in ["r", "right"]:
                self.motion.right()
                action = "right"

            elif action in ["l", "left"]:
                self.motion.left()
                action = "left"

            elif action in ["j", "jump"]:
                self.motion.jump()
                action = "jump"

            elif action in ["c", "crouch"]:
                self.motion.crouch()
                action = "crouch"

            else:
                print("Invalid movement. Try again.")
                continue

            self.check_location(action)

        if self.game_over:
            print("\nGAME OVER!")
            print("You ran out of health.")
            return False

        # CHECK IF THE PLAYER COLLECTED ENOUGH ITEMS
        if (self.score.points >= self.required_bubbles
                and self.score.total_special >= self.required_treasures):

            print("\nLEVEL COMPLETE!")
            print("You collected enough bubbles and treasure!")
            return True

        else:
            print("\nLEVEL INCOMPLETE!")
            print("You reached the end, but did not collect enough items.")
            return False


# DIFFICULTY SELECTION
def difficulty():
    parser = argparse.ArgumentParser(
        description="Choose the difficulty of Underwater Adventure."
    )

    parser.add_argument(
        "-d", "--difficulty",
        choices=["easy", "medium", "hard"],
        default=None,
        help="Choose easy, medium or hard."
    )

    settings = parser.parse_args()

    if settings.difficulty is None:

        while True:
            print("\nCHOOSE YOUR DIFFICULTY!")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")

            choice = input("Enter 1, 2, or 3: ").strip()

            if choice == "1":
                settings.difficulty = "easy"
                break

            elif choice == "2":
                settings.difficulty = "medium"
                break

            elif choice == "3":
                settings.difficulty = "hard"
                break

            else:
                print("Invalid choice. Try again.")

    return settings


# SAVE CHARACTER INFORMATION
def save_character(character: Character) -> None:
    with open("Character.txt", "w") as file:
        file.write(f"Name: {character.name}\n")
        file.write(f"Breed: {character.breed}\n")
        file.write(f"Top: {character.top}\n")
        file.write(f"Bottoms: {character.bottoms}\n")


# SAVE GAME RESULTS
def save_result(character: Character, score: Score,
                difficulty_level: str, completed: bool,
                game_over: bool) -> None:

    filename = "data.csv"

    fields = [
        "Player",
        "Name",
        "Breed",
        "Score",
        "Bubbles_Collected",
        "Special_items",
        "Pearls",
        "Number_of_enemy",
        "Health",
        "Level",
        "Difficulty",
        "Completed",
        "Game_Over"
    ]

    file_exists = os.path.exists(filename)

    # CHECK IF THE CSV FILE ALREADY HAS THE CORRECT HEADERS
    if file_exists:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            old_fields = next(reader, [])

        if old_fields and old_fields != fields:
            print("\nYour data.csv file has different columns.")
            print("Please rename or remove the old file before saving.")
            return

    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writeheader()

        writer.writerow({
            "Player": score.player,
            "Name": character.name,
            "Breed": character.breed,
            "Score": score.score,
            "Bubbles_Collected": score.points,
            "Special_items": score.total_special,
            "Pearls": score.pearls,
            "Number_of_enemy": score.enemy,
            "Health": score.health,
            "Level": score.level,
            "Difficulty": difficulty_level,
            "Completed": completed,
            "Game_Over": game_over
        })

    print("\nYour game results have been saved!")


# DISPLAY HIGH SCORE
def show_high_score() -> None:
    filename = "data.csv"

    if not os.path.exists(filename):
        print("\nNo high scores yet!")
        return

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)

            scores = []

            for row in reader:
                scores.append(int(row["Score"]))

            if len(scores) == 0:
                print("\nNo high scores yet!")

            else:
                print("\nHIGH SCORE:", max(scores))

    except (ValueError, KeyError):
        print("\nUnable to read the high score data.")


# TKINTER RESULTS WINDOW
def show_results(character: Character, score: Score,
                 completed: bool, game_over: bool,
                 difficulty_level: str) -> None:

    root = tk.Tk()
    root.title("Underwater Adventure Results")
    root.geometry("400x450")

    if game_over:
        heading = "GAME OVER"

    elif completed:
        heading = "LEVEL COMPLETE!"

    else:
        heading = "LEVEL INCOMPLETE"

    title = tk.Label(
        root,
        text=heading,
        font=("Arial", 20, "bold")
    )
    title.pack(pady=15)

    name_label = tk.Label(
        root,
        text=f"Cat: {character.name} ({character.breed})",
        font=("Arial", 12)
    )
    name_label.pack(pady=5)

    difficulty_label = tk.Label(
        root,
        text=f"Difficulty: {difficulty_level.capitalize()}",
        font=("Arial", 12)
    )
    difficulty_label.pack(pady=5)

    score_label = tk.Label(
        root,
        text=f"Final Score: {score.score}",
        font=("Arial", 14, "bold")
    )
    score_label.pack(pady=10)

    health_label = tk.Label(
        root,
        text=f"Health: {score.health}/{score.max_health}",
        font=("Arial", 12)
    )
    health_label.pack(pady=5)

    bubble_label = tk.Label(
        root,
        text=f"Bubbles Collected: {score.points}",
        font=("Arial", 12)
    )
    bubble_label.pack(pady=5)

    treasure_label = tk.Label(
        root,
        text=f"Treasures Collected: {score.total_special}",
        font=("Arial", 12)
    )
    treasure_label.pack(pady=5)

    pearl_label = tk.Label(
        root,
        text=f"Pearls: {score.pearls}",
        font=("Arial", 12)
    )
    pearl_label.pack(pady=5)

    enemy_label = tk.Label(
        root,
        text=f"Enemy Hits: {score.enemy}",
        font=("Arial", 12)
    )
    enemy_label.pack(pady=5)

    close_button = tk.Button(
        root,
        text="Close Game",
        command=root.destroy
    )
    close_button.pack(pady=20)

    root.mainloop()


# START THE GAME
def start() -> None:

    print("==============================")
    print("      PROJECT CAT CAFE")
    print("==============================")

    # CHOOSE DIFFICULTY
    settings = difficulty()
    difficulty_level = settings.difficulty

    # CHOOSE CHARACTER
    cat = choose_character()

    # SAVE CHARACTER INFORMATION
    save_character(cat)

    # CREATE SCORE
    game_score = Score(
        0,      # Bubbles collected
        0,      # Score
        1,      # Level
        0,      # Treasures
        0,      # Enemy hits
        1       # Player number
    )

    # CREATE AND PLAY THE LEVEL
    underwater = UnderwaterLevel(
        cat,
        game_score,
        difficulty_level
    )

    completed = underwater.play()

    game_over = underwater.game_over

    # SAVE RESULTS
    save_result(
        cat,
        game_score,
        difficulty_level,
        completed,
        game_over
    )

    # DISPLAY FINAL INFORMATION
    print("\nFINAL RESULTS")
    print("Score:", game_score.score)
    print("Health:", game_score.health)
    print("Bubbles:", game_score.points)
    print("Treasures:", game_score.total_special)
    print("Pearls:", game_score.pearls)
    print("Enemy hits:", game_score.enemy)

    show_high_score()

    # OPEN RESULTS WINDOW
    show_results(
        cat,
        game_score,
        completed,
        game_over,
        difficulty_level
    )


# RUN THE GAME
if __name__ == "__main__":
    start()

