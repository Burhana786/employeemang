from django.urls import path
# from .views import RegView,ViewEmp,DeleteEmp,EditEmp,DeptView,ViewDept,DeleteDept,DeptEdit
from .views import *
urlpatterns=[
    path('reg/',RegView.as_view(),name="reg"),
    path('view/',ViewEmp.as_view(),name="vemp"),
    path('delemp/<int:id>',DeleteEmp.as_view(),name="delemp"),
    path('editemp/<int:id>',EditEmp.as_view(),name="editemp"),
    path('dept/',DeptView.as_view(),name="dept"),
    path('dept1/',ViewDept.as_view(),name="dept1"),
    path('deldept/<int:did>',DeleteDept.as_view(),name="deldept"),
    path('editdept/<int:did>',DeptEdit.as_view(),name="editdept"),
    path('addman/',MangerReg.as_view(),name="addman"),
    path('viewman/',ManagerList.as_view(),name="viewman"),
    path('delman/<int:did>',DeleteMan.as_view(),name="delman"),
    path('editman/<int:did>',ManEdit.as_view(),name="editman"),
]
