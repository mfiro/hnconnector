import requests
import datetime

class Client:
    """A Python client for the Hacker News API."""

    base_url = 'https://hacker-news.firebaseio.com/v0/'

    def __init__(self):
        """Initialize the Client with no additional configuration."""
        pass

    def _request(self, url):
        """Internal method to handle HTTP requests.

        Parameters:
            url (str): The complete URL to make the request to.

        Returns:
            dict: The JSON response from the API if the request is successful.
            None: If the request fails or the response cannot be decoded as JSON.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle connection errors, timeouts, and other request exceptions
            print(f"Request failed: {e}")
        except ValueError as e:
            # Handle JSON decoding errors
            print(f"Failed to decode JSON: {e}")
        return None # Return None on failure
    
    def _makeurl(self, endpoint_name, type_='json'):
        """
        Constructs a complete API URL.

        Parameters:
            endpoint_name (str): The specific API endpoint name.
            type_ (str): The response format, default is 'json'.

        Returns:
            str: The complete URL for the request.
        """
        return f"{self.__class__.base_url}/{endpoint_name}.{type_}"
    
    def get_item(self, item_id):
        """
        Fetches an item by its ID.

        Parameters:
            item_id (int): The ID of the item to fetch.

        Returns:
            dict: The item data, including a human-readable time if available.
        """

        url = self._makeurl(endpoint_name=f"item/{item_id}")
        item = self._request(url)

        if item.get('time'):
            item['time_str'] = str(datetime.datetime.utcfromtimestamp(item['time']))
        return item

    def get_topstories(self):
        """
        Fetches the top stories.

        Returns:
            list: A list of IDs for the top stories.
        """
        url = self._makeurl(endpoint_name='topstories')
        return self._request(url)
    
    def get_beststories(self):
        """
        Fetches the best stories.

        Returns:
            list: A list of IDs for the best stories.
        """
        url = self._makeurl(endpoint_name='beststories')
        return self._request(url)
    
    def get_newstories(self):
        """
        Fetches the latest stories.

        Returns:
            list: A list of IDs for the new stories.
        """
        url = self._makeurl(endpoint_name='newstories')
        return self._request(url)
    
    def get_maxitem(self):
        """
        Fetches the highest (newest) item ID.

        Returns:
            int: The highest item ID currently in the database.
        """
        url = self._makeurl(endpoint_name='maxitem')
        return self._request(url)
    
    def get_user(self, username):
        """
        Fetches user details by username.

        Parameters:
            username (str): The username of the user to fetch.

        Returns:
            dict: The user's details.
        """
        url = self._makeurl(endpoint_name=f'user/{username}')
        return self._request(url)
    
    def get_askstories(self):
        """
        Fetches the latest Ask HN stories.

        Returns:
            list: A list of IDs for the latest Ask HN stories.
        """
        url = self._makeurl(endpoint_name='askstories')
        return self._request(url)
    
    def get_showhn(self):
        """
        Fetches the latest Show HN stories.

        Returns:
            list: A list of IDs for the latest Show HN stories.
        """
        url = self._makeurl(endpoint_name='showstories')
        return self._request(url)
    
    def get_jobstories(self):
        """
        Fetches the latest job stories.

        Returns:
            list: A list of IDs for the latest job stories.
        """
        url = self._makeurl(endpoint_name='jobstories')
        return self._request(url)
