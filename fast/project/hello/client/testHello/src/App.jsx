import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <a href="http://localhost:8000">fast api test </a>
        <form method="post" action="http://localhost:8000/items/2">
          <input name="q"></input>
          <button type="submit">제출</button>
        </form>
    </>  
  )
}

export default App
