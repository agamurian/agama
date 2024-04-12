# api_improvements.py

from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

JSON_PATH = "./data.json"

class Controller():
    @staticmethod
    def get_from_json(key: str):
        with open(JSON_PATH, encoding="UTF8") as json_data:
            data = json.loads(json_data.read())
            return data.get(key, {})

    @staticmethod
    def find(id:int, data:list):
        for element in data:
            if "id" in element.keys() and int(element["id"]) == id:
                return element
        raise HTTPException(status_code=404, detail="Item not found")

    @staticmethod
    def append(key: str, element: dict):
        existing_data = Controller.get_from_json(key)
        existing_data.append(element)
        with open(JSON_PATH, "w", encoding="UTF8") as json_data:
            json_data.write(json.dumps(existing_data))
        return "success"

    @staticmethod
    def delete(key: str, id: int):
        existing_data = Controller.get_from_json(key)
        for item in existing_data:
            if item.get("id") == id:
                existing_data.remove(item)
                with open(JSON_PATH, "w", encoding="UTF8") as json_data:
                    json_data.write(json.dumps(existing_data))
                return "success"
        raise HTTPException(status_code=404, detail="Item not found")

class Task(BaseModel):
    id: int
    name: str
    due_date: str

    @staticmethod
    def get_all_from_json():
        return Controller.get_from_json("tasks")

    @staticmethod
    def find(id):
        task = Controller.find(id, Task.get_all_from_json())
        return task

class Note(BaseModel):
    id: int
    title: str
    content: str

    @staticmethod
    def get_all_from_json():
        return Controller.get_from_json("notes")

    @staticmethod
    def append(note):
        Controller.append("notes", note)

    @staticmethod
    def delete(id: int):
        Controller.delete("notes", id)

class Bookmark(BaseModel):
    id: int
    link: str

    @staticmethod
    def get_all_from_json():
        return Controller.get_from_json("bookmarks")

    @staticmethod
    def append(bookmark):
        Controller.append("bookmarks", bookmark)

    @staticmethod
    def delete(id: int):
        Controller.delete("bookmarks", id)

# New API Endpoints

# PATCH endpoint for partial updates
@app.patch("/tasks/{task_id}")
def partial_update_task(task_id: int, task: Task):
    existing_task = Task.find(task_id)
    for field, value in task.dict().items():
        if value is not None:
            setattr(existing_task, field, value)
    return existing_task

# GET endpoint for searching tasks by name
@app.get("/tasks/search/")
def search_tasks(name: str):
    tasks = Task.get_all_from_json()
    return [task for task in tasks if task["name"] == name]

# GET endpoint for paginated tasks
@app.get("/tasks/paginated/")
def get_paginated_tasks(skip: int = 0, limit: int = 10):
    tasks = Task.get_all_from_json()
    return tasks[skip: skip + limit]

# GET endpoint for sorted tasks by due date
@app.get("/tasks/sorted/")
def get_sorted_tasks():
    tasks = Task.get_all_from_json()
    return sorted(tasks, key=lambda x: x["due_date"])

