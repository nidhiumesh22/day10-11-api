from fastapi import FastAPI, HTTPException
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

@app.get("/employees/{id}")
def get_employee(id: str):
    for emp in employees:
        if emp["id"] == id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees")
def add_employee(employee: Employee):
    for emp in employees:
        if emp["id"] == employee.id:
            raise HTTPException(status_code=400, detail="Employee ID already exists")

    employees.append(employee.dict())
    return {"message": "Employee added successfully"}

@app.put("/employees/{id}")
def update_employee(id: str, employee: Employee):
    for emp in employees:
        if emp["id"] == id:
            emp["name"] = employee.name
            emp["department"] = employee.department
            emp["salary"] = employee.salary
            return {"message": "Employee updated successfully"}

    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{id}")
def delete_employee(id: str):
    for emp in employees:
        if emp["id"] == id:
            employees.remove(emp)
            return {"message": "Employee deleted successfully"}

    raise HTTPException(status_code=404, detail="Employee not found")