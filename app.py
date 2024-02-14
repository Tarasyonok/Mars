from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def main():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    s = """<p>Человечество вырастает из детства.</p>
           <p>Человечеству мала одна планета.</p>
           <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
           <p>И начнем с Марса!</p>
           <p>Присоединяйся!</p>"""
    return s


@app.route("/image_mars")
def image_mars():
    s = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img href="http://astrobel.ru/images/stories/foto/2018/ClipBoard-2.jpg" />
        <p>Вот она какая, красная планета.</p>
    </body>
    </html>
    """
    return s


@app.route("/promotion_image")
def promotion_image():
    s = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Привет, Марс!</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <link href="static/css/style.css" rel="stylesheet">
        </head>
        <body>
            <h1>Жди нас, Марс!</h1>
            <img src="static/img/mars.jpeg" alt="mars" width=200 height=200>
            <p class="alert alert-dark">Человечество вырастает из детства.</p>
            <p class="alert alert-success">Человечеству мала одна планета.</p>
            <p class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p class="alert alert-warning">И начнем с Марса!</p>
            <p class="alert alert-danger">Присоединяйся!</p>
        </body>
        </html>
        """
    return s


@app.route("/astronaut_selection")
def astronaut_selection():
    s = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Привет, Марс!</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <link href="static/css/style.css" rel="stylesheet">
        </head>
        <body>
            <form action="">
                <input class="form-control mb-1" type="text" name="" id="" placeholder="Введите фамилию">
                <input class="form-control mb-3" type="text" name="" id="" placeholder="Введите имя">
                <input class="form-control mb-3" type="email" name="" id="" placeholder="Введите адрес почты">
    
                <label>
                    <p class="mb-1">Какое у вас образование?</p>
                    <select class="form-select" name="" id="">
                        <option value="1" selected>Начальное</option>
                        <option value="2">Среднее</option>
                        <option value="3">Высшее</option>
                    </select>
                </label>
    
                <p class="mt-3 mb-1">Какие у вас профессии?</p>
                <label>
                    <input type="checkbox" name="job" id="">
                    инженер-исследователь
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    пилот
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    строитель
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    экзобиолог
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    врач
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    инженер по терраформированию
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    климатолог
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    специалист по радиационной защите
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    астрогеолог
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    гляциолог
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    инженер жизнеобеспечения
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    метеоролог
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    оператор марсохода
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    киберинженер
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    штурман
                </label>
    
                <label>
                    <input type="checkbox" name="job" id="">
                    пилот дронов
                </label>
    
    
    
                <p class="mt-3 mb-1">Укажите пол</p>
                <label>
                    <input type="radio" name="sex" checked>
                    Мужской
                </label>
    
                <label>
                    <input type="radio" name="sex">
                    Женский
                </label>
    
                <label class="mt-3">
                    <p class="mb-1">Почему Вы хотите принять участие в миссии?</p>
                    <textarea class="form-control" name="why" id=""></textarea>
                </label>
    
    
                <label class="mt-3">
                    <p class="mb-1">Приложите фотографию</p>
                    <input type="file" name="photo" id="">
                </label>
    
                <label class="mt-3 mb-3">
                    <input type="checkbox" name="on_mars" id="">
                    Готовы отсаться на марсе?
                </label>
    
                <button class="btn btn-primary" type="submit">Отправить</button>
            </form>
        </body>
        </html>
        """
    return s


@app.route("/choice/<planet_name>")
def choice_x(planet_name):
    s = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Варианты выбора</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <link href="static/css/style.css" rel="stylesheet">
        </head>
        <body>
            <h1>Моё предложение {planet_name}</h1>
            <p class="alert alert-dark">Человечество вырастает из детства.</p>
            <p class="alert alert-success">Человечеству мала одна планета.</p>
            <p class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</p>
            <p class="alert alert-warning">И начнем с <strong>{planet_name}</strong>!</p>
            <p class="alert alert-danger">Присоединяйся!</p>
        </body>
        </html>
        """
    return s

@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Колонизация</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                  rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                  crossorigin="anonymous">
        </head>
        <body>
            <h1 class="alert alert-light">Результаты отбора</h1>
            <h2 class="alert alert-success" role="alert">Претендента на участие в миссии {nickname}:</h2>
            <h3 class="alert alert-light" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
            <h4 class="alert alert-warning" role="alert">Составляет {rating}</h4>
            <h5 class="alert alert-light" role="alert">Желаем удачи</h5>
        </body>
    </html>"""


@app.route("/load_photo", methods=["POST", "GET"])
def load_photo():

    if request.method == "GET":
        src = "static/img/default.png"

    elif request.method == "POST":
        f = request.files["file"]
        with open("static/img/image.png", "wb") as file:
            file.write(f.read())
        src = "static/img/image.png"

    s = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Отбор астронавтов</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <link href="static/css/style.css" rel="stylesheet">
        </head>
        <body>
            <form method="POST" enctype="multipart/form-data">
                <label>
                    <p class="mb-1">Приложите фотографию</p>
                    <input type="file" name="file" id="file">
                </label>
                
                <img class="mt-2 mb-2" id="image" src="{src}" alt="" height=300><br>
    
                <button class="btn btn-primary" type="submit">Отправить</button>
            </form>
        </body>
        </html>
        """
    return s


@app.route('/carousel')
def carousel():
    return f"""<!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Колонизация</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
                  rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
                  crossorigin="anonymous">
        </head>
        <body>
            <h1 class="alert alert-light">Пейзажи Марса</h1>
            <div id="carouselExample" class="carousel slide" style="width: 50%;">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="static/img/carousel1.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="static/img/carousel2.png" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="static/img/carousel3.png" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
        </body>
    </html>"""

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
