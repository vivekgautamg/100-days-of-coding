def mincostTickets(days, costs):
        dp = [9999]*(days[-1] + 1)
        dp[0] = 0
        days_set = set(days)
        for i in range(1,len(dp)):
            if i in days_set:
                dp[i] = min(costs[0] + dp[i-1], costs[1] + dp[max(0,i-7)], costs[2] + dp[max(0,i-30)])
            else:
                dp[i] = dp[i-1]
        return dp[-1]
