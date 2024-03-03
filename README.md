# hnconnector: An unofficial Hacker News API Client Library in Python

**hnconnector** is a lightweight Python library designed to simplify accessing the Hacker News API. With **hnconnector**, you can easily fetch stories, comments, user profiles, and other data from Hacker News with minimal setup. Whether you're building a custom Hacker News reader, analyzing Hacker News stories, or integrating Hacker News data into your projects, hnconnector provides a straightforward Pythonic interface to interact with Hacker News.

## Features
* Fetch top, new, and best stories from Hacker News
* Retrieve details about specific stories, comments, and users
* Access Ask HN, Show HN, and job stories
* Simple and intuitive API

## Installation
**hnconnector** can be installed using pip. Ensure you have Python 3.6 or higher installed on your system. To install **hnconnector**, open your terminal and run:

```bash
pip install hnconnector
```
## Quick Start
Here's a quick example to get you started by fetching the top stories from Hacker News:

```python
from hnconnector import Client

client = Client()

# Fetch top stories
top_stories = client.get_topstories()

print("Top 10 Hacker News Stories IDs:")
for story_id in top_stories[:10]:
    print(story_id)

# Fetch details for a specific story
story_details = client.get_item(top_stories[0])
print(f"Details of the top story: {story_details}")
```
## Usage
### Initializing the Client
Create an instance of the **Client** class to start interacting with the API:

```python
from hnconnector import Client

client = Client()
```
### Fetching Stories
You can fetch different types of stories (top, new, best, ask HN, show HN, and jobs) as follows:

```python
top_stories = client.get_topstories()
new_stories = client.get_newstories()
best_stories = client.get_beststories()
ask_stories = client.get_askstories()
show_stories = client.get_showhn()
job_stories = client.get_jobstories()()
```

### Retrieving an Item
To retrieve details about a specific item (story, comment, etc.), use its ID:

```python
item_id = 16582136
item_details = client.get_item(item_id)
print(item_details)
```

### Fetching User Profiles

```python
username = 'dang'
user_details = client.get_user(username)
print(user_details['karma'])
```

### Contributing
Contributions to **hnconnector** are welcome! 

### License
**hnconnector** is released under the MIT License. See the LICENSE file for more details.

### Contact
For questions or feedback regarding **hnconnector**, please open an issue on the GitHub repository: https://github.com/mfiro/hnconnector.
