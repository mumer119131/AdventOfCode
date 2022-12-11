
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    
    cost = p
    bought = 0
    debug = []
    while s - cost > 0:

        s -= cost
        bought += 1


        print(cost, s)
        if s - cost - d <= m:
            cost = m
        else:
            cost -= d
        
    
    return bought


print(howManyGames(20 ,3 ,6,85))