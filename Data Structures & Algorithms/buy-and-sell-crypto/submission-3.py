class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #solved this one before but I forgot the solution lol, nvm I remember it

        '''
        BuyP, track the minimum item
        profit, track the profit and update when a greater profit is found


        BuyP = 10 - 10
        profit = 0
                  i
        [10,1,5,6,7,1]
        '''

        buyP = math.inf
        curProfit = 0

        for item in prices:
            if item < buyP:
                buyP = item
            
            curProfit = max(curProfit,(item-buyP))
        
        return curProfit
        