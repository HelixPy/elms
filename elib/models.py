from django.db import models; import datetime;  import pytz

right_now = datetime.datetime.now(); right_now = pytz.utc.localize(right_now)
default_visibility = "offlne";default_thumbnail = " ";default_passport = " ";default_elib_duty = "user"
##oublic, private, both, offline##default_elib_duty=user,bookeeping

class message(models.Model):
    full_name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message_type = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)
    date_sent = models.DateTimeField(default=right_now, blank=True)
    def __str__(self):
        return f"{self.full_name} - {self.email}"

class student(models.Model):
    full_name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=1000)
    reg_num = models.CharField(max_length=50)
    passport = models.CharField(max_length=1000, default=default_passport)
    date_enrolled = models.DateTimeField(default=right_now, blank=True)
    def __str__(self):
        return f"{self.full_name} - {self.reg_num}"

class staff(models.Model):
    full_name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=1000)
    staff_id = models.CharField(max_length=50)
    rank = models.CharField(max_length=1000)
    passport = models.CharField(max_length=1000, default=default_passport)
    date_enrolled = models.DateTimeField(default=right_now, blank=True)
    elib_duty = models.CharField(max_length=1000, default=default_elib_duty)
    def __str__(self):
        return f"{self.full_name} - {self.department}"

class publication(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.CharField(max_length=1000)
    staff_id = models.CharField(max_length=50)
    journal = models.CharField(max_length=1000)
    date_published = models.DateTimeField(default=right_now, blank=True)
    date_uploaded = models.DateTimeField(default=right_now, blank=True)
    upload_staff_id = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=1000, default=default_thumbnail)
    other_info = models.CharField(max_length=1000)
    visibility = models.CharField(max_length=1000, default=default_visibility)  
    def __str__(self):
        return f"{self.title} - {self.journal}"

class book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    num_of_pages = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    available_on_shelf = models.CharField(max_length=100)   #available, not avaible
    department = models.CharField(max_length=1000)
    date_published = models.DateTimeField(default=right_now, blank=True)
    date_uploaded = models.DateTimeField(default=right_now, blank=True)
    thumbnail = models.CharField(max_length=1000, default=default_thumbnail)
    upload_staff_id = models.CharField(max_length=100)
    other_info = models.CharField(max_length=1000)
    visibility = models.CharField(max_length=1000, default=default_visibility) 
    def __str__(self):
        return f"{self.title} - {self.available_on_shelf}"

    
class lecture_note(models.Model):
    course = models.CharField(max_length=1000)
    course_code = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    department = models.CharField(max_length=1000)
    date_uploaded = models.DateTimeField(default=right_now, blank=True)
    thumbnail = models.CharField(max_length=1000, default=default_thumbnail)
    staff_id = models.CharField(max_length=50)
    other_info = models.CharField(max_length=1000)
    visibility = models.CharField(max_length=50, default=default_visibility)  
    def __str__(self):
        return f"{self.course} - {self.department}"

class leasing(models.Model):
    document_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    lib_staff_id = models.CharField(max_length=50)
    date_requested = models.DateTimeField(default=right_now, blank=True)
    date_collected = models.DateTimeField(default=right_now, blank=True)
    return_due_date = models.DateTimeField(default=right_now, blank=True)
    date_returned = models.DateTimeField(default=right_now, blank=True)
    comment = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.document_id} - {self.return_due_date}"

class reading_list(models.Model):
    document_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=right_now, blank=True)
    def __str__(self):
        return f"{self.document_id} - {self.user_id}"

class gen_login(models.Model):
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    last_login = models.DateTimeField(default=right_now, blank=True)
    acc_status = models.CharField(max_length=1000, default='active')
    auth_token = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.user_id} - {self.last_login}"