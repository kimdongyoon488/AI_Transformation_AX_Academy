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

  return (
      <div>
        <h1>My Hacker Stories</h1>
        <label htmlFor='search'>Search:</label>
        <input id='search' type="text"/>
        <hr/>
          <List />
      </div>
  );
  // const a = 0;
  // console.log1(a);

}



export default App;