from django.db import models


# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    account = models.CharField(max_length=16, verbose_name="账号", unique=True)
    password = models.CharField(max_length=255, verbose_name="密码")
    type = models.CharField(max_length=16, verbose_name="用户类型", default="普通用户")
    idNumber = models.CharField(max_length=32, verbose_name="身份证号")

    def __str__(self):
        return self.id


class UserProfile(models.Model):
    id = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=16, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱")
    gender = models.CharField(max_length=16, verbose_name="性别")
    birthday = models.DateField(verbose_name="生日")
    avatar = models.CharField(max_length=255, verbose_name="头像", null=True,
                              default='src/profile_bp/defaultAvatar.jpg')
    signature = models.CharField(max_length=32, verbose_name="个性签名", null=True)
    profileBp = models.CharField(max_length=255, verbose_name="背景图片", null=True, default='src/profile_bp/defaultBp.jpg')

    def __str__(self):
        return self.id


class Friends(models.Model):
    userId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='用户id')
    friendId = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='用户好友id')
    intimacy = models.CharField(max_length=255, verbose_name="情感密度", default='0')

    def __str__(self):
        return f"{self.userId}"


class FriendsRequest(models.Model):
    sendRequestId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='发出请求id')
    receiveRequestId = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='接受请求id')

    def __str__(self):
        return f"{self.sendRequestId}"


class Fans(models.Model):
    userId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='关注的人id')
    fansId = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='粉丝id')

    def __str__(self):
        return f"{self.userId}"


class Email(models.Model):
    sendId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='发件人id')
    receiveId = models.ForeignKey('User', on_delete=models.CASCADE, null=True, related_name='收件人id')
    emailTopic = models.CharField(max_length=32, verbose_name='邮件主题')
    emailContent = models.CharField(max_length=255, verbose_name='邮件内容')
    sendTime = models.CharField(max_length=64, verbose_name='发送时间')

    def __str__(self):
        return f"{self.sendId}"


class Moments(models.Model):
    postId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='发布人id')
    postTime = models.CharField(max_length=64, verbose_name='发布时间')
    postContent = models.CharField(max_length=255, verbose_name='发布内容')
    postPic = models.CharField(max_length=255, verbose_name='发布图片地址', null=True)
    postVideo = models.CharField(max_length=255, verbose_name='发布视频地址', null=True)

    def __str__(self):
        return f"{self.id}"


class MomentsComment(models.Model):
    momentId = models.ForeignKey('Moments', on_delete=models.CASCADE, related_name='所属朋友圈id')
    commentId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='评论人id', null=True)
    commentContent = models.CharField(max_length=64, verbose_name='评论内容', null=True)

    def __str__(self):
        return f"{self.id}"


class MomentsLike(models.Model):
    momentId = models.ForeignKey('Moments', on_delete=models.CASCADE, related_name='点赞朋友圈id')
    likeId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='点赞人id', null=True)

    def __str__(self):
        return f"{self.id}"


class Board(models.Model):
    postId = models.ForeignKey('User', on_delete=models.CASCADE, related_name='公告发布人id')
    postTopic = models.CharField(max_length=64, verbose_name='公告标题', null=False)
    postContent = models.CharField(max_length=255, verbose_name='公告内容', null=False)
    postTime = models.CharField(max_length=64, verbose_name='发布时间', null=False)

    def __str__(self):
        return f"{self.postId}"
