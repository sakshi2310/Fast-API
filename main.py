
from fastapi import FastAPI,Path,HTTPException,Query
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse

class Patient(BaseModel):
    id : Annotated[str,Field(...,description="ID of the patient",examples=['P001'])]
    name : Annotated[str,Field(...,description="Name of the patient")]
    city : Annotated[str,Field(...,description="City where the patient is living")]
    age : Annotated[int,Field(...,gt=0,lt=120,description="Age of the patient")]
    gender : Annotated[Literal['male','female','other'],Field(...,description="Gender of the patient")]
    height : Annotated[float,Field(...,gt=0,description="height of the patient")]
    weight : Annotated[float,Field(...,gt=0,description="weight of the patient")]

    @computed_field
    @property
    def bmi(self) ->float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Overweight"


app = FastAPI()

def load_data():
    try:
        with open('patients.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="patients.json not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON format")
    
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data,f)

@app.get('/')
def hello():
    return {"message":"Patient Management system"}

@app.get('/about')
def about():
    return {'message':'Fully functional api to manage the patient records'}

# for the run this code 
# command : uvicorn main:app --reload
# for the docs /docs  add in the url


@app.get('/view')
def view():
    data = load_data()
    return data

@app.get("/patients/{patient_id}")  
def view_patient(patient_id:str=Path(...,description='ID of the patient',example='P001')):
    # load all the function
    data = load_data()
    # patients = data.get("patients", {})

    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by:str=Query(...,description="sort on the basis on the height , weight , and bmi"),order:str = Query('asc',description="sort in asc or desc order")):

    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail="invalid field select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid order select betewwn asc and desc")
    
    data = load_data()
    patients = data.get("patients", {})

    sort_order = True if order=='desc' else False
    sortd_data = sorted(patients.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)


    return sortd_data

@app.post('/create')
def create_patient(patient:Patient):
    # load the existing data
    data = load_data()

    # check if pateient already exit
    if patient.id in data:
        raise HTTPException(status_code=400,detail="pateient already exist")
    
    # new patient add to the database
    data[patient.id]=patient.model_dump(exclude=['id'])

    # save into the json file
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'pateient created suceesfully'})
