from app.models import Tag, User

USER_NOT_EXIST = -1
TAG_IS_EXIST = 0
TAG_ADD_SUCCESS = 1
ERROR_CODE = 500
TAG_NAME_IS_NULL = -2


def add_tag(tag_name, description, user_id):
    if not user_id:
        return USER_NOT_EXIST
    if tag_name == "":
        return TAG_NAME_IS_NULL
    try:
        tag = Tag()
        tag.name = tag_name
        tag.description = description
        tag.create_user = User.objects.get(pk=user_id)
        tag.save()
        return TAG_ADD_SUCCESS
    except Exception as e:
        print(e)
        return TAG_IS_EXIST
