import React from 'react';
import ReactDOM from 'react';
import logo from './logo.svg';
import './App.css';

const welcome = {
  greeting: 'Hey',
  title: 'React',
};

function getTitle(title){
  return title;
};

const list = [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org"
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net"
  },
];

const List = () =>{
  return list.map(item => {
    return (
          <div key={item.id}>
              <span>name : {item.name}</span>
              <span>name : {item.username}</span>
              <span>phone : {item.phone}</span>
              <span>website : 
                <a href='http://{item.website}'>
                      {item.website}</a></span>
              <span>email : {item.email}</span>          
          </div>
    );
  });
}

class Developer {
  constructor(firstName, lastName){
    this.firstName = firstName;
    this.lastName = lastName;
  } 

  getName(){
    let date = new Date().toLocaleTimeString()
    return this.firstName 
    + " " + this.lastName
    + " (" + date + ")";
  }
}

<></>

const robin = new Developer("Robin", "Wieruch");
console.log(robin.getName());

const App = () => {
  const initialStories = [

    {
      title: 'React',
      url: 'https://reactjs.org/',
      author: 'Jordan Walke',
      num_comments: 3,
      points: 4,
      objectID: 0,
    },
    {
      title: 'Redux',
      url: 'https://redux.js.org/',
      author: 'Dan Abramov',
      num_comments: 2,
      points: 5,
      objectID: 1,
    },

  ];


  return (
    <div>
      <h1>My Hacker Stories</h1>

      <Search onSearch={handleSearch} />

      <hr />

      <List list={stories} />
    </div>
  );
};


const Search = props => {
  const [searchTerm, setSearchTerm] = React.useState('');

  const handleChange = event => {
    setSearchTerm(event.target.value);

    // B
    props.onSearch(event);
  };

  return (
      <div>
      <label htmlFor="search">Search: </label>
      <input
        id="search"
        type="text"
        value={searchTerm}
        onChange={handleChange}
      />
      </div>
  );
};



export default App;