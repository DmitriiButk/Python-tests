from unittest import TestCase
from hw_test.api_yandex import response, response_file


class TestApiYandex(TestCase):

    def test_response_from_yandex(self):
        resp = response.status_code
        self.assertEqual(resp, 200)
        print(f'Код ответа соответствует 200.')

    def test_create_folder(self):
        resp = response_file.status_code
        self.assertEqual(resp, 409, 'Папка не создана!')
        print('При коде ответа 409 папка уже создана.')
