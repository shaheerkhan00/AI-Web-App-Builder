from pydantic import BaseModel, Field


class Schema(BaseModel):
    price: float
    eps: float

class File(BaseModel):
    path: str = Field(description='The path of the file created')
    purpose: str = Field(description='The purpose of the file e.g Main application logic, data processing module, etc.')\

class Plan(BaseModel):
    name: str=Field(description='The name of the app to be built')
    description: str = Field(description='A one line description of the app to be built e,g A web app for calculations')
    techstack: str= Field(description='The techstack of the app to be built e.g python, javascrript, reactjs')
    features : list[str] = Field(description='A list of features of the app to be built e.g user authentication, authorization , main functionalities')
    files: list[File]=Field(description='A list of files to be created, each with a path and purpose')
