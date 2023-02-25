from django.shortcuts import render;from django.shortcuts import render;from django.http import HttpResponse;from django.shortcuts import redirect
#from .models import agentlink, newsletters, properties, user_info, central_login, advert_spaces, saved_properties, agent_messages, paystack_data, admin_messages, profile_tier
import datetime; import random; import string; from django.utils import timezone; import pytz
from django.core.mail import send_mail; from django.core.mail import EmailMultiAlternatives; from django.conf import settings
from django.http import HttpResponse, JsonResponse; import os
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from pathlib import Path

from .models import (message, student, staff, publication, book,
                     lecture_note, leasing, reading_list, gen_login)

not_allowed = [None, "none", "", False, 0, [], (), {}, "/", ]
EXT_ALLOWED = ["pdf", "docx", "jpg", "jpeg", "png", "xlsx", "pub"]
greetings = ["Hi dear", "Happy reading!", "How are you today?", "Whats up?", "Holla!", "How's it going?", "Velkom!", "Hello! let's get started"]

right_now = datetime.datetime.now(); right_now = pytz.utc.localize(right_now); one_month = right_now + datetime.timedelta(days=30)

abc = string.ascii_lowercase; new_name = ''.join(random.choice(abc) for i in range(8))

def allowed_image(filename):
    if not "." in filename.name:
        return False
    ext = filename.split(".")[-1]
    if ext.upper() in EXT_ALLOWED:
        return True
    else:
        return False
def photo_saver(file_data):
    fss = FileSystemStorage()
    if allowed_image(file_data.name):
        file_data.name = f"{new_name}.{file_data.name.split('.')[-1]}"
        file = fss.save(file_data.name, file_data)
        file_url = fss.url(file)
        return file_url
    return False


def get_user_data(identity, user_cart):
    try:
        if user_cart != "student":
            recs = staff.objects.get(staff_id=identity)
        else:
            recs = student.objects.get(reg_num=identity)
        return recs
    except Exception as e:
        print(e);return False


def unwrap(query):
    y = []
    for x in query:
        y.append(x)
    return y

#routes downwards

def home(request):
    return render(request, 'zhome/index.html')

def login(request):
    if request.method == "POST":
        login_data = request.POST.getlist('login_data')
        print(login_data)
        try:
            try:
                auths = gen_login.objects.get(user_id=login_data[0].lower())
                if auths.password != login_data[1]:
                    return render(request, 'login.html', {'greet': random.choice(greetings), 'error_msg':f"Incorrect Password"})
                elif auths.acc_status == "inactive":
                    return render(request, 'login.html', {'greet': random.choice(greetings), 'error_msg': "Sorry your profile has been Deactivated, report to the admin."})
                else:
                    request.session["user_id"] = login_data[0].lower();request.session["user_cart"]=auths.user_cart
                    return redirect('dashboard')

            except ObjectDoesNotExist:
                return render(request, 'login.html', {'greet': random.choice(greetings), 'error_msg':f"We do not have any records for {login_data[0].upper()} "})
        except Exception as e:
            print(e); return render(request, 'login.html', {'greet': random.choice(greetings), 'error_msg':'Sorry an error occurred, please try again'})
    else:
        request.session["user_id"]=""
        return render(request, 'login.html', {'greet': random.choice(greetings)})

def dashboard(request):
    try:
        if request.session["user_id"] in not_allowed:
            return redirect(login)
        else:
            user_data = get_user_data(request.session["user_id"], request.session['user_cart'])
            if user_data:
                return render(request, "lib_admin_home.html", {"user_data": user_data})
            else:
                return render(request, 'login.html', {'greet': random.choice(greetings), 'error_msg':f"We are unable to fetch your records at the moment"})
    except Exception as e:
        print(e); return redirect(login)

def staffprofile(request):
    return render(request, 'staffprofile.html')

def studentprofile(request):
    return render(request, 'student.html')

def borrowing(request):
    return render(request, 'borrowing.html')

def public_search(keyword, request):
    pass

def private_search(keyword, request):
    pass

def publications(request):
    pass

def public_message(request):
    pass

def private_message(request):
    pass

def leasing(user_id, book_id, request):
    pass

def uploads(request):
    return render(request, 'uploads.html')

def bookupload(request):
    if request.method == 'POST':
        print("validating content...")
        print("uploading...")
        print("Book upload was successful")
    return render(request, 'success.html')