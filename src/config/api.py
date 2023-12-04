from account.urls import urlpatterns as accounts_urls
from rest_framework import routers

router = routers.DefaultRouter()
router.urls.extend(accounts_urls)

urlpatterns = router.urls