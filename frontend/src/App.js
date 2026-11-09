// Filename - App.js

// Importing modules
import React, { useState, useEffect } from "react";
import { NavLink, Routes, Route } from 'react-router-dom';
import "./App.css";

import "./App.css";
import Form from "./createActForm"
import DayView from "./DayView"
import WeekView from "./WeekView";
import MonthView from "./MonthView";



function App(){
    const body_app = new FormData()
    body_app.append('type', 'info')
    body_app.append('msg', 'Frontend App initiated with main.')
    fetch('/log', {method: 'POST', body: body_app})
        .catch(error => console.log(error))
    return(
        <Main/>
    );
}

function Main(){
    const body_main = new FormData()
    body_main.append('type', 'info')
    body_main.append('msg', 'Frontend Main initiated with Routes.')
    fetch('/log', {method: 'POST', body: body_main})
        .catch(error => console.log(error))
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