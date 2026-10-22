import React, {useState, useEffect} from "react";
import "./App.css";
import Week from "./week";

function WeekView(){
    const [week, setWeek] = useState();
    useEffect(() => {
        fetch('/weekView', {method: "GET"})
            .then((res) => res.json())
            .then((el)=> {
                setWeek(<Week week={el}/>)
            });

    }, [])

    const body_Weekview = new FormData()
    body_Weekview.append('type', 'info')
    body_Weekview.append('msg', 'Frontend Weekview build')
    fetch('/log', {method: 'POST', body: body_Weekview})
        .catch(error => console.log(error))

    return(
        <div className="WeekActs">
            <p className="WeekHeader">Monday</p>
            <p className="WeekHeader">Tuesday</p>
            <p className="WeekHeader">Wednesday</p>
            <p className="WeekHeader">Thursday</p>
            <p className="WeekHeader">Friday</p>
            <p className="WeekHeader">Saturday</p>
            <p className="WeekHeader">Sunday</p>
            {week}
        </div>

    )
}

export default WeekView;