from rest_framework import routers

from api.views import AlbumViewSet, ArtistViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'albums/?', AlbumViewSet)
router.register(r'artists/?', ArtistViewSet)

urlpatterns = router.urls
