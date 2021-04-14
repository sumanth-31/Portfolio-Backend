from rest.models import Post


def post_to_json(post: Post):
    json_post = {
        "id": post.post_id,
        "title": post.title,
        "content": post.content,
        "collection": post.collection.name,
        "tag": post.tag.name,
        "privacy": post.privacy
    }
    return json_post
