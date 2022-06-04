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
    DetailTask, \
    DeleteUser, \
    EditUser, \
    LogoutUser, \
    LoginUser, \
    CreateUser, \
    UsersList, \
    IndexView

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
    path('users/<int:pk>/delete/', DeleteUser.as_view(), name='delete_user'),
    path('users/<int:pk>/update/', EditUser.as_view(), name='edit_user'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('users/create/', CreateUser.as_view(), name='register'),
    path('users/', UsersList.as_view(), name='users'),
    path('', IndexView.as_view(), name='index'),
]
