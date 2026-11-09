"""
Pydantic (alternative of zod in js)
1. Define a pydantic model
2. instantiate(create instance from a class) the model with raw input data
3. pass the validated model object

install via pip
-> pip install pydantic
or
#install package in correct environment
-> python -m pip install pydantic
"""

from pydantic import BaseModel

#1. Define a pydantic model
class Patient(BaseModel):
    name: str
    age: int

#2 instantiate from model with raw input data
# patient_info = {'name': 'shivam', 'age': 'twenty five'}        #now not possible
patient_info = {'name': 'shivam', 'age': 25}
patient1 = Patient(**patient_info)            
#** -> unpack dictonary into keywords arg 
#like (**patient_info) -> (name='shivam', age=25)

#3 pass the validated model object
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

insert_patient_data(patient1) 


#now no need to hardcore check for type validation we can use same to next functions
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated into database')

update_patient_data(patient1) 



"""
output

shivam
25
inserted into database
shivam
25
updated into database

"""