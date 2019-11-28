from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import QuestionViewSet, ChoiceViewSet


router = DefaultRouter()
router.register(
    prefix=r'questions', 
    viewset=QuestionViewSet
)
router.register(
    prefix=r'choices',
    viewset=ChoiceViewSet
)

urlpatterns = [
    path(
        route='',
        view=include(router.urls)
    )
]
