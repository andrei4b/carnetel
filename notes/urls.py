from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	
	url(r'^note/(?P<pk>\d+)$', views.NoteDetailView.as_view(), name='note-detail'),

]

urlpatterns += [   
    url(r'^mynotes/$', views.NotesByUserListView.as_view(), name='my-notes'),
]

urlpatterns += [   
    path('note/<int:pk>/update/', views.update_or_delete_note, name='update-note'),
]

urlpatterns += [  
	path('note/create/', views.NoteCreate.as_view(), name='note_create'),
]