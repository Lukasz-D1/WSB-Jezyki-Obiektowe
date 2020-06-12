from django.urls import path
from app.views import *

urlpatterns = [
    path('', NewLoginView.as_view(), name='index'),
    path('logout', NewLogoutView.as_view(), name='logout'),

    path('ingredients', AllIngredientView.as_view(), name="all_ingredients"),
    path('ingredients/add/', CreateIngredientView.as_view(), name="ingredient_add"),
    path('ingredients/<int:pk>/update', UpdateIngredientView.as_view(), name="ingredient_update"),
    path('ingredients/<int:pk>/update_status', UpdateIngredientStatusView.as_view(), name="ingredient_update_status"),
    path('ingredients/<int:pk>/', DetailIngredientView.as_view(), name="ingredient_detail"),
    path('ingredients/<int:pk>/delete', DeleteIngredientView.as_view(), name="ingredient_delete"),

    path('types', TypeListView.as_view(), name='all_types'),
    path('types/add/', CreateTypeView.as_view(), name="type_add"),
    path('types/<int:pk>/update', UpdateTypeView.as_view(), name="type_update"),
    path('types/<int:pk>/delete', DeleteTypeView.as_view(), name="type_delete"),

    path('nutrients', NutrientsListView.as_view(), name='all_nutrients'),
    path('nutrients/add/', CreateNutrientsView.as_view(), name="nutrients_add"),
    path('nutrients/<int:pk>/update', UpdateNutrientsView.as_view(), name="nutrients_update"),
    path('nutrients/<int:pk>/delete', DeleteNutrientsView.as_view(), name="nutrients_delete"),
]
