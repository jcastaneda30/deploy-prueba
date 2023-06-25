from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine,Base 
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_route
from models.movie import Movie as MovieModel
from models.user import User as UserModel

app = FastAPI()
app.title = "Mi fast api"
app.version = "0.0.2"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_route)

Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])
def message():
    return HTMLResponse('''<!DOCTYPE html>
                    <html>
                    <head>
                        <title>Imagen centrada</title>
                        <style>
                            /* Estilos para centrar la imagen */
                            .container {
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                height: 100vh;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRndCN-NGTPW4V4Qqeqzzpt5hC3YZ2OGK0q0Q&usqp=CAU" alt="Imagen">
                        </div>
                    </body>
                    </html>
''')