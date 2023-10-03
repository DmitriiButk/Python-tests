from unittest import TestCase
from hw_test.hw_secretary import get_name, add, delete_user_by_number, documents, directories


class TestSecretary(TestCase):
    def test_add(self):
        add('international passport', '311 020203', 'Александр Пушкин', 3)
        self.assertEqual(documents[-1]['name'], 'Александр Пушкин')
        add('passport', '2323', 'Дмитрий Волков', 2)
        self.assertEqual(documents[-1]['name'], 'Дмитрий Волков')

    def test_get_name(self):
        expected1 = 'Аристарх Павлов'
        number1 = '10006'
        expected2 = 'Василий Гупкин'
        number2 = '2207 876234'
        expected3 = 'Документ 2222 не найден.'
        number3 = '2222'
        self.assertEqual(get_name(number1), expected1)
        self.assertEqual(get_name(number2), expected2)
        self.assertEqual(get_name(number3), expected3)

    def test_delete_user_by_name(self):
        number1 = '11-2'
        user1 = 'Геннадий Покемонов'
        expected1 = f'Пользователь {user1} с номером документа {number1} удалён.'
        number2 = '2424'
        expected2 = f'Пользователь с номером документа {number2} не найден.'
        self.assertEqual(delete_user_by_number(number1), expected1)
        self.assertEqual(delete_user_by_number(number2), expected2)
