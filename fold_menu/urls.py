from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', views.show_all_users, name="users") ,
    path('users/delete/', views.delete_user),
    path('show-medias/', views.show_media),
    path('users/<str:id>', views.show_all_users),
    path('upload-image/', views.model_form_upload),
    path('permissions-field/', views.user_perms),
    path('tags/', views.tags),
    path('keypress/', views.keypress),
    path('jalali/', views.jalali_view, name='jalali'),
    # path('alaki/<int:y>/<int:m>/<int:d>', views.jalali),
    path('permissions-field/<str:id>', views.user_perms),
    path('set-permissions/<str:id>', views.set_perm),
    path('', views.Home, name='home'),
    # url(r'^admin/', include(admin.site.urls)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
