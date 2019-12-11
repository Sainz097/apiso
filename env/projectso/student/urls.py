from rest_framework import routers

from .viewsets import StudentViewSet
# from .viewsets import StudentList

router = routers.SimpleRouter()
router.register('students', StudentViewSet)
# router.register('students/search',StudentList)

urlpatterns = router.urls
