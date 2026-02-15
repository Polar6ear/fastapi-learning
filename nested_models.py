from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_dict = {
    'city': 'New York',
    'state': 'NY',
    'pincode': 10001
}

address1 = Address(**address_dict)

patient_info = {
    'name': 'Nitin',
    'age': 42,
    'gender': 'Male',
    'address': address1
}
patient1 = Patient(**patient_info)

print(patient1)