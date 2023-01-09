from django.urls import path,include
from .import views
from rest_framework import routers
from rest_framework.authtoken import views as auth_view

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products',views.ProductViewSet)
router.register(r'retailers',views.RetailerViewSet)

#router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', auth_view.obtain_auth_token)
]
