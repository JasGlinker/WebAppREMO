// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import { NavLink, Routes, Route } from 'react-router-dom';


import "./App.css";
import Form from "./createActForm"
import DayView from "./DayView"
import WeekView from "./WeekView";
import MonthView from "./MonthView";



function App(){
    return(
        <Main/>
    );
}

function Main(){
    return(
        <Routes>
            <Route path="/" element={<DayView/>}></Route>
            <Route path="/create" element={<Form/>}></Route>
            <Route path="/week" element={<WeekView/>}></Route>
            <Route path="/month" element={<MonthView/>}></Route>
        </Routes>
    );
}

export default App;