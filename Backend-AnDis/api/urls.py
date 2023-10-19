from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from api import views
from rest_framework_simplejwt.views import TokenRefreshView


#router = routers.DefaultRouter()
#router.register(r'usuario',views.UsuariosView, 'usuario ')
urlpatterns = [
    #path("api/v1/", include(router.urls)),
    #path('docs/', include_docs_urls(title="UsuarioAPI")),
    path('register/',views.registro),
    path('login/',views.LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]