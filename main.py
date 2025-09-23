from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema import schema
from sqlalchemy import inspect
from app.models import create_tables, SessionLocal, Task,engine

# Initialize FastAPI app
app = FastAPI()


# ----------------- Database Startup Check -----------------
@app.on_event("startup")
def startup_event():
    """Checks if the 'tasks' table exists and creates it if not."""
    inspector = inspect(engine)
    if not inspector.has_table("tasks"):
        print("Table 'tasks' does not exist. Creating table...")
        create_tables()
        
        # Optional: Add initial data after table creation
        db = SessionLocal()
        try:
            db.add_all([
                Task(title="Initial task 1", completed=False),
                Task(title="Initial task 2", completed=True)
            ])
            db.commit()
            print("Initial data added to the 'tasks' table.")
        except Exception as e:
            db.rollback()
            print(f"Failed to add initial data: {e}")
        finally:
            db.close()
    else:
        print("Table 'tasks' already exists. Skipping creation.")


# Create GraphQL router
graphql_app = GraphQLRouter(schema)

# Add GraphQL endpoint
app.include_router(graphql_app, prefix="/graphql")

# A simple root endpoint to confirm the server is running
@app.get("/")
def read_root():
    return {"message": "Welcome to the Lush Tasks FastAPI GraphQL API!"}


