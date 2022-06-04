from django.shortcuts import get_object_or_404
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['get', 'post'])
def recipe_api_list(request):
    if(request.method == 'GET'):
        recipes = Recipe.objects.get_published()[:10]
        serializer = RecipeSerializer(
            instance=recipes,
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)
    else:
        return Response('POST', status=status.HTTP_201_CREATED)


@api_view()
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )
    serializer = RecipeSerializer(
        instance=recipe,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)
