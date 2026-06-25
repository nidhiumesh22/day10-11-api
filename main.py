from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    id: str
    name: str
    department: str
    salary: int

employees = [
    {
        "id": "101",
        "name": "John",
        "department": "HR",
        "salary": 50000
    }
]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/employees")
def get_employees():
    return employees

@app.post("/employees")
def add_employee(employee: Employee):
    employees.append(employee.dict())
    return {"message": "Employee added successfully"}
