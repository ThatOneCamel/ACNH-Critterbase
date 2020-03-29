import React from 'react';
import logo from './logo.svg';
import Toolbar from './components/Toolbar'
import './App.css';
import './Palette.css'

function App() {
  return (
    <div className="App">
      <Toolbar></Toolbar>
      <header className="App-header">
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

