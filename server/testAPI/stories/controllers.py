from typing import Tuple

from flask import Blueprint, Response
from testAPI.response_messages import error, success
from testAPI.stories.services import StoriesService
from testAPI.bootstrap import db_connection

stories_api = Blueprint("stories_api", __name__, url_prefix="/")
stories_service = StoriesService(db_connection)


@stories_api.route("user/<int:userId>", methods=["GET"])
def get_stories_by_user_id(userId: int) -> Tuple[Response, int]:
    result = stories_service.get_stories_by_user_id(user_id=userId)
    if result:
        return success(data=result)
    else:
        return error("No stories associated with this user")


@stories_api.route("story/<int:id>", methods=["GET"])
def get_stories_by_story_id(id: int) -> Tuple[Response, int]:
    result = stories_service.get_story_by_id(id=id)
    if result:
        return success(data=result)
    else:
        return error("Story doesn't exist")


@stories_api.route("title/<title>", methods=["GET"])
def get_stories_by_title_match(title: str) -> Tuple[Response, int]:
    result = stories_service.get_stories_by_title(title=title)
    if result:
        return success(data=result)
    else:
        return error("No stories matching this title")
