from testAPI.stories.models import Story
from testAPI.storage.repository import ConnectionManager, Repository


class StoriesService:

    def __init__(self, connection_manager: ConnectionManager):
        self.repository = Repository(Story, connection_manager)

    def get_stories_by_user_id(self, user_id: int):
        result = self.repository.filter_by(userId=user_id).all()
        return [story.serialize() for story in result] if result else None

    def get_story_by_id(self, id: int):
        result = self.repository.get_object(pk=id)
        return result.serialize() if result else None

    def get_stories_by_title(self, title: str):
        result = self.repository.filter(Story.title.like(f"%{title}%")).all()
        return [story.serialize() for story in result] if result else None

    def bulk_save_stories(self, data: list):
        stories = tuple(
            Story(
                userId=story.get("userId"),
                title=story.get("title")
            ) for story in data
        )
        self.repository.bulk_save(stories)
