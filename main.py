from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel
#uvicorn main:app --reload

class Wikiinput(BaseModel):
    """Класс для ввода названия сводки и кол-ва предложений"""
    s : str
    cnt : int
class Wikioutput(BaseModel):
    """Класс для вывода сводки"""
    output : str


wikipedia.set_lang("ru")
app = FastAPI()

@app.get("/{search}", response_model=Wikioutput)
def src(search : str):
    """Возвращает сводку по вашему запросу через path"""
    res= wikipedia.summary(search, sentences=10)
    return Wikioutput(output=res)


@app.get("/next/query", response_model=Wikioutput)
def with_query(search:str, number:int):
    """Возвращает указанное кол-во предложений из сводки по вашему запросу через query"""
    res = wikipedia.summary(search, sentences=number)
    return Wikioutput(output=res)


@app.post("/classes", response_model=Wikioutput)
def classs(src: Wikiinput):
    """Возвращает указанное кол-во предложений из сводки по вашему запросу"""
    res = f'Запрашиваемое резюме: {wikipedia.summary(src.s, sentences= src.cnt)}'
    return Wikioutput(output=res)
