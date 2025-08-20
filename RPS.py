import random #For computer to make random choices.

#List of acceptable choices
choices = ['rock', 'paper', 'scissors']

#Initializes rounds
roundNumber = 1

#Initialized scores
playerScore = 0
computerScore = 0

print('Welcome to Rock, Paper, Scissors!')
print('Type leave anytime to leave the game.')

while True :
    print(f'Round number {roundNumber}. Are you ready? 😏')
#Takes players input and enters it into a variable, as well as computer.
    playerChoice = input("Enter rock, paper, or scissors: ")
    computerChoice = random.choice(choices)


#Displays choices
    print(f'You chose {playerChoice}...')
    print(f'Computer chose {computerChoice}.')

#Allows user to leave game upon typing "leave"
    if playerChoice == "leave":
        print("Thanks for playing!")
        print("Final scores.")
        print(f"Your score: {playerScore}. Computer score: {computerScore}")
        break
    
#Return 
    if playerChoice not in choices:
        print("Invalid choice. Try again.")
        continue

#Tie, win, or loss check.    
    if playerChoice == computerChoice:
        print('You tied! Tense😬...')
        print(f'Current Score -> You: {playerScore}, Computer: {computerScore}')
   
    elif ((playerChoice == 'scissors' and computerChoice == 'paper') or \
         (playerChoice == 'paper' and computerChoice == 'rock') or \
         (playerChoice == 'rock' and computerChoice == 'scissors')): 

        print('You win! 🎉 Nice job. +1')
        playerScore += 1
        print(f'Current Score -> You: {playerScore}, Computer: {computerScore}')
        
    else:
        print('You lost. 😢 Try again!')
        computerScore += 1
        print(f'Current Score -> You: {playerScore}, Computer: {computerScore}')

    # Show who is currently winning
    if playerScore > computerScore:
        print("You're leading! 🏆")
    elif computerScore > playerScore:
        print("Computer is leading! 🤖")
    else:
        print("It's a tie so far! 🤝")

    roundNumber += 1





