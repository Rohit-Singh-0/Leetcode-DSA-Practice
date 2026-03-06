class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute force
        max_profit = 0 #variable to store the maximum profit
        for buy in range(len(prices)): #traversing the prices array from 0 to len(prices) and this variable will correspond to the buy date
            for sell in range(buy+1, len(prices)):#traversing the prices array from buy to len(prices) and this variable will correspond to the sell date because we can only sell in future (after buying)
                max_profit = max(max_profit, prices[sell] - prices[buy]) #update the value of max_profit variable 
        return max_profit # return the max_profit

        #time = O(n^2)
        #space = O(1)

        #Optimal approach - two pointer
        max_profit = 0 #initialise a max_profit variable
        buy , sell = 0, 1 #initialise 2 pointers referencing the buy and sell index in prices array
        while sell < len(prices): # run the while loop untill the sell index reaches the len(prices) -1
            max_profit = max(max_profit, prices[sell]-prices[buy]) # update the max_profit
            if prices[sell] < prices[buy]:# if the sell price is less than the buy price then update the buy index
                buy = sell
            sell +=1 #increase the sell index by 1
        return max_profit # return the max_profit
         
        #time = O(n)
        #space = O(1)