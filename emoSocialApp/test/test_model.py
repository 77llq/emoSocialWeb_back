from django.test import TestCase
from emoSocialApp.models import User, UserProfile, Friends, FriendsRequest, Fans, Email, Moments, MomentsComment, MomentsLike, Board

class userModelTest(TestCase):
    def setUp(self):
        User.objects.create(id='123', account='usertest')

    def test_post_creation(self):
        user = User.objects.get(id='123')
        self.assertEqual(user.account,'usertest')
        self.assertEqual(user.id, '123')


class userProfileModelTest(TestCase):
    def setUp(self):
        UserProfile.objects.create(id=User.objects.create(id='profile1234', account='usertest'),name='tom',email='tom@123.com',birthday='2025-01-18')
    
    def test_post_creation(self):
        user = User.objects.get(id='profile1234')
        userProfile = UserProfile.objects.get(id=user)
        self.assertEqual(userProfile.email,'tom@123.com')
        self.assertEqual(userProfile.name,'tom')

class friendModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(id='123', account='usertest1')
        user2 = User.objects.create(id='1234', account='friend1')
        Friends.objects.create(userId=user1, friendId=user2, intimacy='200')
    
    def test_post_creation(self):
        user1 = User.objects.get(id='123')
        user2 = User.objects.get(id='1234')
        friends = Friends.objects.get(userId=user1)
        self.assertEqual(friends.friendId, user2)  
        self.assertEqual(friends.intimacy, '200')

class fansModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(id='123', account='usertest1')
        user2 = User.objects.create(id='1234', account='friend1')
        Fans.objects.create(userId=user1, fansId=user2)
    
    def test_post_creation(self):
        user1 = User.objects.get(id='123')
        user2 = User.objects.get(id='1234')
        fans = Fans.objects.get(userId=user1)
        self.assertEqual(fans.fansId, user2)  

class requestModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(id='123', account='usertest1')
        user2 = User.objects.create(id='1234', account='friend1')
        FriendsRequest.objects.create(sendRequestId=user1, receiveRequestId=user2) 

    def test_post_creation(self):
        user1 = User.objects.get(id='123')
        user2 = User.objects.get(id='1234')
        request = FriendsRequest.objects.get(sendRequestId=user1)
        self.assertEqual(request.receiveRequestId,user2)

class emailModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(id='123', account='usertest1')
        user2 = User.objects.create(id='1234', account='friend1')
        Email.objects.create(sendId=user1, receiveId=user2, emailTopic='emailtopic', emailContent='contentemail',sendTime='2025-03-07')
    
    def test_post_creation(self):
        user1 = User.objects.get(id='123')
        email = Email.objects.get(sendId=user1)
        self.assertEqual(email.emailTopic,'emailtopic')
        self.assertEqual(email.emailContent,'contentemail')
        self.assertEqual(email.sendTime,'2025-03-07')

class momentModelTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(id='123', account='usertest1')
        Moments.objects.create(postId=user1, postTime='2025-01-01', postContent='happy new year', postPic='picaddress', postVideo='videoaddress')

    def test_post_creation(self):
        user1 = User.objects.get(id='123')
        moment = Moments.objects.get(postId = user1)
        self.assertEqual(moment.postTime,'2025-01-01')
        self.assertEqual(moment.postContent,'happy new year')
        self.assertEqual(moment.postPic,'picaddress')
        self.assertEqual(moment.postVideo,'videoaddress')

class commentModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='123', account='usertest1')
        self.user2 = User.objects.create(id='1234', account='friend1')

        self.moment = Moments.objects.create(
            postId=self.user1,
            postTime='2025-01-01',
            postContent='happy new year'
        )

        self.comment = MomentsComment.objects.create(
            momentId=self.moment,
            commentId=self.user2,
            commentContent='you too'
        )


    def test_post_creation(self):
        comment = MomentsComment.objects.get(id=self.comment.id)
        self.assertEqual(comment.momentId, self.moment) 
        self.assertEqual(comment.commentId, self.user2) 
        self.assertEqual(comment.commentContent, 'you too')  

class likesModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='123', account='usertest1')
        self.user2 = User.objects.create(id='1234', account='friend1')

        self.moment = Moments.objects.create(
            postId=self.user1,
            postTime='2025-01-01',
            postContent='happy new year'
        )
        self.momentLikes = MomentsLike.objects.create(
            momentId = self.moment,
            likeId = self.user2
        )
    def test_post_creation(self):
        likes = MomentsLike.objects.get(id=self.momentLikes.id)
        self.assertEqual(likes.likeId, self.user2)

class boardModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(id='123', account='usertest1')

        self.board = Board.objects.create(
            postId=self.user1,
            postTopic='topic',
            postContent='content',
            postTime='2025-01-01'
        )
    def test_post_creation(self):
        board = Board.objects.get(postId = self.user1)
        self.assertEqual(board.postTopic,'topic')
        self.assertEqual(board.postContent,'content')
        self.assertEqual(board.postTime,'2025-01-01')