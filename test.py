from main import Bored

bored = Bored()

# print(bored.get_activity())
# print(bored.get_activity_by_type(type='recreational'))
# print(bored.get_activity_by_id(key=1000000))
# print(bored.get_activity_by_accessibility(accessibility=0.05))
# print(bored.get_activity_by_price(price=0.02))
print(bored.get_activity_by_price_range(minprice=0, maxprice=1))




