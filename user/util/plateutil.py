from django.db import IntegrityError

from user.models import Plate, User


def get(plate_pk):
    try:
        return Plate.objects.get(pk=int(plate_pk))
    except:
        return None


def get_for_audit(audit):
    try:
        return Plate.objects.filter(audit=audit)
    except:
        return None


def add_plate(name, description, user_id):
    if not user_id:
        return -1
    try:
        plate = Plate()
        plate.name = name
        plate.description = description
        plate.create_user = User.objects.get(pk=user_id)
        plate.save()
        return 1
    except IntegrityError as e:
        return 0
