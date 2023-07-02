hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
#prices for hairstyles 
prices = [30, 25, 40, 20, 20, 35, 50, 35]
#haircut numbers customer get last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0 
for price in prices:
  total_price += price
print("the total sum of price for hair cuts :", total_price) 
average_price = total_price/len(prices)
print("the average of price for hair cuts :",average_price)

#average price is more expensive than we thought it would be! So we cut all prices by 5 dollars
new_prices=[num-5 for num in prices]
print(new_prices)

number_of_hairstyles = len(hairstyles)
for i in range(0,number_of_hairstyles):
  print (i)
for i in range(len(hairstyles)):
  total_revenue += prices[i]*last_week[i]
print("Total Revenue: ",total_revenue)
average_daily_revenue =total_revenue/7
print("Average Daily Revenue :", average_daily_revenue)

# All of the haircuts she has that are under 30 dollars
cuts_under_30 = []
for i in range(len(new_prices)-1):
  if new_prices[i] < 30:
     cuts_under_30.append(hairstyles[i])
      
print(cuts_under_30)
