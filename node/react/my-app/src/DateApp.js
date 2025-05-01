import React, { useState } from 'react';
import { MyDate } from './Date';

function App() {

  const [year, setYear] = useState('');
  const [month, setMonth] = useState('');
  const [day, setDay] = useState('');
  const [isAdd, setIsAdd] = useState(false); // 등록 버튼 클릭 여부
  const [message, setMessage] = useState('');

  const handleClick = () => {

    const dateObj = new MyDate(Number(year), Number(month), Number(day));

    if (!isAdd) {
      setMessage(dateObj.getFormattedDate());
      setIsAdd(true);
    } else {
      setMessage(dateObj.getFormattedDate());
    }
  };

  return (
    <>
      <div>
        <label>년:</label>
        <input type="number" value={year}
          onChange={(e) => setYear(e.target.value)}></input>
      </div>
      <div>
        <label>월:</label>
        <input type="number" value={month}
          onChange={(e) => setMonth(e.target.value)}></input>
      </div>
      <div>
        <label>일:</label>
        <input type="number" value={day}
          onChange={(e) => setDay(e.target.value)}></input>
      </div>

      <button onClick={handleClick}>
          {isAdd ? '수정' : '등록'}
      </button>

      {message && <p>{message}</p>}

    </>  
    
  );
}

export default App;
