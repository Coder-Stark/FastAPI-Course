"""
Project -> Patient's Profile Management by Doctor


Endpoints (CRUD)
1. /create  
2. /view
3. /view/patient_id
4. /update/patient_id
5. /delete/patient_id


HTTP Methods (4 majorly)
1. GET     ->      Read/View/Retrieve
2. POST    ->      Create/Add/Insert
3. PUT     ->      Update
4. DELETE  ->      Delete/remove
"""

from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


@app.get("/")
def hello():
    return {
        "message" : "Patient Management System API"
    }


@app.get("/about")
def about():
    return{
        "message" : "A fully functional API to manage your patient records"
    }


#open patients.json file
def load_data():
    with open("patients.json", 'r') as f:
        data = json.load(f)

    return data

@app.get("/view")
def view():
    data = load_data()

    return data


"""
Path Params
Path parameters are dynamic segments of a URL path
used to identify a specific resource.
"""

# @app.get("/patient/{patient_id}")
# def view_patient(patient_id : str):
#     #load all the patient
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     return {"error" : "patient not found"}


"""
Path()
used to provide metadata, validation rules and documentation
hints for path parameters in your API endpoints

Title, Description, Example, ge (>=), gt(>), le(<=), lt(<), Min_length, Max_length, regex
"""

# #Same above just with description and example
# @app.get("/patient/{patient_id}")
# def view_patient(patient_id : str = Path(..., description='ID of the patient in the DB', example='P001')):
#     #load all the patient
#     data = load_data()

#     if patient_id in data:
#         return data[patient_id]
#     return {"error" : "patient not found"}


"""
HTTP Status Codes
3 digits numbers returned by a web server to indicate the result of a 
client's request (like from a browser or API consumer)

2xx    ->        success
3xx    ->        redirection
4xx    ->        client side error
5xx    ->        server side error

some example
200    ->        standard success
201    ->        resource created
204    ->        success but no data (delete successfully)

400    ->        bad request (invalid request)
401    ->        unauthorized
403    ->        forbidden (authentication but no permission)
404    ->        not found (resource doesn't exist)

500     ->       internal server error (generic failure)
502     ->       bad gateway (like ngnix failed to reach backend)
503     ->       service unavailable (server is down or overloaded)


HTTPException
special built-in exception in FastAPI used to return custom HTTP error responses
when something goes wrong in your API
"""

#Same above just with httpexecption
@app.get("/patient/{patient_id}")
def view_patient(
    patient_id : str = Path(
        ...,                           #required
        description='ID of the patient in the DB', 
        example='P001'
    )
):
    #load all the patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


"""
Query Parameter (?)
optional key-value paris appended to the end of a url used to pass additional data
to server in http request (eg. ?sort=desc)
"""

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(
        ..., 
        description='Sort on the basis of height, weight or bmi'
    ), 
    order: str = Query(
        'asc', 
        description='Sort in asc or desc order'
    )
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')

    data = load_data()

    sort_order = True if order=="desc" else False             #(ternary operator like in js condition : true : false   in python    true condition false)
    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=sort_order)      #reverse -> false (always asc) and true (always desc)

    return sorted_data


"""
url - > http://127.0.0.1:8000/sort?sort_by=bmi&order=desc

output

[
  {
    "name": "Ananya Verma",
    "city": "Guwahati",
    "age": 28,
    "gender": "female",
    "height": 1.65,
    "weight": 90,
    "bmi": 33.06,
    "verdict": "Obese"
  },
  {
    "name": "Neha Sinha",
    "city": "Kolkata",
    "age": 30,
    "gender": "female",
    "height": 1.55,
    "weight": 75,
    "bmi": 31.22,
    "verdict": "Obese"
  },
  {
    "name": "Arjun Verma",
    "city": "Mumbai",
    "age": 40,
    "gender": "male",
    "height": 1.8,
    "weight": 90,
    "bmi": 27.78,
    "verdict": "Normal"
  },
  {
    "name": "Ravi Mehta",
    "city": "Mumbai",
    "age": 35,
    "gender": "male",
    "height": 1.75,
    "weight": 85,
    "bmi": 27.76,
    "verdict": "Overweight"
  },
  {
    "name": "Sneha Kulkarni",
    "city": "Pune",
    "age": 22,
    "gender": "female",
    "height": 1.6,
    "weight": 45,
    "bmi": 17.58,
    "verdict": "Underweight"
  }
]
"""