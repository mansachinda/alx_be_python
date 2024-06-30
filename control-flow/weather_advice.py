# Prompt User Input for Weather
user = input("What's the weather like today? (sunny/rainy/cold): ")
# Variables containing 'sunny', 'rainy', 'cold'
sunny = "sunny"
rainy = "rainy"
cold = "cold"

# Control-Flow using 'if', 'elif', 'else' conditions
if user == sunny:
    print("Wear a t-shirt and sunglasses.")
elif user == rainy:
    print("Don't forget your umbrella and a raincoat.")
elif user == cold:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
