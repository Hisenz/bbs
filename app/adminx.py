import xadmin
from .models import *


# Register your models here.
class NullAdmin(object):
    pass


class UserAdmin(object):
    list_display = ('nickname', 'email')
    search_fields = ['nickname', 'email']
    list_editable = search_fields


class PostAdmin(object):
    list_display = ('headline', 'user', 'give_a_like', 'read_num')
    search_fields = ['headline', 'user']
    list_editable = ['headline']


class TagAdmin(object):
    list_display = ('name', 'create_user')
    search_fields = ['name', 'create_user']


class RecommendedAdmin(object):
    list_display = ('post', 'create_time')
    search_fields = ['post']


class RankAdmin(object):
    list_display = ('post', 'rank')
    search_fields = ['post']


class PlateAdmin(object):
    list_display = ('name', 'create_user', 'audit')
    search_fields = ['name', 'create_user']
    list_editable = ['audit']


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Plate, PlateAdmin)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Review, NullAdmin)
xadmin.site.register(Rank, RankAdmin)
xadmin.site.register(Recommended, RecommendedAdmin)