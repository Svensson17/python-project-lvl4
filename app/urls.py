from django.urls import path

from app.views import StatusList, \
    CreateStatus, \
    UpdateStatus, \
    DeleteStatus, \
    TaskList, \
    DeleteTask, \
    UpdateTask, \
    CreateTask, \
    LabelList, \
    CreateLabel, \
    UpdateLabel, \
    DeleteLabel, \
    DetailTask

urlpatterns = [

    path('statuses/', StatusList.as_view(), name='statuses'),
    path('statuses/create/', CreateStatus.as_view(), name='create_stat'),
    path(
        'statuses/<int:pk>/update/',
        UpdateStatus.as_view(),
        name='update_stat'
    ),
    path(
        'statuses/<int:pk>/delete/', DeleteStatus.as_view(), name='delete_stat'
    ),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('tasks/create/', CreateTask.as_view(), name='create_task'),
    path('tasks/<int:pk>/update/', UpdateTask.as_view(), name='update_task'),
    path('tasks/<int:pk>/', DetailTask.as_view(), name='detail_task'),
    path('tasks/<int:pk>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('labels/', LabelList.as_view(), name='labels'),
    path('labels/create/', CreateLabel.as_view(), name='create_label'),
    path(
        'labels/<int:pk>/update/',
        UpdateLabel.as_view(),
        name='update_label'
    ),
    path(
        'labels/<int:pk>/delete/',
        DeleteLabel.as_view(),
        name='delete_label'
    ),
]
