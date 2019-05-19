from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # 首页
    path('', views.index, name='index'),
    # 登陆界面
    path('login/', views.login, name='login'),
    # 注册界面
    path('signup/', views.signup, name='signup'),
    # 注册用户
    path('register/', views.register, name='register'),
    # 注销
    path('logout/', views.logout, name='logout'),
    # 进入修改个人资料界面
    path('change/', views.to_change, name='change'),
    # 修改个人资料
    path('modify/', views.modify, name='modify'),
    # 进入发帖界面
    path('posting/', views.posting, name='posting'),
    # 用户展示
    path('showuser/',views.show_user, name='showuser'),
    # 创建板块
    path('create_plate/', views.create_plate, name='create_plate'),
    # 添加板块
    path('add_plate/', views.add_plate, name='add_plate'),
    # 创建标签
    path('create_tag/', views.create_tag, name='create_tag'),
    # 添加标签
    path('add_tag/', views.add_tag, name='add_tag'),
    # 添加帖子
    path('add_post/', views.add_post, name='add_post'),
    # 帖子展示
    path('show_post/', views.post, name='show_post'),
    # 添加点赞
    path('add_like/', views.add_like, name='add_like'),
    # 取消点赞
    path('reduce_like/', views.reduce_like, name='reduce_like'),
    # 添加评论
    path('add_review/', views.add_review, name='add_review'),
    # 展示帖子列表
    path('show_posts/', views.show_posts, name='show_posts'),
    # 动态登录
    path('dynamic_login/', views.dynamic_login, name='dynamic_login'),
    # 获取用户
    path('getuser/', views.get_user, name="get_user"),
    # 发送邮件
    path('sendmail/', views.sendmail, name="sendmail"),
    # 查询
    path('search/', views.search, name='search'),
    # 上传图片
    path('upload_image/', views.upload_image, name="uploadimage"),
    # 最新
    path('latest/', views.latest, name='latest'),
    # 添加回复
    path('addreply/', views.add_replay, name='addreplay'),
    # 修改密码
    path('changepassword/', views.change_password, name='changepassword'),
]

