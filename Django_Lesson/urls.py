from django.contrib import admin
from django.urls import path
from app.views import (
    product_create, 
    product_update, 
    product_list_view, 
    ProductCreateView, 
    ProductUpdateView
)

urlpatterns = [
    path('', product_list_view, name='product_list'),  # ルートURLを商品一覧表示に設定
    path('app/', product_list_view, name='product_list'),  # 商品一覧表示（関数ベース）
    path('admin/', admin.site.urls),  # 管理サイト
    path('app/new/', product_create, name='product_form'),  # 商品作成（関数ベース）
    path('app/edit/<int:pk>/', product_update, name='product_update_form'),  # 商品編集（関数ベース）
    # path('app/detail/<int:pk>/', product_detail_view, name='product_detail'),  # 商品詳細表示（関数ベース）

    # クラスベースのビュー
    path('app/new/cbv/', ProductCreateView.as_view(), name="new_cbv"),  # 商品作成（クラスベース）
    path('app/edit/cbv/<int:pk>/', ProductUpdateView.as_view(), name="edit_cbv"),  # 商品編集（クラスベース）
]
