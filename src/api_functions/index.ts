// Define the base URL
const BASE_URL = 'http://localhost:8000';

// Function to perform a GET request
export async function fetchData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

// Function to perform a POST request
export async function createData(url, data) {
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error('Failed to create resource');
    }
    const createdData = await response.json();
    return createdData;
  } catch (error) {
    console.error('Error creating data:', error);
    throw error;
  }
}

// Function to perform a PUT request
export async function updateData(url, data) {
  try {
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    if (!response.ok) {
      throw new Error('Failed to update resource');
    }
    const updatedData = await response.json();
    return updatedData;
  } catch (error) {
    console.error('Error updating data:', error);
    throw error;
  }
}

// Function to perform a DELETE request
export async function deleteData(url) {
  try {
    const response = await fetch(url, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error('Failed to delete resource');
    }
    return 'Resource deleted successfully';
  } catch (error) {
    console.error('Error deleting data:', error);
    throw error;
  }
}

// Example usage:
// Replace '/tasks/' with the appropriate endpoint for your API
const tasksUrl = `${BASE_URL}/tasks/`;

// Fetch all tasks
export function getTasks(){
fetchData(tasksUrl)
  .then(tasks => console.log('Tasks:', tasks))
  .catch(error => console.error('Error fetching tasks:', error));
}

// Create a new task
const newTask = {
  id: 1,
  name: 'New Task',
  due_date: '2024-04-30',
};

//type Task: Object
type Task = {
  id: number;
  name: string;
  due_date: string;
};

export function createTasks(newTask: Task){
createData(tasksUrl, newTask)
  .then(createdTask => console.log('Created task:', createdTask))
  .catch(error => console.error('Error creating task:', error));
}

// Update an existing task
const taskId = 1;
const updatedTask = {
  name: 'Updated Task Name',
};

export function updateTask(updatedTask: Task){
updateData(`${tasksUrl}/${taskId}`, updatedTask)
  .then(updatedTask => console.log('Updated task:', updatedTask))
  .catch(error => console.error('Error updating task:', error));
}

// Delete an existing task
export function deleteTask(taskId: int){
deleteData(`${tasksUrl}/${taskId}`)
  .then(response => console.log('Response:', response))
  .catch(error => console.error('Error deleting task:', error));
}
