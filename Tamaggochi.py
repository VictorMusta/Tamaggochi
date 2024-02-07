import time
from random import randrange


class Pet(object):
    colors = ['red', 'blue', 'green', 'yellow']
    sad_vocab = ['Grrrrr...', 'Meow...', 'Woaf...', ':O', ':/', ';(']
    happy_vocab = [':D', ':P', ':)', 'UwU', '^^', 'Nya~', 'Meow!', 'Woaf!']
    species = ['cat', 'dog', 'horse', 'whale', 'dinosaur', 'julien']
    max_hunger = 10
    max_happiness = 10
    warning_limit = 3

    def mood(self):
        if self.hunger > self.warning_limit or self.happiness > self.warning_limit:
            return 'Happy'
        return 'Sad'

    def __init__(self, name):
        self.name = name
        self.color = self.colors[randrange(0, len(self.colors))]
        self.hunger = randrange(1, self.max_hunger)
        self.happiness = randrange(1, self.max_happiness)
        self.species = self.species[randrange(0, len(self.species))]
        self.life_speed = randrange(1, 4)

    def __str__(self):
        return f'Your {self.species} named {self.name} is {self.mood()}'

    def talk(self):
        if self.mood() == 'Sad':
            print(self.sad_vocab[randrange(0, len(self.sad_vocab))])
        else:
            print(self.happy_vocab[randrange(0, len(self.happy_vocab))])

    def win_game(self):
        self.happiness += randrange(1, self.max_happiness - self.happiness)

    def loose_game(self):
        self.happiness -= randrange(1, 2)
        print(self.sad_vocab[randrange(0, len(self.sad_vocab))])

    def play_game(self):
        your_score = randrange(0, 10)
        pet_score = randrange(0, 10)
        print("Higher score wins!")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Your score is", your_score)
        print(f'{self.name}\'s score is {your_score}')
        if your_score > pet_score:
            self.loose_game()
        else:
            self.win_game()

    def pass_time(self):
        self.happiness -= 1
        self.hunger -= 1
        if self.mood() == 'Sad':
            print(self, '\n')
            print('You should feed or play with him now!!!')

    def play_with(self):
        pass
