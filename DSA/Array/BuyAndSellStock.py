# The approch for this kind of Question is 
# first find the smallest number from array 
# apply loop on array for remaining number to find maximum profit
# first take first element as Best Buy then check the profit 

def StockPrice(arr):
    MaxProfit = 0
    BestBuy = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > BestBuy: 
            MaxProfit = max(MaxProfit,arr[i] - BestBuy)
        
        BestBuy = min(BestBuy, arr[i])

    return MaxProfit 


if __name__ == '__main__':
    arr = [7,1,5,3,6,4]
    profit = StockPrice(arr)
    print('Max Profit is :', profit)