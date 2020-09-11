from flask import jsonify


def error(err: str = "Error", code: int = 404):
    """Returns err message with status code"""
    response = dict(error=err)
    return jsonify(response), code


def success(data: dict = None, message: str = "", code: int = 200):
    """Returns success response with data or a message if any provided"""
    if data is not None:
        response = data
    elif message:
        response = {"message": message}  # type: ignore
    else:
        response = {"message": "Success"}  # type: ignore
    return jsonify(response), code
