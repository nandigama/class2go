# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

#c2g specific comments
# instead of putting any indicies here, we put them in a south migration at
# <location to be inserted>

from django.db import models
from django.contrib.auth.models import User

#does additional pages need an owner?
class AdditionalPages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.ForeignKey(User)
    access_id = models.TextField(blank=True)
    course_id = models.ForeignKey('Courses')
    write_access = models.TextField(blank=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    update_log = models.TextField(blank=True)
    time_created = models.DateField(auto_now=False, auto_now_add=True);
    last_updated = models.DateField(auto_now=True, auto_now_add=True);
    class Meta:
        db_table = u'additional_pages'

class Announcements(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.BigIntegerField(null=True, blank=True)
    access_id = models.TextField(blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'announcements'

class AssignmentCategories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'assignment_categories'

class AssignmentGrades(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    assn_id = models.BigIntegerField(null=True, blank=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    json = models.TextField()
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'assignment_grades'

class AssignmentSubmissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.BigIntegerField()
    course_id = models.BigIntegerField()
    assn_id = models.BigIntegerField()
    json = models.TextField()
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'assignment_submissions'

class Assignments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.BigIntegerField(null=True, blank=True)
    access_id = models.TextField(blank=True)
    course_id = models.BigIntegerField()
    category_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    due_date = models.BigIntegerField(null=True, blank=True)
    close_date = models.BigIntegerField(null=True, blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'assignments'

class CourseAnalytics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField(null=True, blank=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    json = models.TextField()
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'course_analytics'

class CourseMaps(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    json = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'course_maps'

class Courses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    code = models.TextField(blank=True)
    title = models.TextField(blank=True)
    institution_id = models.TextField(blank=True)
    institution_title = models.TextField(blank=True)
    mode = models.TextField(blank=True)
    listing_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    staff_emails = models.TextField(blank=True)
    term = models.TextField(blank=True)
    year = models.IntegerField(null=True, blank=True)
    calendar_start = models.BigIntegerField(null=True, blank=True)
    calendar_end = models.BigIntegerField(null=True, blank=True)
    meeting_info = models.TextField(blank=True)
    feature_settings = models.TextField(blank=True)
    membership_control = models.TextField(blank=True)
    join_password = models.TextField(blank=True)
    list_publicly = models.IntegerField(null=True, blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'courses'

class Files(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.BigIntegerField()
    access_id = models.TextField(blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'files'

class ForumPostReplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    forum_id = models.BigIntegerField()
    forum_post_id = models.BigIntegerField()
    description = models.TextField(blank=True)
    rating_data = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'forum_post_replies'

class ForumPosts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    forum_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    rating_data = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'forum_posts'

class Forums(models.Model):
    id = models.BigIntegerField(primary_key=True)
    access_id = models.TextField(blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'forums'

class Institutions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField()
    country = models.TextField(blank=True)
    city = models.TextField(blank=True)
    domains = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'institutions'

class Lectures(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    access_id = models.TextField(blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    calendar_start = models.BigIntegerField(null=True, blank=True)
    calendar_end = models.BigIntegerField(null=True, blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'lectures'

class Officehours(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    calendar_start = models.BigIntegerField(null=True, blank=True)
    calendar_end = models.BigIntegerField(null=True, blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'officehours'

class Roles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    title = models.CharField(max_length=765)
    is_staff = models.IntegerField(null=True, blank=True)
    privileges = models.TextField(blank=True)
    holder_ids = models.TextField(blank=True)
    holder_count = models.BigIntegerField(null=True, blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'roles'

class Sections(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    membership = models.TextField(blank=True)
    members = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sections'

class SharingPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    object_id = models.BigIntegerField()
    type = models.TextField(blank=True)
    licensee_id = models.BigIntegerField()
    cond_by = models.IntegerField(null=True, blank=True)
    cond_nc = models.IntegerField(null=True, blank=True)
    cond_nd = models.IntegerField(null=True, blank=True)
    cond_sa = models.IntegerField(null=True, blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'sharing_permissions'

class UserCourseData(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    json = models.TextField()
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user_course_data'

#Extended storage fields for Users, in addition to django.contrib.auth.models
#Uses one-to-one as per django recommendations at
#https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.models.User
class UserProfile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.OneToOneField(User)
    is_instructor = models.IntegerField(null=True, blank=True)
    site_data = models.TextField(blank=True)
    class Meta:
        db_table = u'user_profile'

class VideoAnnotations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    access_id = models.TextField(blank=True)
    video_id = models.BigIntegerField()
    time_in_video = models.IntegerField(null=True, blank=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'video_annotations'

class VideoQuizSubmissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    video_id = models.BigIntegerField()
    json = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'video_quiz_submissions'

class VideoQuizzes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    access_id = models.TextField(blank=True)
    video_id = models.BigIntegerField()
    json = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'video_quizzes'

class Videos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    owner_id = models.IntegerField(null=True, blank=True)
    access_id = models.TextField(blank=True)
    course_id = models.BigIntegerField()
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    index = models.IntegerField(null=True, blank=True)
    segments = models.TextField(blank=True)
    time_created = models.BigIntegerField(null=True, blank=True)
    last_updated = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'videos'

