from rest.utils import bad_request


def invalid_user():
    return bad_request("No Such User Exists")
