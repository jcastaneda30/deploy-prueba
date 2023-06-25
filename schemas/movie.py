from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int]
    movie_title:str = Field(    max_length=500)
    overview:str = Field(   max_length=500)
    year:int = Field(le=2022)
    rating:float = Field(le=10,ge=0)
    category:str = Field(max_length=50)

    class Config:
        schema_extra = {
             "example":{
                  'id':1,
                  "movie_title":"Mi peliculacxvcx",
                  "overview":"Descripcion mivieasdf",
                    "year":2022,
                    "rating":0,
                    "category":"sdjk"
             }
        }