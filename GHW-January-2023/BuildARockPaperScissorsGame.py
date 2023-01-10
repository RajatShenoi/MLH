import maskpass
import os

print("Only two players may play the game")
print("Type 'r' for rock, 'p' for paper, and 's' for scissors")

score_a = 0
score_b = 0

_ = input("Press enter to begin")
os.system('clear')

while True:
    print("Player 1 score: " + str(score_a))
    print("Player 2 score: " + str(score_b))
    move_a = 'a'
    while True:
        move_a = maskpass.askpass(prompt="Player 1 move: ").lower()
        if move_a == 'r' or move_a == 'p' or move_a == 's':
            break
        else:
            print("Inavlid Move, try again with 'r', 'p', or 's'")
    move_b = 'a'
    while True:
        move_b = maskpass.askpass(prompt="Player 2 move: ").lower()
        if move_b == 'r' or move_b == 'p' or move_b == 's':
            break
        else:
            print("Invalid Move, try again with 'r', 'p', or 's'")
    if move_a == move_b:
        print("Tie!")
    if move_a == 'r' and move_b == 'p':
        print("Player 2 wins!")
        score_b += 1
    if move_a == 'r' and move_b == 's':
        print("Player 1 wins!")
        score_a += 1
    if move_a == 'p' and move_b == 'r':
        print("Player 1 wins!")
        score_a += 1
    if move_a == 'p' and move_b == 's':
        print("Player 2 wins!")
        score_b += 1
    if move_a == 's' and move_b == 'p':
        print("Player 1 wins!")
        score_a += 1
    if move_a == 's' and move_b == 'r':
        print("Player 2 wins!")
        score_b += 1
    print("Player 1 played " + move_a)
    print("Player 2 played " + move_b)
    _ = input("Press enter to continue")
    os.system('clear')
