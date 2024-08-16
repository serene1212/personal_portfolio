from django.test import TestCase
from django.urls import reverse


class HomeViewTestCase(TestCase):
    def test_template_render(self):
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")

    def test_context_data(self):
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context["title"])
