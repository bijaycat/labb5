'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    cleaned_pokemon_name = str(pokemon_name).strip().lower()

    # TODO: Build a clean URL and use it to send a GET request
    pi_url = f"{POKE_API_URL}{cleaned_pokemon_name}/"

    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    try:
        # Send GET request to PokeAPI
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad responses

        # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
        pokemon_info = response.json()
        print(f"Successfully fetched information for {pokemon_info['name']} (ID: {pokemon_info['id']}).")
        return pokemon_info

    # TODO: If the GET request failed, print the error reason and return None
    except requests.exceptions.RequestException as e:
        # If the GET request failed, print the error reason and return None
        print(f"Error fetching Pokemon information: {e}")

    return

if __name__ == '__main__':
    main()