import pytest
from selenium.webdriver.common.by import By
from tests.functional_tests.recipes.base import RecipeBaseFunctionalTest

from recipes.tests.test_recipe_base import RecipeMixin


@pytest.mark.functional_test
class RecipeHomePageFunctionalTest(RecipeBaseFunctionalTest, RecipeMixin):
    def test_recipe_home_page_without_recipes_not_found_message(self):
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes have been published yet', body.text)
