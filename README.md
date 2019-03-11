# cpyWallPost
## 这是个十分简单的REST API，基本上就是个图床。暂时满足了个人需求，有bug欢迎提issue
使用[Django](https://www.djangoproject.com/)框架和[Django-REST-Framework](https://www.django-rest-framework.org/)构建

# API 列表：
- /cpyPosts/qr/{id} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//获取qr码
- /cpyPosts/add &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; //上传文件
- /cpyPosts/del/{id} &nbsp;&nbsp; //删除文件
- /cpyPosts/view/{id}  //查看文件
- /cpyPosts/edit/{id} &nbsp; //修改文件
