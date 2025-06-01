from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ConsultaSQLView

urlpatterns = [
    path('consulta/', ConsultaSQLView.as_view(), name='consulta-sql'),
    
    # JWT endpoints:
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
