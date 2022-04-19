from django.urls import path
from . import views

urlpatterns = [
    path('students', views.students, name='students'),
    path('studentsList', views.ListViewStudents.as_view(), name='student_list'),
    path('studentsFacultySelect', views.ListViewFacultySelect.as_view(), name='student_select_list'),
    path('studentsFacultyList/<str:faculty>', views.ListViewStudentsByFaculty.as_view(),
         name='student_list_faculty'),

]
