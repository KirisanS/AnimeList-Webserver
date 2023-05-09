import React from 'react';
import {BrowserRouter as Router, Routes,Route} from "react-router-dom";
import Home from './pages/home';

//import './styles.css';


const About = () => {
  return(
    <div> 
      <h1>About Page</h1>
    </div>
  )
}

const App = ()  => {

  return (
    <Router>
      <div> 
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/aboutPage" element={<About/>}/>
        </Routes>
      </div> 
    </Router> 
  );
}


export default App;
