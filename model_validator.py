from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    marrige: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have emergency contact number.')
        
        return model
    

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.marrige)

patient_info = {
    'name': 'Nitin',
    'email': 'neuralnitin@gmail.com',
    'age': '62',
    'allergies': ['pollen', 'dust'],
    'marrige': False,
    'weight': 43.2,
    'contact_details': {'phone_number': '2341234'}
}

patient1 = Patient(**patient_info)
update_patient_data(patient1)