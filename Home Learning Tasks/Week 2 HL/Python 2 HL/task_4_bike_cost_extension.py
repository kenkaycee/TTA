"""As an extension to the motorbike task that costs
£2000 and loses 10% of its value every year. Set up
a function that performs the calculation by passing
in parameters. Then using a loop, print the value of
the bike every following year until it falls below
£1000"""    

#Solution
def bike_value():
  cost = int(input("Enter the purchase price of the bike: "))
  if cost == 2000:
    while True:
      cost *= 0.9
      if cost < 1000:
        break      
      print(f"Next year, the value of the bike will decline to: £{round(cost,2)}")
      
  else:
    print("\nPurchase price must be equals to 2000, please type in 2000")
    return bike_value()
bike_value()