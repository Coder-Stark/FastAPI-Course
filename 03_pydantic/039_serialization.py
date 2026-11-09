#SERIALIZATION

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

temp = patient1.model_dump()

print(temp)
print(type(temp))

temp = patient1.model_dump_json()

print(temp)
print(type(temp))


#export specific only
temp1 = patient1.model_dump(include=['name', 'gender'])
print(temp1)

temp2 = patient1.model_dump(exclude=['name', 'gender'])
print(temp2)

temp3 = patient1.model_dump(exclude={'address': ['state']})
print(temp3)


"""
outputs
{'name': 'shivam', 'gender': 'male', 'age': 25, 'address': {'city': 'gurgaon', 'state': 'harayana', 'pin': '122001'}}
<class 'dict'>

{"name":"shivam","gender":"male","age":25,"address":{"city":"gurgaon","state":"harayana","pin":"122001"}}
<class 'str'>


{'name': 'shivam', 'gender': 'male'}

{'age': 25, 'address': {'city': 'gurgaon', 'state': 'harayana', 'pin': '122001'}}

{'name': 'shivam', 'gender': 'male', 'age': 25, 'address': {'city': 'gurgaon', 'pin': '122001'}}

"""