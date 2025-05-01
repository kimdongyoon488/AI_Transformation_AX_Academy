import React from 'react';

// 임의의 초기 데이터 (스토리 배열)
const initialStories = [
  { id: 1, title: '제목1', author: '김동윤' },
  { id: 2, title: '제목2', author: '홍길동' },
  { id: 3, title: '제목3', author: '원빈' },
];

// 2초 후 데이터를 응답하는 "가짜 API"
const getAsyncStories = () =>
  new Promise((resolve) =>
    setTimeout(() => {
      resolve({ data: { stories: initialStories } });
    }, 2000)
  );

// 메인 App 컴포넌트
const App = () => {
  const [stories, setStories] = React.useState([]); // 처음엔 빈 배열

  React.useEffect(() => {
    getAsyncStories().then((result) => {
      setStories(result.data.stories); // 받아온 데이터로 상태 업데이트
    });
  }, []); // 마운트 시 1회만 실행됨

  return (
    <div>
      <h1>스토리 목록</h1>
      {stories.length === 0 ? (
        <p>로딩중</p>
      ) : (
        <ul>
          {stories.map((story) => (
            <li key={story.id}>
              <strong>{story.title}</strong> — {story.author}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default App;