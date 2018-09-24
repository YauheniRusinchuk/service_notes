from django.urls import path
from mydatabase.views import (index, detail, EmailDelete, add_new_email,
                            add_new_email_post, list_email, update_change,
                            delete_change)

app_name = 'mydatabase'

urlpatterns = [
    path('', index, name='mydb_index'),
    path('<int:pk>/', detail, name='mydb_detail'),
    path('new/', add_new_email, name='add_new_email'),
    path('newadd/', add_new_email_post, name='new_add_post'),
    path('listemail/', list_email, name='email_list'),
    path('deletechange/<int:pk>/', delete_change, name='delete_change'),
    path('updatechange/<int:pk>/', update_change, name='update_change'),
    path('delete/<int:pk>/', EmailDelete.as_view(), name='email_delete')
]
