from pydantic import BaseModel, Field, EmailStr, computed_field

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    marrige: bool
    allergies: list[str]
    contact_detail: dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    

def updated_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.marrige)
    print(f'BMI: {patient.bmi}')

patient_info = {
    'name': 'Nitin',
    'email': 'neuralnitin@gmail.com',
    'age': 42,
    'allergies': ['pollen', 'dust'],
    'marrige': False,
    'weight': 43.2,
    'height': 1.75,
    'contact_detail': {'phone_number': '2341234'}
    }
product1 = Patient(**patient_info)
# product1.bmi
updated_patient_data(product1)

