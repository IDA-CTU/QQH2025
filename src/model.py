import numpy as np
import pandas as pd


class Model:

    def place_bets(
        self,
        summary: pd.DataFrame,
        opps: pd.DataFrame,
        inc: pd.DataFrame,
    ):
        min_bet = summary.iloc[0]["Min_bet"]
        N = len(opps)

        bets = np.zeros((N, 3))
        bets[np.arange(N), np.random.choice([0, 1, 2])] = min_bet
        bets = pd.DataFrame(
            data=bets, columns=["BetH", "BetA", "BetD"], index=opps.index
        )
        return bets
