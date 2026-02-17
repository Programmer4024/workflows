from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Employee Management System")

# Data Model
class Employee(BaseModel):
    id: int
    name: str
    role: str
    department: str

# In-memory database
db = []

@app.get("/")
def home():
    return {"status": "EMS API is Live on AWS", "BaseURL_Active": True}

@app.post("/employees/")
def add_employee(emp: Employee):
    db.append(emp)
    return {"message": f"Employee {emp.name} added successfully"}

@app.get("/employees/", response_model=List[Employee])
def get_employees():
    return db