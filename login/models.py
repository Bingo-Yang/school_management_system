# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class TBook(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_author = models.CharField(max_length=20, blank=True, null=True)
    book_pub = models.CharField(max_length=20, blank=True, null=True)
    book_operator = models.CharField(max_length=20, blank=True, null=True)
    book_put_num = models.IntegerField(blank=True, null=True)
    book_name = models.CharField(max_length=20, blank=True, null=True)
    book_category = models.CharField(max_length=20, blank=True, null=True)
    book_pubnum = models.IntegerField(blank=True, null=True)
    book_price = models.IntegerField(blank=True, null=True)
    book_pubdate = models.DateField(blank=True, null=True)
    book_inrto = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'


class TBookBorrow(models.Model):
    borrow_id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, db_column='book', blank=True, null=True)
    stu = models.ForeignKey('TStuMessenger', models.DO_NOTHING, db_column='stu', blank=True, null=True)
    borrow_time = models.DateField(blank=True, null=True)
    return_time = models.DateField(blank=True, null=True)
    registrar = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book_borrow'


class TClass(models.Model):
    cno = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=30, blank=True, null=True)
    grade = models.ForeignKey('TGrade', models.DO_NOTHING, db_column='grade', blank=True, null=True)
    major = models.ForeignKey('TMajor', models.DO_NOTHING, db_column='major', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_class'


class TCourse(models.Model):
    cour_id = models.IntegerField(primary_key=True)
    cour_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_course'


class TGrade(models.Model):
    gra_id = models.IntegerField(primary_key=True)
    gra_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_grade'


class THeadTeacher(models.Model):
    ht_id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey('TTeacher', models.DO_NOTHING, db_column='teacher', blank=True, null=True)
    clazz = models.ForeignKey(TClass, models.DO_NOTHING, db_column='clazz', blank=True, null=True)
    ht_in_date = models.DateField(blank=True, null=True)
    ht_out_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_head_teacher'


class TMajor(models.Model):
    maj_id = models.IntegerField(primary_key=True)
    maj_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_major'


class TStuMessenger(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    clazz = models.ForeignKey(TClass, models.DO_NOTHING, db_column='clazz', blank=True, null=True)
    stu_gender = models.CharField(max_length=2, blank=True, null=True)
    stu_id_num = models.CharField(max_length=20, blank=True, null=True)
    stu_addr = models.CharField(max_length=50, blank=True, null=True)
    stu_political = models.CharField(max_length=10, blank=True, null=True)
    stu_healthy = models.CharField(max_length=10, blank=True, null=True)
    stu_name = models.CharField(max_length=15, blank=True, null=True)
    stu_age = models.IntegerField(blank=True, null=True)
    stu_birthday = models.DateField(blank=True, null=True)
    stu_phone = models.IntegerField(blank=True, null=True)
    stu_nation = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stu_messenger'


class TStuRegister(models.Model):
    sr_id = models.IntegerField(primary_key=True)
    stu = models.ForeignKey(TStuMessenger, models.DO_NOTHING, db_column='stu', blank=True, null=True)
    stu_major = models.CharField(max_length=12, blank=True, null=True)
    stu_recommender = models.CharField(max_length=10, blank=True, null=True)
    clazz = models.ForeignKey(TClass, models.DO_NOTHING, db_column='clazz', blank=True, null=True)
    stu_enrollment = models.DateField(blank=True, null=True)
    stu_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stu_register'


class TStuScore(models.Model):
    sco_id = models.IntegerField(primary_key=True)
    stu = models.ForeignKey(TStuMessenger, models.DO_NOTHING, db_column='stu', blank=True, null=True)
    clazz = models.ForeignKey(TClass, models.DO_NOTHING, db_column='clazz', blank=True, null=True)
    test_date = models.DateField(blank=True, null=True)
    test_teacher = models.CharField(max_length=20, blank=True, null=True)
    test_category = models.CharField(max_length=20, blank=True, null=True)
    test_score = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    course = models.ForeignKey(TCourse, models.DO_NOTHING, db_column='course', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stu_score'


class TTeacher(models.Model):
    tea_id = models.IntegerField(primary_key=True)
    tea_name = models.CharField(max_length=20, blank=True, null=True)
    tea_gender = models.CharField(max_length=3, blank=True, null=True)
    tea_political = models.CharField(max_length=20, blank=True, null=True)
    tea_edu = models.CharField(max_length=20, blank=True, null=True)
    tea_id_num = models.CharField(max_length=20, blank=True, null=True)
    tea_work_date = models.DateField(blank=True, null=True)
    tea_age = models.IntegerField(blank=True, null=True)
    tea_marry = models.CharField(max_length=10, blank=True, null=True)
    tea_natioin = models.CharField(max_length=10, blank=True, null=True)
    tea_date = models.DateField(blank=True, null=True)
    tea_phone = models.IntegerField(blank=True, null=True)
    major = models.ForeignKey(TMajor, models.DO_NOTHING, db_column='major', blank=True, null=True)
    tea_intro = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_teacher'


class TTeachingStaff(models.Model):
    ts_id = models.IntegerField(primary_key=True)
    teacher = models.ForeignKey(TTeacher, models.DO_NOTHING, db_column='teacher', blank=True, null=True)
    course = models.ForeignKey(TCourse, models.DO_NOTHING, db_column='course', blank=True, null=True)
    tea_in_date = models.DateField(blank=True, null=True)
    tea_out_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_teaching_staff'


class TUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=15, blank=True, null=True)
    user_password = models.CharField(max_length=20, blank=True, null=True)
    user_nickname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
