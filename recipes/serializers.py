from django.contrib.auth.models import User
from rest_framework import serializers

from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'category', 'public', 'preparation'
        ]

    # Abaixo, ficam só os campos personalizados
    public = serializers.BooleanField(source='is_published', read_only=True)
    preparation = serializers.SerializerMethodField(
        method_name='any_method_name', read_only=True
    )
    category = serializers.StringRelatedField(read_only=True,)

    def any_method_name(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
