import logging
import sys

import requests
from testAPI.bootstrap import db_connection
from testAPI.stories.services import StoriesService

logger = logging.getLogger("Flask-Project-Logger")


def get_100_stories_v1():
    stories_service = StoriesService(db_connection)
    stories = list()
    for id in range(1, 101):
        url = f"https://jsonplaceholder.typicode.com/todos/{id}"
        response = requests.get(url=url)
        if response.status_code == 200:
            if response.json().get("completed"):
                stories.append(response.json())
        else:
            logger.error(f"{url} returned response with status code {response.status_code}.")

    stories_service.bulk_save_stories(stories)


def get_100_stories_v2():
    stories_service = StoriesService(db_connection)
    stories = list()
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/")
    if response.status_code == 200:
        for story in response.json():
            if story.get("completed"):
                stories.append(story)
        stories_service.bulk_save_stories(stories)
    else:
        logger.error(f"{response.url} returned response with status code {response.status_code}.")


if __name__ == '__main__':
    # Check input args
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if "-v1" in opts:
        get_100_stories_v1()
    elif "-v2" in opts:
        get_100_stories_v2()
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} (-v1 | -v2)\n"
                         f" <v1> using https://jsonplaceholder.typicode.com/todos/id\n"
                         f" <v2> using https://jsonplaceholder.typicode.com/todos/")

