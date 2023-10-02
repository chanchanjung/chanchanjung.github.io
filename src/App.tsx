import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Route, Routes} from "react-router-dom";
import {Main} from "./pages/Main";
import {Interface} from "./pages/java/Interface";

function App() {
    return (
        <Routes>
            <Route path="/" element={<Main/>}/>
            <Route path="/interface" element={<Interface/>}/>
        </Routes>
    );

}
export default App;
