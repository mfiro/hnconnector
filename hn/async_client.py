import asyncio
import aiohttp
import datetime
import json
from aiohttp import ClientError, ClientResponseError

class aioClient:
    """The asnyc implementation of hn.Client"""
    base_url = 'https://hacker-news.firebaseio.com/v0/'

    def __init__(self):
        self._semaphore = asyncio.Semaphore(100)

    async def _request(self, url):
        async with self._semaphore:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        response.raise_for_status()  # Raises an exception for 400/500 status codes
                        try:
                            return await response.json()
                        except json.JSONDecodeError:
                            print("Error: Received non-JSON response")
                            return None  # Or handle it in another way
            except ClientResponseError as e:
                # Handles specific HTTP errors (e.g., 404 Not Found, 403 Forbidden)
                print(f"HTTP Error: {e.status} - {e.message}")
            except ClientError as e:
                # Handles client errors (e.g., connection failures)
                print(f"Client Error: {e}")
            except asyncio.TimeoutError:
                # Handles timeout error
                print("Timeout Error: The request took too long to complete")
            except Exception as e:
                # Handles other unspecified errors
                print(f"An unexpected error has occurred: {e}")
    
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
    
    async def get_item(self, item_id):
        """
        Fetches an item by its ID.

        Parameters:
            item_id (int): The ID of the item to fetch.

        Returns:
            dict: The item data, including a human-readable time if available.
        """

        url = self._makeurl(endpoint_name=f"item/{item_id}")
        item = await self._request(url)


        if item.get('time'):
            item['time_str'] = str(datetime.datetime.utcfromtimestamp(item['time']))
        return item

    async def get_topstories(self):
        """
        Fetches the top stories.

        Returns:
            list: A list of IDs for the top stories.
        """
        url = self._makeurl(endpoint_name='topstories')
        return await self._request(url)
    
    async def get_beststories(self):
        """
        Fetches the best stories.

        Returns:
            list: A list of IDs for the best stories.
        """
        url = self._makeurl(endpoint_name='beststories')
        return await self._request(url)
    
    async def get_newstories(self):
        """
        Fetches the latest stories.

        Returns:
            list: A list of IDs for the new stories.
        """
        url = self._makeurl(endpoint_name='newstories')
        return await self._request(url)
    
    async def get_maxitem(self):
        """
        Fetches the highest (newest) item ID.

        Returns:
            int: The highest item ID currently in the database.
        """
        url = self._makeurl(endpoint_name='maxitem')
        return await self._request(url)
    
    async def get_user(self, username):
        """
        Fetches user details by username.

        Parameters:
            username (str): The username of the user to fetch.

        Returns:
            dict: The user's details.
        """
        url = self._makeurl(endpoint_name=f'user/{username}')
        return await self._request(url)
    
    async def get_askstories(self):
        """
        Fetches the latest Ask HN stories.

        Returns:
            list: A list of IDs for the latest Ask HN stories.
        """
        url = self._makeurl(endpoint_name='askstories')
        return await self._request(url)
    
    async def get_showhn(self):
        """
        Fetches the latest Show HN stories.

        Returns:
            list: A list of IDs for the latest Show HN stories.
        """
        url = self._makeurl(endpoint_name='showstories')
        return await self._request(url)
    
    async def get_jobstories(self):
        """
        Fetches the latest job stories.

        Returns:
            list: A list of IDs for the latest job stories.
        """
        url = self._makeurl(endpoint_name='jobstories')
        return await self._request(url)
