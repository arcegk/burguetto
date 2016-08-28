from django.conf.urls import url
from api.views import GetIngredientsAPIView

urlpatterns = (

	url(r'^ingredient-list/$', GetIngredientsAPIView.as_view(), name="ingredient_list" ),

)