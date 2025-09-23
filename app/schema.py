from datetime import datetime
import strawberry
from typing import List,Optional
from app.models import Task, SessionLocal
from sqlalchemy.exc import SQLAlchemyError

# Strawberry type for the Task
@strawberry.type
class TaskType:
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime

# ----------------- Mutations -----------------
@strawberry.type
class Mutation:
    #   Add a task by its given title
    @strawberry.mutation
    def add_task(self, title: str) -> Optional[TaskType]:
        db = SessionLocal()
        try:
            new_task = Task(title=title)
            db.add(new_task)
            db.commit()
            db.refresh(new_task)
            return new_task
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Database error: {e}")
            raise Exception("Failed to add new task.")
        finally:
            db.close()

       

    @strawberry.mutation      
    def toggle_task(self, id: int) -> Optional[TaskType]:
        db = SessionLocal()
        try:
            task = db.query(Task).filter(Task.id == id).first()
            if not task:
                return None
            task.completed = not task.completed
            task.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(task)
            return task
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Database error: {e}")
            raise Exception(f"Failed to toggle task with ID {id}.")
        finally:
            db.close()
            

    #   Deletes a task by its ID
    @strawberry.mutation
    def delete_task(self, id: int) -> Optional[TaskType]:
        db = SessionLocal()
        try:
            task = db.query(Task).filter(Task.id == id).first()
            if not task:
                return None
            db.delete(task)
            db.commit()
            return task
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Database error: {e}")
            raise Exception(f"Failed to delete task with ID {id}.")
        finally:
            db.close()
    
    

# GraphQL Query class with database error handling
@strawberry.type
class Query:
    @strawberry.field
    def all_tasks(self) -> List[TaskType]:
            db = SessionLocal()
            try:
                tasks = db.query(Task).order_by(Task.id).all()
                return tasks
            except SQLAlchemyError as e:
                print(f"Database error: {e}")
                raise Exception("Failed to fetch tasks from the database.")
            finally:
                db.close()

    @strawberry.field
    def task(self, id: int) -> Optional[TaskType]:
        """Fetches a single task by its ID."""
        db = SessionLocal()
        try:
           
            task = db.query(Task).filter(Task.id == id).first()
            return task
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            raise Exception("Failed to fetch task from the database.")
        finally:
            db.close()
    
    @strawberry.field
    def tasks_by_completion(self, completed: bool) -> List[TaskType]:
        """Fetches all tasks based on their completion status."""
        db = SessionLocal()
        try:
            tasks = db.query(Task).filter(Task.completed == completed).all()
            return tasks
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            raise Exception("Failed to fetch tasks by completion status.")
        finally:
            db.close()

# Create the GraphQL schema
schema = strawberry.Schema(query=Query,mutation=Mutation)