
class Player:
    def __init__(self):
        self.num_wins = 0
        self.num_losses = 0
    def get_win_average(self):
        if self.num_wins + self.num_losses == 0 :
            return "-"
        else:
            win_avg = self.num_wins / (self.num_wins + self.num_losses)
            return format(round(win_avg, 3), ".3f")

def game_result(p1_move, p2_move):
    result = "draw"
    if p1_move == "rock":
        if p2_move == "paper":
            result = "player2"
        elif p2_move == "scissors":
            result = "player1"
    elif p1_move == "paper":
        if p2_move == "rock":
            result = "player1"
        elif p2_move == "scissors":
            result = "player2"
    else:#p1_move = "scissors"
        if p2_move == "rock":
            result = "player2"
        elif p2_move == "paper":
            result = "player1"
    return result



output = ""
while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    num_players, num_games = data

    num_games_total =  num_games * num_players *(num_players - 1)//2
    players = []
    for i in range(num_players):
        players.append(Player())

    for i in range(num_games_total):
        p1_num,  p1_move, p2_num, p2_move = input().split()
        p1_num, p2_num = int(p1_num), int(p2_num)
        result = game_result(p1_move, p2_move)
        if result == "player1":
            players[p1_num - 1].num_wins += 1
            players[p2_num - 1].num_losses += 1
        elif result == "player2":
            players[p2_num - 1].num_wins += 1
            players[p1_num - 1].num_losses += 1

    for player in players:
        output += str(player.get_win_average()) + "\n"
    output += "\n"
print(output.strip())
