def rps(p1, p2):
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock',
    }

    if p1 == p2: 
        return "Draw!"
    
    return "Player 1 won!" if rules[p1] == p2 else "Player 2 won!"


if __name__ == "__main__":

    print(rps('rock', 'scissors'))  # Player 1 won!
    print(rps('scissors', 'rock'))  # Player 2 won!
    print(rps('rock', 'rock'))      # Draw!

    assert rps('rock', 'scissors') == "Player 1 won!"
    assert rps('scissors', 'rock') == "Player 2 won!"
    assert rps('rock', 'rock') == "Draw!"
    
    print("Все тесты прошли ✅")
