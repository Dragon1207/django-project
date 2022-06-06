from django.urls import path

from recipes.views import api, site

app_name = 'recipes'

urlpatterns = [
    path('',
         site.RecipeListViewHome.as_view(),
         name='home'),
    path('recipes/search/',
         site.RecipeListViewSearch.as_view(),
         name='search'),
    path('recipes/category/<int:category_id>/',
         site.RecipeListViewCategory.as_view(),
         name='category'),
    path('recipes/<int:pk>/',
         site.RecipeDetail.as_view(),
         name='recipe'),
    path('recipes/api/v1/',
         site.RecipeListViewHomeApi.as_view(),
         name='recipes_api_v1'),
    path(
        'recipes/api/v1/<int:pk>/',
        site.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail",
    ),
    path(
        'recipes/theory/',
        site.theory,
        name="theory",
    ),
    path(
        'recipes/api/v2/',
        api.RecipeAPIv2ViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name="recipes_api_v2",
    ),
    path(
        'recipes/api/v2/<int:pk>/',
        api.RecipeAPIv2ViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name="recipes_api_v2_detail",
    ),

]
