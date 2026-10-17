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

    return(
        <div className="WeekActs">
            <div className="WeekHeader">
                <p>Monday</p>
                <p>Tuesday</p>
                <p>Wednesday</p>
                <p>Thursday</p>
                <p>Friday</p>
                <p>Saturday</p>
                <p>Sunday</p>
            </div>
            {week}
        </div>

    )
}

export default WeekView;