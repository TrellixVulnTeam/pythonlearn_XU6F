

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")

weight=0
items=[]

for cargo in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("sorry over_limit, present weight = {}".format(weight))
        break
    else:
        weight+=cargo[1]
        items.append(cargo[0])

print(weight)
print(items)



# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 2")

weight=0
items=[]

for cargo,cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("sorry over_limit, present weight = {}".format(weight))
        break
    elif weight+cargo_weight >=100:
        continue
    else:
        weight+=cargo_weight
        items.append(cargo)

print(weight)
print(items)




# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
for sen in headlines:
    news_ticker += sen+" "
    if len(news_ticker) > 140:
        news_ticker =news_ticker[:140]
        break




print(news_ticker)