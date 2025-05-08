"""
Assignment Overview:

You are building a Dog Image Browser using the Dog CEO REST API.

The app should allow users to:
- View a list of all available dog breeds
- Get a random image of a breed
- Get a random image of a sub-breed

You will be using the Dog CEO API: https://dog.ceo/dog-api/

Your app should display a main menu with the following options:
1. Show all breeds
2. Get a random image from a breed
3. Get a random image from a sub-breed
4. Exit

The system should handle the following errors:
- Handling errors when a user enters an invalid menu option
- Handling errors when a user enters a breed that does not exist
- Handling errors when a user enters a sub-breed that does not exist
- Handling connection errors when calling the API

If there is an error you should print your own custom error message to the user and allow them to try again.
- Hint: you can use a while loop + try / except blocks to handle this

You should use try / except blocks to handle these errors.

You can either use the should use the requests library or the http.client library to make your requests

"""


import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get(f"https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        if "message" in data:
            return data["message"]
        else:
            print("Error: Unexpected API response structure!")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch breed list from API. Details: {e}")
        return {}

def get_random_image(breed):
    """GET request to fetch a random image from a breed."""
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/images/random
    # TODO: Return the image URL or handle errors
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        response.raise_for_status()
        data = response.json()
        if "message" in data:
            return data ['message']
        else:
            print("Error: Unexpected API response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch random breed image from API. Details: {e}")
        return None


   

def get_random_sub_breed_image(breed, sub_breed):
    """GET request to fetch a random image from a sub-breed."""
    # TODO: Make a request to https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random
    # TODO: Return the image URL or handle errors
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        if "message" in data:
            return data ['message']
        else:
            print("Error: Unexpected API response.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not fetch random image for sub-breed '{sub_breed}'. Details: {e}")
        return None

def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    # TODO: Print all breeds (sorted), 5 per line
    breed_list = sorted(breeds_dict.keys())
    for i in range(0, len(breed_list), 5):
        print(" | ".join(breed_list[i:i+5]))

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            if breeds:
                show_breeds(breeds)

        elif choice == "2":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            if breed in breeds:
                image_url = get_random_image(breed)
                if image_url:
                    print(f"Random image of {breed}: {image_url}")
            else:
                print(f"Error: {breed} is not an existing breed at this time.")
            # TODO: Check if breed exists and fetch image
            # TODO: Print image URL or error message

        elif choice == "3":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            if breed in breeds and breeds[breed]:
                print(f"Available sub-breeds: {','.join(breeds[breed])}")
                sub_breed = input("Enter sub-breed name: ").strip().lower()
                if sub_breed in breeds[breed]:
                    image_url = get_random_sub_breed_image(breed, sub_breed)
                    if image_url:
                        print(f"Random image of {breed} ({sub_breed}): {image_url}")
                else:
                    print(f"Error: '{sub_breed}' is not a valid sub-breed of {breed}.")
            else:
                print(f"Error: '{breed}' is not a valid breed with sub-breeds.")
            # TODO: Check if breed has sub-breeds
            # TODO: Ask for sub-breed, check if valid, then fetch image
            # TODO: Print image URL or error message

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
