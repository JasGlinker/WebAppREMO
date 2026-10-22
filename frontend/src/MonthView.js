import React, {useState, useEffect} from "react";
import "./App.css";

import Week from "./week";
import Menu from "./menu";

function MonthView(){
    const [weeks, setWeeks] = useState([]);
    useEffect(() => {
        fetch('/month', {method: "GET"})
            .then((res) => res.json())
            .then((el) => {
                console.log(el);
                for (let week = 0; week < el.length; week++){
                    console.log("week:", el[week])
//
                    setWeeks(values => [...values, <Week week={el[week]}/>])
                }
            })

    }, []);

    const body_Monthview = new FormData()
    body_Monthview.append('type', 'info')
    body_Monthview.append('msg', 'Frontend Monthview build')
    fetch('/log', {method: 'POST', body: body_Monthview})
        .catch(error => console.log(error))

    return(
        <>
            <Menu/>
            <div className="Month">
                <p className="WeekHeader">Monday</p>
                <p className="WeekHeader">Tuesday</p>
                <p className="WeekHeader">Wednesday</p>
                <p className="WeekHeader">Thursday</p>
                <p className="WeekHeader">Friday</p>
                <p className="WeekHeader">Saturday</p>
                <p className="WeekHeader">Sunday</p>
                {weeks}
            </div>
        </>

    )
}

export default MonthView;