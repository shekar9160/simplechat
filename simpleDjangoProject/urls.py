"""simpleDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from simpleFirstApp import views
from simpleDjangoProject import settings

urlpatterns = [

    # Simple Text Page
    path('', views.IndexPageController, name="index_page"),
    path('firstPage',views.FirstPageController,name="first_page"),

    #loading Html File Pages
    path('htmlPages',views.HtmlPageController,name='html_page'),

    #passing data to html templates
    path('htmlPagesWithData',views.HtmlPageControllerWithData,name='html_page_data'),


    #passing data from url to controller
    path('htmlWithDataPass/<str:url_data>', views.PassingDatatoController, name='html_data_pass'),

    path('addData',views.addData,name="add_data"),

    path('add_student',views.add_student,name="add_student"),

    path('add_teacher', views.add_teacher, name="add_teacher"),

    path('show_all_data', views.show_all_data, name="show_all_data"),

    path('update_student/<str:student_id>',views.update_student,name="update_student"),

    path('edit_student', views.edit_student, name="edit_student"),

    path('delete_student/<str:student_id>', views.delete_student, name="delete_student"),

    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
