from app.models import Image


def create(image):

    new = Image()
    new.image = image
    new.save()
    return new
