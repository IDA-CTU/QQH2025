import pandas as pd

from model import Model
from environment import Environment

games = pd.read_csv("./data/games.csv", index_col=0, parse_dates=["Date", "Open"])

env = Environment(games, Model(), init_bankroll=1000, min_bet=1, max_bet=250)

evaluation = env.run()

print()
print(f"Final bankroll: {env.bankroll:.2f}")

history = env.get_history()
