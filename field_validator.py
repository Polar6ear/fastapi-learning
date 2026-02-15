from pydantic import BaseModel, field_validator, EmailStr

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be between 0 and 100')

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value
        
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()    

def update_patient(patient: Patient):
    print(patient.name)
    print(patient.email)


patient_info = {
    'name': 'Nitin',
    'email': 'nitin@gmail.com'
}

patient1 = Patient(**patient_info) #validation -> type coercion

update_patient(patient1)