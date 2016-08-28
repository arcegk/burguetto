from rest_framework import serializers

from ingredient.models import Ingredient

class IngredientSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Ingredient
		fields = ('name', 'extra_price', 'image_path', 'section')