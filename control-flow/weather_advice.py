# weather_advice.py

def get_weather_recommendation():
    """
    Prompts the user for current weather conditions and provides
    clothing recommendations based on the input.
    """
    # Prompt the user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
    # Convert input to lowercase to handle case-insensitivity (e.g., "Sunny" vs "sunny")

    # Provide clothing recommendations based on the user's input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        # Handle unexpected input
        print("Sorry, I don't have recommendations for this weather.")

# Call the function to run the program
if __name__ == "__main__":
    get_weather_recommendation()

