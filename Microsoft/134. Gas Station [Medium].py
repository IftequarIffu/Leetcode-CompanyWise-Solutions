class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # At any point, if we have less gas than required, there's no way
        if(sum(gas) < sum(cost)):
            return -1
        
        totalGas = 0
        ansIndex = 0
        chainContinuing = 0
        for i in range(len(gas)):

            totalGas = totalGas + (gas[i] - cost[i])

            if(totalGas < 0):
                totalGas = 0
                chainContinuing = 0
            else:
                if(chainContinuing == 0):
                    ansIndex = i
                    chainContinuing = 1
            
        return ansIndex