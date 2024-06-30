# Prompt User Input for Weather
weather = input("What's the weather like today? (sunny/rainy/cold): ")
# Variables containing 'sunny', 'rainy', 'cold'
sunny = "sunny"
rainy = "rainy"
cold = "cold"

# Control-Flow using 'if', 'elif', 'else' conditions
if weather == sunny:
    print("Wear a t-shirt and sunglasses.")
elif weather == rainy:
    print("Don't forget your umbrella and a raincoat.")
elif weather == cold:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
