from django.contrib import admin
from django.urls import path, include  # Importe a função include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclua as rotas da sua API
    path('api/', include('api.photo_routes')),  # Supondo que suas rotas da API estão em api.photo_routes
]

# Servir arquivos de mídia durante o desenvolvimento
from django.conf import settings
from django.conf.urls.static import static

# Adicione estas linhas no final do arquivo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
