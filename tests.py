import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_valid_genre_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_books_genre() == {'Книга 1': 'Фантастика'}

    def test_set_book_genre_not_valid_genre_not_added_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Комиксы')
        assert collector.get_books_genre() == {'Книга 1': ''}

    def test_set_book_genre_valid_genre_without_book_in_books_genre_empty_dict(self):
        collector = BooksCollector()
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_get_book_genre_valid_name_book_received(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_book_genre('Книга 1') == 'Фантастика'

    def test_get_books_with_specific_genre_valid_genre_received(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    def test_get_books_genre_received(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        assert collector.get_books_genre() == {'Книга 1': ''}

    @pytest.mark.parametrize('book, genre',
                             [['Книга 1', 'Фантастика'], ['Книга 2', 'Мультфильмы'], ['Книга 3', 'Комедии']])
    def test_get_books_for_children_books_not_in_age_rating_received(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]

    @pytest.mark.parametrize('book, genre', [['Книга 1', 'Ужасы'], ['Книга 2', 'Детективы']])
    def test_get_books_for_children_books_in_age_rating_empty_list(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']

    def test_add_book_in_favorites_without_book_in_books_genre_empty_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_again_add_book_added_only_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']

    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.delete_book_from_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_received(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']
