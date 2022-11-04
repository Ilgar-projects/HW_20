import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.model.director import Director
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    d1 = Director(id=1, name='test')
    g1 = Genre(id=1, name='test')

    red = Movie(
        id=1,
        title='RED',
        description='tes tes tes',
        trailer='test',
        year=2022,
        genre_id=1,
        genre=g1,
        director_id=d1
    )

    movie_dao.get_one = MagicMock(returne_value=red)
    movie_dao.get_all = MagicMock(returne_value=[red,])
    movie_dao.create = MagicMock(returne_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def director_service(self, movie_dao_fixture):
        self.director_service = MovieService(dao=movie_dao_fixture)

    def test_partially_update(self):
        movie_d = {
            'id': 1,
            'year': 2020,
        }
        movie = self.director_service.partially_update(movie_d)

        assert movie.year == movie_d.get('year')


    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id == 1

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) == 1

    def test_create(self):
        director_d = {
            'name': 'Rose',
        }
        self.director_service.create(director_d)

        assert director_d is not None

    def test_update(self):
        director_d = {
            'id': 1,
            'name': 'Rose',
        }
        self.director_service.update(director_d)
    def test_delete(self):
        self.director_service.delete(1)
