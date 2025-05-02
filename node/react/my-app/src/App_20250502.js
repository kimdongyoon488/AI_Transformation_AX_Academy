import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

// 컴포넌트 정의
const Home = () => <h2>🏠 홈 페이지입니다</h2>;
const About = () => <h2>📘 소개 페이지입니다</h2>;
const Contact = () => <h2>📞 연락처 페이지입니다</h2>;

function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
        <h1>🌐 React Router 예제</h1>

        {/* 네비게이션 메뉴 */}
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/" style={{ marginRight: '10px' }}>홈</Link>
          <Link to="/about" style={{ marginRight: '10px' }}>소개</Link>
          <Link to="/contact">연락처</Link>
        </nav>

        {/* 경로에 따라 컴포넌트 렌더링 */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;