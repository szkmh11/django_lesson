from django.contrib import admin
from django.urls import path
from app import views
from app.views import (
    product_create_view,  # 商品作成の関数ベースビュー
    product_update,       # 商品編集の関数ベースビュー
    product_list_view,    # 商品一覧表示の関数ベースビュー
    product_delete_view,  # 商品削除の関数ベースビュー
    category_filter,      # カテゴリ別の商品表示ビュー
)

urlpatterns = [
    path('', product_list_view, name='product_list'),  # ルートURLを商品一覧表示に設定
    path('app/', product_list_view, name='product_list_app'),  # 商品一覧表示（関数ベース）
    path('admin/', admin.site.urls),  # 管理サイト
    path('app/new/', product_create_view, name='product_create'),  # 商品作成（関数ベース）
    path('app/edit/<int:pk>/', product_update, name='product_update'),  # 商品編集（関数ベース）
    path('app/delete/<int:pk>/', product_delete_view, name='product_delete'),  # 商品削除（関数ベース）

    # クラスベースのビュー (削除)
    # path('app/new/cbv/', ProductCreateView.as_view(), name="product_create_cbv"),  # 商品作成（クラスベース）
    # path('app/edit/cbv/<int:pk>/', ProductUpdateView.as_view(), name="product_update_cbv"),  # 商品編集（クラスベース）
    # path('app/delete/cbv/<int:pk>/', ProductDeleteView.as_view(), name="product_delete_cbv"),  # 商品削除（クラスベース）

    # カテゴリごとのフィルタリングURL
    path('category/<int:id>/', category_filter, name='category_filter'),  # カテゴリ別の商品一覧
]
