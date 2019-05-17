import xadmin
from .models import *


# Register your models here.
class NullAdmin(object):
    pass


class UserAdmin(object):
    list_display = ('nickname', 'email')
    search_fields = ['nickname', 'email']
    list_editable = ['nickname', 'email']


class PostAdmin(object):
    pass


xadmin.site.register(Post, NullAdmin)
xadmin.site.register(Plate, NullAdmin)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(Tag, NullAdmin)
xadmin.site.register(Review, NullAdmin)
xadmin.site.register(Rank, NullAdmin)
xadmin.site.register(Recommended, NullAdmin)