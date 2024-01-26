class Solution:
    def numberToWords(self, num: int) -> str:

        ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        
        def recursiveFunction(n):

            if(n==0):
                return ""

            if(n<=19):
                return ones[n-1]

            if(n<=99):
                return tens[(n//10)-2] + " " + recursiveFunction(n%10).strip()

            if(n<=999):
                return ones[(n//100)-1] + " " + "Hundred" + " " + recursiveFunction(n%100).strip()

            if(n<=999999):
                return recursiveFunction(n//1000).strip() + " " + "Thousand" +  " " + recursiveFunction(n%1000).strip()

            if(n<=999999999):
                return recursiveFunction(n//1000000).strip() + " " + "Million" + " " + recursiveFunction(n%1000000).strip()
            
            if(n<=999999999999):
                return recursiveFunction(n//1000000000).strip() + " " + "Billion" + " " + recursiveFunction(n%1000000000).strip()






        if(num==0):
            return "Zero"

        ans = recursiveFunction(num)
        return ans.strip()




        