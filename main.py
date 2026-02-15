from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse 
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json
app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='Id of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City of the patient')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in m')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kg')]


    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    
    @computed_field
    @property
    def vertict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal weight'
        elif self.bmi < 30:
            return 'normal'
        else:
            return 'Obese'




def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


@app.get('/')
def status_check():
    return {"status": "OK"}

@app.get('/view')
def view_patients():
    patient_data = load_data()
    return patient_data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='Id of the patient', example='P001')):
    data = load_data()

    if patient_id in data:
        return data[patient_id] 

    return HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort by height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field selected from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail=f'Invalid order select between asc and desc')

    data = load_data()
    sort_order = True if order == 'desc' else False 
    sorted_data = sorted(data.values(), key=lambda x: x.get('sort_by', 0), reverse=sort_order)

    return sorted_data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.post('/create')
def create_patient(patient: Patient): #patient naam ka json recieve krega jiska datatype hai Patinet
    #load existing data
    data = load_data()
    
    #check if patient id already exists or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient with this id already exists')
    #load new patient data 
    #the data is python dictionary and the patient is pydantic object so we need to convert it into dictionary before using it.
    #convert pydantic object to dictionary using .dict() method
    data[patient.id] = patient.model_dump(exclude=['id'])
    #save the data back to json file
    save_data(data)
    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'})