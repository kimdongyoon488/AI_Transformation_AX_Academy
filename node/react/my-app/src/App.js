import logo from './logo.svg';
import './App.css';

const tableStyle = {
  backgroundColor :"yellow",
  fontsize: "20px"
};

const welcome = {
  greeting : 'Hey',
  title: 'React',

};

function getTitle(title){
  return title;
};


function App() {
  let names = ["아이디","비밀번호","로그인","다시입력"];

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React1
        </a>
      </header>
      <div className="login-form">
                <h1>{welcome.greeting} {getTitle('리액트')}</h1>              
                <table border="1" style={tableStyle}>
                    <tr>
                        <td>{names[0]} </td><td><input id="id"/></td>
                    </tr>
                    <tr>
                        <td>{names[1]} </td><td><input id="pw"/></td>
                    </tr>
                    <tr>
                        <td colspan="2"><button onclick="login()">{names[2]}</button> <input type="reset" value={names[3]}/></td>
                    </tr>
                </table>
        </div>
    </div>
  );
}

export default App;
