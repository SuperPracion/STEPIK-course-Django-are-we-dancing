from django.test import TestCase
from django.urls import reverse
from . import views


# Create your tests here.

# class TestHoroscope(TestCase):
#     def test_index(self):
#         response = self.client.get('/horoscope/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_libra(self):
#         response = self.client.get('/horoscope/libra/')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)',
#                       response.content.decode())
#
#     def test_all_signs(self):
#         for sign, description in views.zodiac_dict.items():
#             reverse_path = reverse('horoscope-name', args=(sign, ))
#             response = self.client.get(reverse_path)
#             self.assertEqual(response.status_code, 200)
#             self.assertIn(description, response.content.decode())

class TestHoroscope(TestCase):
    def test_libra_redirect(self):
        for i in range(1, 13):
            reverse_path = reverse('horoscope-name', args=(i,))
            response = self.client.get(reverse_path)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{list(views.zodiac_dict)[i - 1]}/')