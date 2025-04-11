from fastapi import FastAPI

app = FastAPI()

workout_list = ["Banana", "Apple", "Orange"]

@app.get("/workouts")
async def get_strings():
    return {"workouts": workout_list}

@app.post("/workouts")
async def add_string(name: str = ""):
    workout_list.append(name)
    return {"workouts": workout_list}

@app.delete("/workouts")
async def delete_string(index: int = 0):
    workout_list.pop(index)
    return {"workouts": workout_list}