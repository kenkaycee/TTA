"""
A motorbike costs £2000 and loses 10% of its value every year. Using a loop, 
print the value of the bike every following year until it falls below £1000.
"""

#solution
cost = 2000.0
print(f"The original cost of the bike is £{2000}")
while True:
  cost *= 0.9
  if cost < 1000.0:
    break 
  print(f"\nNext year, the value of the bike will decline to: £{round(cost,2)}")
