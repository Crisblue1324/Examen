from django.urls import path
from apps.gestion_venta.views import categoria, producto, cliente

app_name = "gestion_venta"
urlpatterns = []

urlpatterns += [
    #path('home/',home.SecurityTemplateView.as_view(),name="home"),
    path('categoria/list', categoria.CategoriaListView.as_view(),name="categoria_list" ),
    path('categoria/create',categoria.CategoriaCreateView.as_view(),name="categoria_create" ),
    path('categoria/update/<int:pk>',categoria.CategoriaUpdateView.as_view() ,name="categoria_update" ),
    path('categoria/delete/<int:pk>',categoria.CategoriaDeleteView.as_view() ,name="categoria_delete" ),
]

# urls producto
urlpatterns += [
    path('producto/list', producto.ProductoListView.as_view(),name="producto_list" ),
    path('producto/create',producto.ProductoCreateView.as_view(),name="producto_create" ),
    path('producto/update/<int:pk>',producto.ProductoUpdateView.as_view() ,name="producto_update" ),
    path('producto/delete/<int:pk>',producto.ProductoDeleteView.as_view() ,name="producto_delete" ),
]

# urls cliente
urlpatterns += [
    path('cliente/list', cliente.ClienteListView.as_view(),name="cliente_list" ),
    path('cliente/create',cliente.ClienteCreateView.as_view(),name="cliente_create" ),
    path('cliente/update/<int:pk>',cliente.ClienteUpdateView.as_view() ,name="cliente_update" ),
    path('cliente/delete/<int:pk>',cliente.ClienteDeleteView.as_view() ,name="cliente_delete" ),
]