import os

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "super-super-secret")

    from testAPI.stories.controllers import stories_api

    urls = (
        stories_api,
    )

    with app.app_context():
        for blueprint in urls:
            app.register_blueprint(blueprint)

    return app


application = create_app()

if __name__ == '__main__':
    application.run(use_reloader=False)
