# Rock-Paper-Sccisors
In this project, I investigated how different strategies affect outcomes in rock-paper-scissors, focusing on situations where players have an "edge." For example, I simulated a match-up where Player 1 throws rock half the time, while Player 2 throws scissors two-thirds of the time. This gives Player 1 a theoretical 9% advantage.

Through simulations, I found that despite this edge, Player 1 can still perform worse than the optimal random strategy about 5% of the time, simply due to chance. In rare cases, Player 1, despite the advantage, lost up to 17 times in a row. By experimenting with simulation sizes, I created empirical distributions that closely match the expected theoretical outcomes, revealing just how much randomness can impact results, even when an advantage exists.

![rps1billsim](https://github.com/user-attachments/assets/0739508e-2e13-45d2-b860-b62f2d572891)

Graph 1: Over 1 billion simulated trials, each averaging the win percentage across 100,000 games, reveal that when Player 1 has a 9% edge over the long run, they consistently come out ahead. With such a large sample size, Player 1’s advantage stabilizes, and they are always winning by the end of each trial set.

Graph 2: In a smaller simulation of only 100 games, repeated 10,000 times, the empirical distribution shows a different story. Here, even though Player 1 has an edge, shorter trial runs introduce more variability due to chance. This simulation reveals that Player 1 can still lose or perform below their optimal win rate, with the worst cases showing them losing up to 12 times in a row. This demonstrates how, over shorter runs, randomness can overshadow the theoretical advantage, leading to unexpected losing streaks.

![Figure_2](https://github.com/user-attachments/assets/4e7181ab-3d08-4c95-a75c-44d921c6d497)



a cool expermient with Central Limit therorem and variance based on sample size.
