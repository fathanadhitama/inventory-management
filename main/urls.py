from django.urls import path
from main.views import show_main, create_item, show_json,show_xml, show_json_by_id, show_xml_by_id
from main.views import register, login_user, logout_user
from main.views import delete_item, add_amount, reduce_amount

app_name = 'main'

urlpatterns = [
    path('create-item/', create_item, name="create_item"),
    path('', show_main,name='show_main'),
    path('json/', show_json, name="show_json"),
    path('xml/', show_xml, name="show_xml"),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<int:id>/', delete_item, name='delete'),
    path('add_amount/<int:id>/', add_amount, name='add_amount'),
    path('reduce_amount/<int:id>/', reduce_amount, name='reduce_amount'),
]