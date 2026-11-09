#why we should use pydantic
"""
To overcome the 2 problems 
1. Type validation
2. Data validation 
"""

#Problem 1 : Type validation
def insert_patient_data(name, age):
    print(name)
    print(age)
    print('inserted into database')

insert_patient_data('nitish', 'thirty')     #name and age are of any type (cause problems later)

#1st way to resolve (type hunting -> at the time of code another programmer see type)
#but it can not create error so the code can bypass

# def insert_patient_data(name:str, age: int)   


#2nd way (strictly enforce) -> not scalable

def insert_patient_data2(name:str, age:int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError('Incorrect data type')

insert_patient_data2('nitish', 30)    


#again we have to do same thing
def update_patient_data2(name:str, age:int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print('inserted into database')
    else:
        raise TypeError('Incorrect data type')


#Problem 2 : Data validation
def insert_patient_data3(name:str, age:int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError('Age cant be negative')
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError('Incorrect data type')

insert_patient_data2('nitish', 30)    

#same for update



"""
outputs

nitish
thirty
inserted into database

nitish
30
inserted into database

nitish
30
inserted into database

"""