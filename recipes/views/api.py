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
    elif(request.method == 'POST'):
        serializer = RecipeSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            author_id=1,
            category_id=1,

        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(http_method_names=['get', 'patch', 'delete'])
def recipe_api_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )
    if (request.method == 'GET'):
        serializer = RecipeSerializer(
            instance=recipe,
            many=False,
            context={'request': request},
        )
        return Response(serializer.data)
    elif (request.method == 'PATCH'):
        serializer = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, )

    elif (request.method == 'DELETE'):
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
