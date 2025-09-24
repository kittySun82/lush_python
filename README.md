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
#### Resposnse:
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
mutation

mutation{
  deleteTask(id:5){
    id
    title
    completed
    createdAt
    updatedAt
  }
  
  
}
