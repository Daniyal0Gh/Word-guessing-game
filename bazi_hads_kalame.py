import random 

def get_input():
    while True:
        print('-'*10)
        user_input = input('Enter your guess : ')
        if user_input.isalpha():
            return user_input
        print('Your input was not correct. please enter again.')

def get_input_from_list(Words):
    user_input = get_input()
    while user_input.lower() not in Words:
          print('You should guess a word from the given words list!')
          print('Please enter a correct word')
          user_input = get_input()
    return user_input.lower()

def print_game_intro():
    print('-'*10)
    print('Hi, Welcome to the Guess Game')
    print('All words :', my_list)
    print('Please start gussing.')
    
def run_game(number_of_ruonds, Words):
    print_game_intro()
    print(f'number of guesses: {number_of_ruonds}')
    correct_word = random.choice(Words)
    for i in range(number_of_ruonds):
        user_input = get_input_from_list(Words)
        if user_input == correct_word:
            print('YOU WON!')
            return
        else:
            print('you guessed wrong!')
            print(f'please try again! number of rounds left: {number_of_ruonds-1-i}')
    print('shoma bakhtid!')

my_list = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
run_game(5, my_list)