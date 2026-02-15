from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patiennt in less than 50 words", exmples=['Nitin', 'Monty'])]
    linkedIn: AnyUrl
    email: EmailStr
    age: int
    weight: Annotated[float, Field(strict=True)] 
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
     
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('insert into database')

patient_info = {'name': 'Nitin', 'age': 20, 'weight': 98, "married": True, "allergies": ['pollen', 'dust'], "contact-details": {'nitin':'123', 'monty':'456'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)