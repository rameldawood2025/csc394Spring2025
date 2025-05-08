import React, { useState, useEffect } from "react";

function WorkoutList() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/workouts")
      .then((response) => response.json())
      .then((data) => {
        setWorkouts(data.workouts || []); // assuming API returns { "workouts": [...] }
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching workouts:", error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <h1>Workout List</h1>
      <ul>
        {workouts.map((workout, index) => (
          <li key={index}>{workout}</li>
        ))}
      </ul>
    </div>
  );
}

export default WorkoutList;



