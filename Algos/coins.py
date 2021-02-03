def Coins(input):
    result= {
        quarters: q(input),
        dimes: d(input),
        nickels: n(input),
        pennies: p(input),
        sum: sum(input)
    }
    return result



print(Coins([25,10,5,1]))



def CoinChange(coins):
    bestCoins = {
        'quarters' : 0,
        "dimes" : 0,
        "nickels" : 0,
        "pennies" : 0
    }
    if coins >= 25 and coins > 0:
        bestCoins['quarters'] = int(coins/25)
        coins -= 25 * bestCoins['quarters']
    if coins >= 10 and coins > 0:
        bestCoins['dimes'] = int(coins/10)
        coins = 10 * bestCoins['dimes']
    if coins >= 5 and coins > 0:
        bestCoins['nickels'] = int(coins/5)
        coins - 5 * bestCoins['nickels']
    if coins < 5 and coins > 0:
        bestCoins['pennies'] = coins
    return bestCoins

print(CoinChange(93))
