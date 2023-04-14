import random
import pygame

def play_music(music_files, current_music):
    pygame.mixer.init()
    clock = pygame.time.Clock()

    music = pygame.mixer.Sound(music_files[current_music])
    music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(10)



def main():
    music_files = ["Queen - We Will Rock You (Official Video) (mp3cut.net) (1).mp3",
                   "Queen - The Show Must Go On (with lyrics) In memory of Freddie Mercury (mp3cut.net).mp3"]

    current_music = 0
    required_points = required(music_files, current_music)

    while True:
        player_points = 0
        computer_points = 0
        #music = pygame.mixer.Sound("Queen - We Will Rock You (Official Video) (mp3cut.net) (1).mp3")
        #music.play()
        #music()
        game(required_points, player_points, computer_points)
        #music.stop()
        if play_again(current_music, music_files) == "yes":
            current_music = (current_music+1) % len(music_files)
            play_music(music_files, current_music)

        else:
            break
            #music.stop()
            #music = pygame.mixer.Sound("Queen - The Show Must Go On (with lyrics) In memory of Freddie Mercury (mp3cut.net).mp3")
            #music.play()
        #else:


def game(required_points, player_points, computer_points):
    while win(required_points, player_points, computer_points):
        player_choice = player()
        available_choices = ["Rock", "Paper", "Scissor"]
        computer_choice = random.choice(available_choices)
        if player_choice == computer_choice:
            print("Computer choice: " + computer_choice)
            print("It's Tie")
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Rock" and computer_choice == "Scissor":
            print("Computer choice: " + computer_choice)
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Paper" and computer_choice == "Rock":
            print("Computer choice: " + computer_choice)
            print("Player wins")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        elif player_choice == "Scissor" and computer_choice == "Paper":
            print("Computer choice: " + computer_choice)
            print("Player wins!")
            player_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)

        else:
            print("Computer choice: " + computer_choice)
            print("Computer wins!")
            computer_points += 1
            print("Player points:" + str(player_points))
            print("Computer points:" + str(computer_points))
            print("=" * 40)


def win(required_points, player_points, computer_points):
    if int(player_points) == required_points:
        #music = pygame.mixer.Sound("Queen - We Are The Champions (Official Video) (mp3cut.net).mp3")
        #music.play()
        print("*" * 40)
        print("Player wins!!!!!!")
        print("CONGRATULATION!!!!!")
        print("*" * 40)
        return False

    elif int(computer_points) == required_points:
        print("*" * 40)
        print("Computer wins!!!!!")
        print("Sorry, try again")
        print("*" * 40)
        return False

    return True

def player():
    while True:
        try:
            available_choices = ["Rock", "Paper", "Scissor"]
            print("=" * 40)
            player_choice = input("Rock, Paper, Scissor: ").title()
            if player_choice in available_choices:
                return player_choice
            else:
                raise ValueError("YOUR CHOICE IS NOT APPROPRIATE")
        except ValueError:
            print("YOUR CHOICE IS NOT APPROPRIATE")
            pass

def required(music_files, current_music):
    while True:
        play_music(music_files, current_music)
        try:
            print("=" * 40)
            print("WELCOME TO THE GAME!")
            return int(input("Please, enter the required points: "))
        except ValueError:
            print("YOU SHOULD INPUT INTEGER")

def play_again(current_music, music_files):
    current_music = (current_music + 1) % len(music_files)
    available_answers = ["yes", "no"]
    while True:
        try:
            answer = str(input("Do you want to play again? YES/NO: ")).lower()
            try:
                if answer in available_answers:
                    return answer
                else:
                    raise ValueError
            except ValueError:
                print("YOU SHOULD INPUT YES OR NO")
        except ValueError:
            print("YOU SHOULD INPUT YES OR NO")


if __name__ == '__main__':
    main()