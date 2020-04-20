from django.urls import path
from rest_framework.routers import SimpleRouter
from medsupport import views

router = SimpleRouter()
router.register(r'hospitals', views.HospitalsViewSet)
router.register(r'solutions', views.SolutionsViewSet)
router.register(r'hospital-needs', views.HospitalNeedsViewSet)

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
] + router.urls
