import requests
import datetime

class Client:
    base_url = 'https://hacker-news.firebaseio.com/v0/'

    def __init__(self):
        pass

    def _request(self, url):
        r = requests.get(url)
        r = r.json()
        return r
    
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
