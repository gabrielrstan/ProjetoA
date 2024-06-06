
from django.test import TestCase
from django.urls import resolve, reverse

from user.views import HomePageView


class UserHomePageViewTest(TestCase):
    def test_user_home_page_view_is_correct(self):
        view = resolve(reverse('user:home'))
        self.assertIs(view.func.view_class, HomePageView)

    def test_user_home_page_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('user:home'))
        self.assertEqual(response.status_code, 200)

    def test_user_home_page_loads_correct_template(self):
        response = self.client.get(reverse('user:home'))
        self.assertTemplateUsed(response, 'user/pages/home.html')
