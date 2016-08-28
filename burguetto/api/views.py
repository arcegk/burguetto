from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer


class CreateCheckoutAPIView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request):
		data = request.data
		return None


class GetIngredientsAPIView(APIView):

	#permission_classes = (IsAuthenticated, )

	def get(self, request):
		vegetable = Ingredient.objects.filter(section="VEGETABLE")
		vegetable_serialize = IngredientSerializer(vegetable, many=True)

		protein = Ingredient.objects.filter(section="PROTEIN")
		protein_serialize = IngredientSerializer(protein, many=True)

		bread = Ingredient.objects.filter(section="BREAD")
		bread_serialize = IngredientSerializer(bread, many=True)

		cheese = Ingredient.objects.filter(section="CHEESE")
		cheese_serialize = IngredientSerializer(cheese, many=True)

		response = {
			'vegetable' : vegetable_serialize.data,
			'protein' : protein_serialize.data,
			'cheese' : cheese_serialize.data,
			'bread' : bread_serialize.data
		}

		return Response({'ingredients' : response})
