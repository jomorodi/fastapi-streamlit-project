from enum import Enum
from typing import Annotated
from fastapi import FastAPI , Form , Response
from pydantic import BaseModel
import model

app = FastAPI()



class ModelLanguage(str, Enum):
    english = "english"
    russian = "russian"
    
    german = "german"
    spanish = "spanish"
    french = "french"

class Item(BaseModel):
    text: str
    


@app.post("/{language}")
async def procses_text (language: ModelLanguage , text: Annotated[str, Form()] ):
    #print (text)'
    #
    #model.select(language)
    return Response (model.tospeech (text, language ) , media_type = "audio/vnd.wav")