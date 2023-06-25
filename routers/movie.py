from fastapi import Depends,Path,Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from fastapi.routing import APIRouter
from services.movie import MovieService
from schemas.movie import Movie 

movie_router = APIRouter()

@movie_router.get("/movies", tags=["Movies"],response_model=List[Movie],status_code=200,dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result=MovieService(db).get_movies()
    return JSONResponse(status_code=200,content=jsonable_encoder(result))   

#localhost:8000/movies/5
@movie_router.get(path='/movies/{id}',tags=['Pelicula'],response_model=Movie)
def get_movie(id:int = Path(ge=1,le=2000))->Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

@movie_router.get('/movies/',tags=['movies'],response_model=List[Movie])
def get_movies_by_category(category:str=Query(min_length=5,max_length=15))->List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.post('/movies', tags=['movies'],status_code=201)
def create_movies(movies: List[Movie]):
    db = Session()
    MovieService(db).create_movies(movies)
    return "Se realizo con exito"



@movie_router.put(path='/movies/{id}',tags=['movie'],status_code=200)
def update_movie(id:int , movie: Movie):
    db=Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    MovieService(db).uptdate_movie(id,movie)
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


@movie_router.delete(path='/movies/{id}',tags=['delete Movies'],status_code=200)
def delete_movies(id: int):
    db=Session()
    result = db.query(MovieModel).filter(MovieModel.id==id).first()
    if not result:
        return JSONResponse(status_code=404,content={'message':'No se encontro'})
    MovieService(db).delete_movies(result)
    return JSONResponse(status_code=404,content={'message':'Eliminado'})
