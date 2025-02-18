import Home from "./pages/Home";
import InputData from "./pages/InputData";
import MyApp from "./pages/TestPrime";

import React from "react";
import {Route, Routes, Link} from "react-router-dom";
import "./App.css";


function App() {
  return (
    <div className="App">
      <nav className="menu">
        <Link to="/">Home</Link> | {""}
        <Link to="/inputdata">InputData</Link> | {""}
        <Link to="/myapp">MyApp</Link> {""}
      </nav>
      <Routes>
        <Route path="/" element={<Home />} ></Route>
        <Route path="/inputdata" element={<InputData />} ></Route>
        <Route path="/myapp" element={<MyApp />} ></Route>  
      </Routes>
      </div>
  );
}

//Link to ~~ -> <a href="/">Home</a>
//Link태그는 A태그로 나옴


//<nav태그> -> <routers태그>
// to아래 값을 똑같은 path를 가진 값을 라우터에서 찾아서 
// 그 elemet속성에 할당되어 있는 react 컴포넌트를 보여줌
export default App;
