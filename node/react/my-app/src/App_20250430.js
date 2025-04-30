import React, { useState, useEffect } from 'react';

const App = () => {
  // localStorage에서 name 불러오기 (없으면 빈 문자열로 시작)
  const [name, setName] = useState(localStorage.getItem('name') || '');

  // name이 바뀔 때마다 localStorage에 저장
  useEffect(() => {
    localStorage.setItem('name', name);
  }, [name]);

  // 입력값이 바뀔 때 상태 변경
  const handleChange = (e) => {
    setName(e.target.value);
  };

  return (
    <div>
      <h1>안녕하세요, {name || '방문자'}님!</h1>
      <input
        type="text"
        value={name}
        onChange={handleChange}
        placeholder="이름을 입력하세요"
      />
    </div>
  );
};

export default App;
