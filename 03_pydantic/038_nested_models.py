#Nested Models
"""
1. better organization of related data
2. reusability 
3. readability
4. validation (nested models are already validated)
"""

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'harayana', 'pin': '122001'}
address1 = Address(**address_dict)

patient_dict = {'name': 'shivam', 'gender': 'male', 'age': 25, 'address': address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)


"""
outputs

name='shivam' gender='male' age=25 address=Address(city='gurgaon', state='harayana', pin='122001')
shivam
gurgaon
122001
"""