import random


class Game:
    def __init__(self):
        self.boxes = list(range(1, 101))
        random.shuffle(self.boxes)

    def find_number(self, player_index):
        num_tries = 0
        current_box = player_index

        while num_tries < 50:
            num_tries += 1

            # Open the current box and check the number inside
            number_found = self.boxes[current_box - 1]

            if number_found == player_index:
                return 1

            # Move to the next box based on the number found
            current_box = number_found
        return 0

    def play_game(self):
        success = []
        for player_index in range(1, 101):
            success.append(self.find_number(player_index))
        return 1 if sum(success) == 100 else 0


def simulate_games(num_iterations):
    overall_success = []
    for _ in range(num_iterations):
        game = Game()
        overall_success.append(game.play_game())

    return sum(overall_success) / num_iterations


num_iterations = 10000
success_rate = simulate_games(num_iterations)
print(success_rate)
