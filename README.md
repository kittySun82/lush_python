# lush_python
Practising to use FastAPI, Python, SQLAlchemy, Sqlite and Strawberry GraphQL to manage a simple list of tasks

## Getting Started

Follow these steps to download, install requirements, and start the FastAPI server:

### Prerequisites

- Ensure you have latest Python 3.13 or higher installed.

### Download and Install

1. Clone the repository:

   ```git clone https://github.com/your-username/your-fastapi-project.git```

2. Change into the project directory:

   ```cd lush-python```

3. Create and activate a virtual environment:

   ```python -m venv venv```
   ```venv\Scripts\activate```

4. Install dependencies:

   ```pip install -r requirements.txt```
   
### Start FastAPI Server

Run the FastAPI server with the following command:

   ```uvicorn main:app --reload```

Visit http://127.0.0.1:8000/docs in your browser to access the Swagger documentation and explore available API endpoints.

## GraphQL API

### Access the GraphQL Playground

Visit http://127.0.0.1:8000/graphql in your browser to access the GraphQL Playground.

### Examples of GraphQL Queries

#### Get Tasks Data
```graphql
query
query {
  allTasks {
    id
    title
    completed
    createdAt
    updatedAt
  }


  task(id:1) {
    id
    title
    completed
    createdAt
    updatedAt
  }
  tasksByCompletion(completed:true) {
    id
    title
    completed
    createdAt
    updatedAt
  }
}

```
#### Response:
```
{
  "data": {
    "allTasks": [{
        "id": 1,
        "title": "Pack at least 300 Scooby as gift ",
        "completed": true,
        "createdAt": "2025-09-22T19:51:53.854048",
        "updatedAt": "2025-09-23T20:26:37.694131"
      },
      {
        "id": 2,
        "title": "Make 100 Hello kitty bath ball ",
        "completed": false,
        "createdAt": "2025-09-22T19:53:28.664727",
        "updatedAt": "2025-09-22T19:53:28.664733"
      },
      {
        "id": 3,
        "title": "Produce 10 kg Citric",
        "completed": false,
        "createdAt": "2025-09-23T20:25:21.012303",
        "updatedAt": "2025-09-23T20:25:21.012308"
      }
    ],
    "task": {
      "id": 1,
      "title": "Pack at least 300 Scooby as gift ",
      "completed": true,
      "createdAt": "2025-09-22T19:51:53.854048",
      "updatedAt": "2025-09-23T20:26:37.694131"
    },
    "tasksByCompletion": [{
        "id": 1,
        "title": "Pack at least 300 Scooby as gift ",
        "completed": true,
        "createdAt": "2025-09-22T19:51:53.854048",
        "updatedAt": "2025-09-23T20:26:37.694131"
      }
    ]
  }
}

``` 
### Mutation:
#### modify the data
``` graphql
mutation
mutation{
  addTask(title:"Make 200 scooby bath ball"){
    id
    title
    completed
    createdAt
    updatedAt
  }
  toggleTask(id:4){
    id
    title
    completed
    createdAt
    updatedAt 
  }
  deleteTask(id:4){
    id
    title
    completed
    createdAt
    updatedAt     
  }
}
``` 
####  Response:
``` 
{
  "data": {
    "addTask": {
      "id": 4,
      "title": "Make 200 scooby bath ball",
      "completed": false,
      "createdAt": "2025-09-24T16:16:17.158299",
      "updatedAt": "2025-09-24T16:16:17.158304"
    }
    "toggleTask": {
      "id": 4,
      "title": "Make 200 scooby bath ball",
      "completed": true,
      "createdAt": "2025-09-24T16:16:17.158299",
      "updatedAt": "2025-09-24T16:23:13.941113"
    },
    "deleteTask": {
      "id": 4,
      "title": "Make 200 scooby bath ball",
      "completed": true,
      "createdAt": "2025-09-24T16:16:17.158299",
      "updatedAt": "2025-09-24T16:23:13.941113"
    }
  }
}
```

### Addtional Error handling
#### Business Logic Errors: 
Examples include attempting to delete/modify a task that doesn't exist or adding a task with an empty title.

#### Validation Errors: 
The input data fails to meet the schema's requirements (e.g., providing an id as a string instead of an integer).

#### Database Errors:
These are issues at the data layer, such as a database connection failure, can't find tasks table, a unique constraint violation, or a transaction deadlock.

#### Authentication/Authorization Errors: 
The user does not have permission to perform an action.

All these specific error types can be catches by creating custom, domain-specific exceptions.

### Addtional Queues
Like I have already added in the codes, tasks can not only be fetched by its id, but also by its completed status, search words in title or specified date. 


