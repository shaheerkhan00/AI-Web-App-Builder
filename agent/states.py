from pydantic import BaseModel, Field, ConfigDict


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


class ImplementationTask(BaseModel):
    filepath: str = Field(description='The path of the file to be modified')
    task_description: str = Field(description='A detailed description of the implementation task to be performed in the file')
    
class TaskPlan(BaseModel):
    implementation_steps:list[ImplementationTask]=Field(description='A list of implementation steps to be taken to build the app')
    model_config = ConfigDict(extra='allow')

    