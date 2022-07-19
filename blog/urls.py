from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('register/', user_views.register, name='register'),
    url('profile/', user_views.profile, name='profile'),
    url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url('', include('app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


print(urlpatterns)
