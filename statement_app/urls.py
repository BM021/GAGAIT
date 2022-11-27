from django.urls import path
from . import views
from .views import MainPage, StatementDetail, UpdateStatement, DeleteStatement, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', MainPage.as_view(), name='main_page'),
    path('search', views.search_exact_statement),
    path('exact_statement/<int:pk>', views.get_exact_statement),
    path('statement/<int:pk>', StatementDetail.as_view(), name='statement'),
    path('statements_form', views.create_statement),
    path('update_statement/<int:pk>', UpdateStatement.as_view(), name='update_statement'),
    path('delete_statement/<int:pk>', DeleteStatement.as_view(), name='delete_statement'),
]
