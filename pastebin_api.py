'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = 'vvx2NDA3W-1jbugeuE47C2vBlYnlqu8K'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """
    # Data to be sent to the PasteBin API
    data = {
        "api_dev_key": API_DEV_KEY,
        "api_paste_data": body_text,
        "api_paste_name": title,
        "api_paste_expire_date": expiration,
        "api_paste_private": 0 if listed else 2,  # 0 for public, 2 for unlisted
        "api_paste_format": "python",  # You can modify this based on your paste content
    }

    # Make the request to PasteBin API
    response = requests.post(PASTEBIN_API_POST_URL, data=data)

    # Check if the paste was created successfully
    if response.text.startswith("Bad API request"):
        print("Error creating PasteBin paste:", response.text)
        return None
    else:
        paste_url = response.text
        print("PasteBin paste created successfully. URL:", paste_url)
        return paste_url

if __name__ == "__main__":
    # Example usage
    title = "My Paste"
    body_text = "This is the content of my paste."
    expiration = "1H"
    listed = True

    created_url = post_new_paste(title, body_text, expiration, listed)

    if created_url:
        print("Paste created successfully. URL:", created_url)
    else:
        print("Failed to create PasteBin paste.")