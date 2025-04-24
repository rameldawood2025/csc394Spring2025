from fastapi import FastAPI, Form
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

users = []
workouts = []
meals = []

openai.api_key = os.getenv("OPENAI_API_KEY")

# USERS

@app.get("/users")
async def get_users():
    return {"users": users}

@app.post("/users")
async def add_user(name: str = Form(...)):
    users.append(name)
    return {"users": users}

@app.delete("/users")
async def delete_user(index: int = 0):
    if 0 <= index < len(users):
        users.pop(index)
    return {"users": users}

# WORKOUTS

@app.get("/workouts")
async def get_workouts():
    return {"workouts": workouts}

@app.post("/workouts")
async def add_workout(name: str = Form(...)):
    workouts.append(name)
    return {"workouts": workouts}

@app.delete("/workouts")
async def delete_workout(index: int = 0):
    if 0 <= index < len(workouts):
        workouts.pop(index)
    return {"workouts": workouts}

# MEALS

@app.get("/meals")
async def get_meals():
    return {"meals": meals}

@app.post("/meals")
async def add_meal(name: str = Form(...)):
    meals.append(name)
    return {"meals": meals}

@app.delete("/meals")
async def delete_meal(index: int = 0):
    if 0 <= index < len(meals):
        meals.pop(index)
    return {"meals": meals}

# SMART ENDPOINT

@app.get("/recommendation")
async def get_workout_recommendation():
    if not workouts:
        return {"message": "No workouts found. Add some workouts first!"}

    prompt = f"Suggest a new workout based on the user's previous workouts: {', '.join(workouts)}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        suggestion = response['choices'][0]['message']['content']
        return {"recommendation": suggestion}
    except Exception as e:
        return {"error": str(e)}






