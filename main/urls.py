from django.urls import path
from main.views import create_product_flutter, show_main, create_item, show_json,show_xml, show_json_by_id, show_xml_by_id
from main.views import register, login_user, logout_user
from main.views import delete_item, add_amount, reduce_amount
from main.views import get_item_json, add_item_ajax, delete_item_ajax

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
    path('add-amount/<int:id>/', add_amount, name='add_amount'),
    path('reduce-amount/<int:id>/', reduce_amount, name='reduce_amount'),
    path('get-item/', get_item_json, name="get_item"),
    path('create-ajax/', add_item_ajax, name="add_item_ajax"),
    path('delete-ajax/<int:id>', delete_item_ajax, name="delete_ajax"),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]