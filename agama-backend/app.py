from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import json
# from app_improvements import *

app = FastAPI()

JSON_PATH = "./data.json"
# define controller functions:
class Controller():
    @staticmethod
    def get_from_json(key: str):
        """load any data by key from storage by key"""
        with open(JSON_PATH, encoding="UTF8") as json_data:
            data = json.loads(json_data.read())
            requested_data = data[key]
        return requested_data

    @staticmethod
    def find(id:int, data:list):
        for element in data:
            if "id" in element.keys():
                if int(element["id"]) == id:
                    return element
            else: 
                print("this element have no id")


    @staticmethod
    def append(key: str, element: dict):
        "add element to existing data, for example single note to all notes"
        existing_data = Controller.get_from_json(key)
        updated_data = existing_data + element
        with open(JSON_PATH, encoding="UTF8") as json_data:
            json_data.write(json.dumps(updated_data))
        return "success"

    @staticmethod
    def delete(key: str, id: int):
        "add data to existing data, for example single note to all notes"
        existing_data = Controller.get_from_json(key)
        data_to_delete = Controller.find(id, existing_data)
        updated_data = existing_data - data_to_delete
        with open(JSON_PATH, encoding="UTF8") as json_data:
            json_data.write(json.dumps(updated_data))
        return "success"



# Define models
class Task(BaseModel):
    id: int
    name: str
    due_date: str

    @staticmethod
    def get_all_from_json():
        """get all notes from json data storage"""
        return Controller.get_from_json("tasks")

    @staticmethod
    def find(id):
        task = Controller.find(id,Task.get_all_from_json())
        return task

    @staticmethod
    def create(name:str):
        """ create a new task"""
        placeholder = "some"
        tasks = Task.get_all_from_json()
        tasks += {"name": name, "content": placeholder, "due_date":"20122024"}


class Note(BaseModel):
    id: int
    title: str
    content: str

    @staticmethod
    def get_all_from_json():
        """get all notes from json data storage"""
        return Controller.get_from_json("notes")

    @staticmethod
    def append(note):
        Controller.append("note",note)

class Bookmark(BaseModel):
    id: int
    link: str

    @staticmethod
    def get_all_from_json():
        """get all notes from json data storage"""
        return Controller.get_from_json("bookmarks")

# Sample data
notes = Note.get_all_from_json()
bookmarks = Bookmark.get_all_from_json()

# Routes for tasks
@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    tasks = Task.get_all_from_json()
    return tasks

@app.get("/tasks/{task_id}")
def get_single_task(task_id: int):
    task = Task.find(task_id)
    return task

@app.post("/tasks/")
def create_task(task: Task):
    Task.create(task)
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    task = Task.find(task_id)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    del tasks[task_id]

# Routes for notes
@app.get("/notes/", response_model=List[Note])
def get_notes():
    return notes

@app.post("/notes/")
def create_note(note: Note):
    notes.append(note)
    return note

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    notes[note_id] = note
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    del notes[note_id]

# Routes for bookmarks
@app.get("/bookmarks/", response_model=List[Bookmark])
def get_bookmarks():
    return bookmarks

@app.post("/bookmarks/")
def create_bookmark(bookmark: Bookmark):
    bookmarks.append(bookmark)
    return bookmark

@app.put("/bookmarks/{bookmark_id}")
def update_bookmark(bookmark_id: int, bookmark: Bookmark):
    bookmarks[bookmark_id] = bookmark
    return bookmark

@app.delete("/bookmarks/{bookmark_id}")
def delete_bookmark(bookmark_id: int):
    del bookmarks[bookmark_id]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

