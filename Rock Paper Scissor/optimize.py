def rock_paper_scissors(choice1, choice2):
    if choice1 == choice2: return 0.5 # tie
    beat = {
        "rock" : "scissors",
        "paper" : "rock",
        "scissors" : "paper"
    }
    return 1 if beat[choice1] == choice2 else 0 # check if choice1 beat choice2
