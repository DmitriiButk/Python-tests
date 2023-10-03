from hw_test.hw_secretary import get_name, add, delete_user_by_number, documents


class TestPytest():
    def test_add(self):
        add('international passport', '311 020203', 'Александр Пушкин', 3)
        assert documents[-1]['name'] == 'Александр Пушкин'
        add('passport', '2323', 'Дмитрий Волков', 2)
        assert documents[-1]['name'] == 'Дмитрий Волков'

    def test_get_name(self):
        expected = 'Аристарх Павлов'
        expected2 = 'Геннадий Покемонов'
        number1 = '10006'
        number2 = '11-2'
        number3 = '2222'
        assert get_name(number1) == expected
        assert get_name(number2) == expected2
        assert get_name(number3) == 'Документ 2222 не найден.'

    def test_delete_user_by_name(self):
        number1 = '11-2'
        user1 = 'Геннадий Покемонов'
        assert delete_user_by_number(number1) == f'Пользователь {user1} с номером документа {number1} удалён.'
        number2 = '2424'
        assert delete_user_by_number(number2) == f'Пользователь с номером документа {number2} не найден.'
