market_2nd = {'ns': 'green', 'ew':'red'} #dictionary

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red' + str(intersection) #this assert statement is needed because the way the code is written, no light will be red. Something needs to be red or cars will keep crashing into each other. Assertions are santiy checks

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
