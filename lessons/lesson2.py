"""if it's raining, tell me to pack umbrella"""

weather: str = input('"What is the weather like"')
if (weather == "rain"): 
    print("Pack an umbrella!")
else: 
    print("You don't need an umbrella")
    if (weather =="snow"): 
        print("Pack a jacket")
print("have a lovely day!")

