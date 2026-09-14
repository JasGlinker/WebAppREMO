// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import { NavLink, Routes, Route } from 'react-router-dom';


import "./App.css";
import Form from "./createActForm"
import DayView from "./DayView"




function App(){
    return(
        <Main/>
    );
}

function Main(){
    return(
        <Routes>
            <Route path="/" element={<DayView/>}></Route>
            <Route path="/new" element={<Form/>}></Route>
        </Routes>
    );
}

export default App;