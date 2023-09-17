n, k = map(int, input().split())
prices = list(map(int, input().split()))
cash = int(input())
print(cash-((sum(prices)-prices[k])//2))