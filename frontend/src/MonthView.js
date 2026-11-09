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
                //console.log(el);
                for (let week = 0; week < el.length; week++){
                    //console.log("week:", el[week])
//
                    setWeeks(values => [...values, <Week week={el[week]['acts']} scope={"month"} startday={el[week]['date']}/>])
                }
            })

    }, []);

    const body_Monthview = new FormData()
    body_Monthview.append('type', 'info')
    body_Monthview.append('msg', 'Frontend Monthview build')
    fetch('/log', {method: 'POST', body: body_Monthview})
        .catch(error => console.log(error))

    const MonthStrings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December']
    const Month = MonthStrings[new Date().getMonth()]

    return(
        <>
            <Menu/>
            <p className="HeadlineMonth">{Month}</p>
            <div className="Month">
                <p className="WeekHeader">Mon</p>
                <p className="WeekHeader">Tue</p>
                <p className="WeekHeader">Wed</p>
                <p className="WeekHeader">Thu</p>
                <p className="WeekHeader">Fri</p>
                <p className="WeekHeader">Sat</p>
                <p className="WeekHeader">Sun</p>
                {weeks}
            </div>
        </>

    )
}

export default MonthView;