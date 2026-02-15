from pydantic import BaseModel


class Address(BaseModel):
    city: str
    pincode: int

class Patient(BaseModel):
    name: str
    address: Address

a_data = {
    'city': 'New York',
    'pincode': 10001
}

a1 = Address(**a_data)

p_data = {
    'name': 'Nitin',
    'address': a_data
}

p1 = Patient(**p_data)

temp = p1.model_dump()
temp2 = p1.model_dump_json()
print(temp) #dictionary me convert ho jayega --> {'name': 'Nitin', 'address': {'city': 'New York', 'pincode': 10001}}
print(p1) #normal object print hoga --> name='Nitin' address=Address(city='New York', pincode=10001)
print(temp2)
