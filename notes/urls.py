from django.urls import path
from notes.views import index, note_detail, NoteDelete, note_add, add_new_note

app_name = 'notes'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', note_detail, name='detail'),
    path('new/', note_add, name='new_note'),
    path('addnew/', add_new_note, name='add_new'),
    path('delete/<int:pk>/', NoteDelete.as_view(), name='note_delete')
]
