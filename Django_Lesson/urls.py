from django.contrib import admin
from django.urls import path
from app.views import (
    product_create_view,  # 商品作成の関数ベースビュー
    product_update,       # 商品編集の関数ベースビュー
    product_list_view,    # 商品一覧表示の関数ベースビュー
    product_delete_view,  # 商品削除（関数ベースビュー）
    ProductCreateView,    # 商品作成のクラスベースビュー
    ProductUpdateView     # 商品編集のクラスベースビュー
)

urlpatterns = [
    path('', product_list_view, name='product_list'),  # ルートURLを商品一覧表示に設定
    path('app/', product_list_view, name='product_list'),  # 商品一覧表示（関数ベース）
    path('admin/', admin.site.urls),  # 管理サイト
    path('app/new/', product_create_view, name='new'),  # 商品作成（関数ベース）にname='new'を設定
    path('app/edit/<int:pk>/', product_update, name='product_update_form'),  # 商品編集（関数ベース）
    path('app/delete/<int:pk>/', product_delete_view, name='delete'),  # 商品削除


    # クラスベースのビュー
    path('app/new/cbv/', ProductCreateView.as_view(), name="new_cbv"),  # 商品作成（クラスベース）
    path('app/edit/cbv/<int:pk>/', ProductUpdateView.as_view(), name="edit_cbv"),  # 商品編集（クラスベース）
]
