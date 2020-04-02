import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './logo.svg';
import Toolbar from './components/Toolbar'
import './App.css';
import './Palette.css'
import CritterTable from './components/CritterTable';

const fetch = require('node-fetch');

function App() {
  
  function hello(){
  fetch('https://seasonpedia.com/crit/fish/King-Salmon')
	.then(res => res.text())
	.then(body => {
		console.log(body + '\n');
    let obj = JSON.parse(body);
    let msg = obj.name + ' appears in: ' + obj['Northern Hemisphere'] + ', sells for ' + obj.price + ' and can be found at: ' + obj.time;
    console.log(msg);
    alert(msg);
});
  }

  return (
    <div className="App">
      <Toolbar></Toolbar>
      <CritterTable></CritterTable>
      <header className="App-header">
      <button onClick={hello}> CLICK ME </button>

        
        <img src={logo} className="App-logo" alt="logo"/>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <h1 className="cream">HELLOOOOOO</h1>
      </header>
    </div>
  );
}

export default App;

