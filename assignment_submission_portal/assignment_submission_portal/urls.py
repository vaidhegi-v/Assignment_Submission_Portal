# urls.py
from django.urls import path
from assignment.views import home, RegisterUser, LoginUser, UploadAssignment, admin_assignments, accept_assignment, reject_assignment

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('upload/', UploadAssignment.as_view(), name='upload'),
    path('admins/', admin_assignments, name='admin-assignments'),
    path('assignments/<str:assignment_id>/accept/', accept_assignment, name='accept-assignment'),
    path('assignments/<str:assignment_id>/reject/', reject_assignment, name='reject-assignment'),
]
