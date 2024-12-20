import nashpy as nash
import numpy as np

player1_payoff = np.array([[3, 1],
                           [0, 2]])

player2_payoff = np.array([[2, 1],
                           [0, 3]])


game = nash.Game(player1_payoff, player2_payoff)

equilibria = game.support_enumeration()

print("Nash Equilibria:")
for eq in equilibria:
    print(f"Player 1 strategy: {eq[0]}, Player 2 strategy: {eq[1]}")
