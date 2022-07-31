import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from './Header';
import Home from './Home';
import Forum from './forum';
import PlantID from "./PlantID";

function App() {
  return (
    <Router>
     <Routes>
      <Route path="/" element={<div className="App">
        <Header />
        <Home />
        <Forum />
      </div>}/> 
      <Route path="/PlantID" element={<PlantID />}/>
    </Routes>
    </Router>
  );
}

export default App;
