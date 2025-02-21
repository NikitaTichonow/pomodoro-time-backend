from fastapi import FastAPI, APIRouter, status
from fixtures import tasks as fixtures_task
from schema.tasks import Task

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/all", response_model=list[Task])
async def get_tasks():
    return fixtures_task


@router.post("/", response_model=Task)
async def create_task(task: Task):
    fixtures_task.append(task)
    return task


@router.patch("/{task_id}", response_model=Task)
async def update_task(task_id: int, name: str):
    for task in fixtures_task:
        if task["id"] == task_id:
            task['name'] = name
            return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(fixtures_task):
        if task["id"] == task_id:
            del fixtures_task[index]
            return {"message": f"task {task_id} deleted"}
        
    return {"message": f"task {task_id} not found"}, status.HTTP_404_NOT_FOUND


