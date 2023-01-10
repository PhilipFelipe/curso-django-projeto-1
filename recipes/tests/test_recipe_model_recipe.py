from django.core.validators import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase
from ..models import Recipe


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Default Category'),
            author=self.make_author(username='Alex'),
            title='Recipe title',
            description='Recipe description',
            slug='recipe-slug-for-no-defaults',
            preparation_time=10,
            preparation_time_unit='minutos',
            servings=5,
            servings_unit='porções',
            preparation_steps='Recipe preparation steps',
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand([
        ('title', 65),
        ('description', 200),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False'
        )

    def test_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False'
        )

    def test_recipe_string_representation(self):
        title = 'Testing representation'
        self.recipe.title = title
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), title,
            msg=f'Recipe string representation must be "{title}" but "{str(self.recipe)}" was received.'
        )


