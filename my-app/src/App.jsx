import React from 'react';
import {BrowserRouter as Router, Routes,Route, Link} from "react-router-dom";
import Home from './pages/home';

//import './styles.css';

/*const Home = () => {
  return (
    <div>
      <h1>Home Page</h1>
    </div>
  );
}*/

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
        <li>
          <Link to="/">Home</Link>
          <Link to="/aboutPage"> About </Link>
        </li>

        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/aboutPage" element={<About/>}/>
        </Routes>
      </div> 
    </Router> 
  );
}


export default App;
