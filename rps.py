import numpy as np
import matplotlib.pyplot as plt
import time



def mult_to_rps(p_strat, n):
    p = np.random.multinomial(1, p_strat, size = n)
    ps = []
    for i in range(p.shape[0]):
        for j in range(p.shape[1]):
            if p[i][j] == 1:
                ps.append(ro_sham_bo[j])
                
    return ps


def rps_winner(player1, player2, throw):

    if   player1[throw] == 'R' and player2[throw] == 'R': return 0
    elif player1[throw] == 'R' and player2[throw] == 'P': return 2
    elif player1[throw] == 'R' and player2[throw] == 'S': return 1
    elif player1[throw] == 'P' and player2[throw] == 'R': return 1
    elif player1[throw] == 'P' and player2[throw] == 'P': return 0
    elif player1[throw] == 'P' and player2[throw] == 'S': return 2
    elif player1[throw] == 'S' and player2[throw] == 'R': return 2
    elif player1[throw] == 'S' and player2[throw] == 'P': return 1
    elif player1[throw] == 'S' and player2[throw] == 'S': return 0


def sim_rps(p1,p2,n,bet_size):
    p1w = 0
    p2w = 0
    p1wp = []
    p2wp = []
    
    
    for throw in range(1,n):
        winner = rps_winner(p1,p2,throw)
        if winner == 1:
            p1w += bet_size
            
        elif winner == 2: 
            p2w += bet_size
            
        p1wp.append((p1w/bet_size) / throw)
        p2wp.append((p2w/bet_size) / throw)
                
    return p1w, p2w, p1wp, p2wp


def print_plts(p1wp, p2wp,p1w,p2w):
    print('\n')
    print(f"player 1 profit: {(p1w-p2w)*bet_size}$")#, player2 profit: {(p2w-p1w)* bet_size}$")
    print(f"player 1 win pct: {round((p1wp[len(p1wp)-1])*100,2)}%, player 2 win pct: {round((p2wp[len(p2wp)-1])*100,2)}%, tie pct {
        round((1 - abs(((p2wp[len(p2wp)-1]) + (p1wp[len(p1wp)-1])))) * 100,2)}%")
    plt.figure()
    plt.plot(range(len(p1wp)), p1wp, label='p1')
    plt.plot(range(len(p2wp)), p2wp, label='p2')
    plt.axhline(y=1/3, color='r', linestyle='--', label='optimal')
    plt.legend()
    plt.show()
    print('\n')


def pct_favored(strat):
    highest_prob = np.max(strat)
    index = np.argmax(strat)

    if index == 0:
        return 'Rock', (highest_prob - (1/3)) / (1/3) * 100
    elif index == 1:
        return 'Paper', (highest_prob - (1/3)) / (1/3) * 100
    else:
        return 'Sccisors', (highest_prob - (1/3)) / (1/3) * 100







n = 10000
p = 2500
bet_size = 1
ro_sham_bo   = ['R','P','S']

player1_winnings_n_trials = []
player1_winpct_n_trials = []
p1_strat = np.random.rand(3)
p2_strat = np.random.rand(3)
p1_strat = p1_strat / np.sum(p1_strat)
p2_strat = p2_strat / np.sum(p2_strat)


for i in range(p):

    
    start_time = time.time() 
    player1 = mult_to_rps(p1_strat, n)
    player2 = mult_to_rps(p2_strat, n)
    
    p1w, p2w, p1wp, p2wp =  sim_rps(player1, player2, n, np.random.randint(1, 11))
    player1_winnings_n_trials.append(p1w - p2w)
    player1_winpct_n_trials.append(p1wp[-1])  
    end_time = time.time()
    iteration_time = end_time - start_time
        
    
   
    progress = i / p
    arrow = '█' * int(round(progress * 50) - 1)
    spaces = '░' * (50 - len(arrow))
    print(f"\r[{arrow}{spaces}] {int(progress * 100)}%  | Estimated sim time: {(iteration_time*p)/60:.2f} mins", end='\r')
    
    # print(f"player 1 profit: {(p1w-p2w)*bet_size}$")#, player2 profit: {(p2w-p1w)* bet_size}$")
    # if i % (p/5) == 0:
    #     print_plts(p1wp, p2wp,p1w,p2w)

    

print('\n')

favored1, favordpct1 = pct_favored(p1_strat)
favored2, favordpct2 = pct_favored(p2_strat)
print(f"p1 favored {favored1} by {round(favordpct1,2)}% | p2 favored {favored2} by {round(favordpct2,2)}%")
print(p1_strat, p2_strat)
print(f"mean win p1 over {n} trials and {p} events:", np.mean(player1_winnings_n_trials))
print(f"mean win pct p1 over {n} trials and {p} events: {round(np.mean(player1_winpct_n_trials),2)*100}%")