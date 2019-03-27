import xadmin
from .models import *


# Register your models here.
class NullAdmin(object):
    pass


xadmin.site.register(Post, NullAdmin)
xadmin.site.register(Plate, NullAdmin)
xadmin.site.register(User, NullAdmin)
xadmin.site.register(Tag, NullAdmin)
xadmin.site.register(Review, NullAdmin)
xadmin.site.register(Rank, NullAdmin)




