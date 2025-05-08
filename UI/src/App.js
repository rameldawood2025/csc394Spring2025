import React, { useEffect, useState } from 'react';

function App() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/workouts') 
      .then(res => res.json())
      .then(data => {
        setWorkouts(data.workouts); 
      })
      .catch(err => console.error("API error:", err));
  }, []);

  return (
    <div style={{ fontFamily: 'Arial', padding: '20px' }}>
      <nav>
        <a href="/">Home</a> | <a href="/workouts">Workouts</a>
      </nav>
      <h1>My Workouts</h1>
      <ul>
        {workouts.map((w, index) => (
          <li key={index}>
            <strong>{w.name}</strong> — {w.target}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;




















