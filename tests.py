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

    @pytest.mark.parametrize('book, genre', [['Книга 1', 'Фантастика'], ['Книга 2', 'Ужасы'], ['Книга 3', 'Детективы'],
                                             ['Книга 4', 'Мультфильмы'], ['Книга 5', 'Комедии']])
    def test_set_book_genre_valid_genre_added(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.books_genre[book] == genre

    @pytest.mark.parametrize('book, genre', [['Книга 1', 'Фантастика'], ['Книга 2', 'Ужасы'], ['Книга 3', 'Детективы'],
                                             ['Книга 4', 'Мультфильмы'], ['Книга 5', 'Комедии']])
    def test_get_book_genre_valid_name_book_received(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    @pytest.mark.parametrize('book, genre', [['Книга 1', 'Фантастика'], ['Книга 2', 'Ужасы'], ['Книга 3', 'Детективы'],
                                             ['Книга 4', 'Мультфильмы'], ['Книга 5', 'Комедии']])
    def test_get_books_with_specific_genre_valid_genre_received(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(genre) == [book]

    @pytest.mark.parametrize('book', ['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4', 'Книга 5'])
    def test_get_books_genre_received(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.get_books_genre() == {book: ''}


    def test_get_books_for_children_received(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_new_book('Книга 3')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        collector.set_book_genre('Книга 3', 'Детективы')
        assert collector.get_books_for_children() == ['Книга 1']

    @pytest.mark.parametrize('book', ['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4', 'Книга 5'])
    def test_add_book_in_favorites_added(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    @pytest.mark.parametrize('book', ['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4', 'Книга 5'])
    def test_delete_book_from_favorites_book_deleted(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize('book', ['Книга 1', 'Книга 2', 'Книга 3', 'Книга 4', 'Книга 5'])
    def test_get_list_of_favorites_books_received(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]
