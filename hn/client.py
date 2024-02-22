import requests
import datetime

class Client:
    base_url = 'https://hacker-news.firebaseio.com/v0/'

    def __init__(self):
        pass

    def _request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response.json()       # Return JSON response if request is successful
        except requests.exceptions.RequestException as e:
            # Handle connection errors, timeouts, and other request exceptions
            print(f"Request failed: {e}")
        except ValueError as e:
            # Handle JSON decoding errors
            print(f"Failed to decode JSON: {e}")
        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred: {e}")
    
    def _makeurl(self, endpoint_name, type_='json'):
        return f"{self.__class__.base_url}/{endpoint_name}.{type_}"
    
    def get_item(self, item_id):
        """
        item['descendants'] refers to the number of comments, if the item is story.
        item['score'] is the points
        """

        url = self._makeurl(endpoint_name=f"item/{item_id}")
        item = self._request(url)

        # Add a string represented time to the dict
        if item.get('time'):
            item['time_str'] = str(datetime.datetime.utcfromtimestamp(item['time']))
        return item

    def get_topstories(self):
        url = self._makeurl(endpoint_name='topstories')
        return self._request(url)
    
    def get_beststories(self):
        """It returns the id of the best stories.
        """
        url = self._makeurl(endpoint_name='beststories')
        return self._request(url)
    
    def get_newstories(self):
        url = self._makeurl(endpoint_name='newstories')
        return self._request(url)
    
    def get_maxitem(self):
        url = self._makeurl(endpoint_name='maxitem')
        return self._request(url)
    
    def get_user(self, username):
        url = self._makeurl(endpoint_name=f'user/{username}')
        return self._request(url)
    
    def get_askstories(self):
        """Returns up to 200 of the latest Ask HN
        """

        url = self._makeurl(endpoint_name='askstories')
        return self._request(url)
    
    def get_showhn(self):
        """Returns up to 200 of the latest Show HN
        """

        url = self._makeurl(endpoint_name='showstories')
        return self._request(url)
    
    def get_jobstories(self):
        """Returns up to 200 of the latest Job stories
        """

        url = self._makeurl(endpoint_name='jobstories')
        return self._request(url)
    



