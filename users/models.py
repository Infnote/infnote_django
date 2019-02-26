from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class UserManager(models.Manager):
    def create(self, user_id, **kwargs):
        if not user_id:
            raise ValueError('user_id is required.')

        user = self.model(user_id=user_id, **kwargs)
        user.save()

        return self.get(user_id=user_id)

    def get_by_natural_key(self, username):
        return self.get(email=username)


class User(models.Model):

    # User content
    user_id = models.CharField(max_length=100, primary_key=True)
    nickname = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=100, unique=True, null=False, blank=False)
    avatar = models.CharField(max_length=255, null=True)
    bio = models.CharField(max_length=255, null=True)

    # Key
    signature = models.CharField(max_length=100, null=True)

    # Local info
    topics = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    date_created = models.IntegerField(default=0)

    # Blockchain
    block_height = models.IntegerField(default=0)
    block_time = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['nickname', 'email', 'signature']

    class Meta:
        db_table = 'infnote_users'

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.nickname + ' : ' + self.email
