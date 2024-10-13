from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
from .forms import *

urlpatterns = [
    
    path('',inicio_inicio, name='inicio'),
    path('login/',login_request, name='login'),
    path('logout/',LogoutView.as_view(template_name= 'logout.html'), name='logout'),

    path('nuevo_usuario/', registro , name='nuevo_usuario'),
    path('editar_perfil/', edit_user , name='editar_perfil'),
    path('crear_avatar/', agregar_avatar , name='crear_avatar'),
    path('editar_coleccion/<pk>', agregar_comics_a_coleccion , name='editar_coleccion'),
    
    path('lista_comics/', comicList.as_view(), name='lista_comics'),
    path('detalle_comics/<pk>', comicDetalle.as_view(), name='detalle_comics'),
    path('crear_comics/', comicCreate.as_view(), name='crear_comics'),
    path('modifica_comics/<pk>', comicUpdate.as_view(), name='modifica_comics'),
    path('elimina_comics/<pk>', comicDelete.as_view(), name='elimina_comics'),


    path('colecciones/', coleccionlist.as_view(), name='colecciones'),
    path('detalle_coleccion/<pk>', coleccionDetalle.as_view(), name='detalle_coleccion'),
    path('crear_coleccion/', coleccionCreate.as_view(), name='crear_coleccion'),
    path('modifica_coleccion/<pk>', coleccionUpdate.as_view(), name='modifica_coleccion'),
    path('elimina_coleccion/<pk>', coleccionDelete.as_view(), name='elimina_coleccion'),
    path('About/',about_me,name='about'),
    path('contacto/', contact_view, name='contacto')

]