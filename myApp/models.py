from django.db import models
from datetime import datetime
class Meta:
        managed = False
        db_table = 'auth_group'
class AuthGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=80)

class AuthGroupPermissions(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)


    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField( max_length=2000)
    time_post = models.DateTimeField(default=datetime.now())
    userID = models.TextField()
    # authuserfkp = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Post'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=2000)
    time_comment = models.DateTimeField(default=datetime.now())
    authuserfkc = models.ForeignKey(AuthUser,on_delete=models.CASCADE)
    postfk = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Comment'

class lab411(models.Model):
    id = models.AutoField(primary_key=True)
    mssv = models.TextField(max_length=80)
    name = models.TextField(max_length=80)
    address = models.TextField(max_length=80)

    class Meta:
        managed = False
        db_table = 'lab411'
class Tl1(models.Model):
    id = models.AutoField(primary_key=True)
    mssv = models.TextField(max_length=20)
    name = models.TextField(max_length=80)
    address = models.TextField(max_length=90)

    class Meta:
        managed = False
        db_table = 'tl1'

class test(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.FloatField(max_length=80)

    class Meta:
        managed = False
        db_table = 'myApp_authgroup'
class mone(models.Model):
    id = models.AutoField(primary_key=True)
    unit = models.TextField(max_length=40)


    class Meta:
        managed = False
        db_table = 'mone'





