from django.shortcuts import render , HttpResponse , render_to_response , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from site_with_foldmenu.forms import DocumentForm
from django.views import generic
from django.contrib.auth.models import User , Group , Permission , ContentType
from pymongo import MongoClient
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import os
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from jalali_date import datetime2jalali, date2jalali
import jdatetime
from fold_menu import jalali

con = MongoClient()
db = con['djangodb_test']
col_users = db['auth_user']


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


def my_view(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


@login_required
def keypress(request):
    return render(request,'keypress.html')


@login_required
def tags(request):
    if request.method == 'GET':
        return render(request,'tag.html')
    elif request.method == 'POST':
        try:
            tags = request.POST.get("tags")
            tags = tags.split(";")
            tags.remove('')
            col_users.update_one({'id':request.user.id},{'$set':{'tags':tags}})
            return render(request,'done_insert_tags.html')
        except:
            return render(request,'somethings_wrong.html')


@csrf_exempt
@require_http_methods(["POST", "GET"])
@login_required
def jalali_view(request):
    # jalali_date= datetime2jalali(request.user.last_login)
    # en_date = jalali.Persian(str('13'+jalali_date)).gregorian_string("{}/{}/{}")
    # eng_date = jdatetime.date(y,m,d).togregorian()
    if request.method == 'GET':
        return render(request,'persian_calendar.html')
    elif request.method == 'POST':
        try:
            en_date = jalali.Persian(str(request.POST['date'])).gregorian_string("{}/{}/{}")
            print(request.user.id)
            # if 'selected_date' in col_users.find({'id':request.user.id}):
            col_users.update_one({'id':request.user.id},{'$set':{'selected_date':en_date}})
            return render(request,'done_save_selected_date.html')
        except:
            return render(request,'somethings_wrong.html')


@login_required
def Home(request):
    return render(request, 'home.html')


@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


@login_required
@csrf_exempt
@require_http_methods(["POST", "GET"])
def show_all_users(request, id=None):
    users = User.objects.all()
    if request.method == 'GET' and id is None:
        return render(request,'show_users.html',{'users':users})
    else:
        user = get_object_or_404(User, id=id)
        form = UserForm(request.POST or None , instance=user)
        if form.is_valid():
            form.save()
            return redirect("users")
        return render(request, 'edit_user.html', {"form": form , "id" : id})


@login_required
def delete_user(request):
    id = request.POST.get("id")
    User.objects.get(id=id).delete()
    return redirect("users")


@login_required
def show_media(request):
    path = '/home/oem/django_projects/site_with_foldmenu/media/'
    path2 = '/home/oem/django_projects/site_with_foldmenu/media/'
    name_medias=os.listdir(path)
    return render(request,'show_all_medias.html', {'medias':name_medias,'path':path2})


@login_required
@csrf_exempt
def set_perm(request, id):
    request.POST._mutable=True
    del request.POST['id']
    try:
        if request.user.is_superuser:
            user=User.objects.get(id=id)
            for item in request.POST:
                permission = Permission.objects.get(name=item)
                user.user_permissions.add(permission)
                user.save()
            return render(request, 'done_set_permissions.html')
        else:
            return render(request, 'havent_permissions.html')
    except:
        return render(request,'somethings_wrong.html')


@login_required
def user_perms(request, id = None):
    if request.user.is_superuser:
        if id is None:
            users = User.objects.all()
            return render(request,'all_user_perm.html',{'users':users})
        elif id is not None:
            users=User.objects.get(id=id)
            return render(request,'permissions_field.html',{'users':users})
    else:
        return render(request, 'havent_permissions.html')


