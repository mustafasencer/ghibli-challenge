from flask import Blueprint, render_template

from app import ghibli_service
from utils.cache import cache

bp = Blueprint('movies', __name__)


@bp.route('/movies', methods=('GET',))
@cache(ttl=60)
def list_movies():
    films = ghibli_service.list('films', {})
    people = ghibli_service.list('people', {'fields': 'id,name,films'})
    people_with_film_ids = [
        {
            'name': person['name'],
            **{item.split('/')[-1]: None for item in person['films']}
        }
        for person in people
    ]
    result = []
    for film in films:
        film['people'] = []
        for person in people_with_film_ids:
            if film['id'] in person:
                film['people'].append(person['name'])
        result.append(film)
    return render_template('list_films.html', films=result)


@bp.route('/movies/<mid>', methods=('GET',))
def get_movie(mid):
    film = ghibli_service.get_by_id('films', mid)
    return render_template('get_film.html', film=film)
