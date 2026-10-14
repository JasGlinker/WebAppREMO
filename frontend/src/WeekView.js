import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity"

function WeekView(){
    const [weekacts, setActs] = useState({
        mon: [],
        tue: [],
        wed: [],
        thu: [],
        fri: [],
        sat: [],
        sun: []
    })

    useEffect(() => {
        fetch('/weekView', {method: "GET"})
            .then((res) => res.json())
            .then((el)=> {
                const weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
                for (let i = 0; i < 7; i++){
                    for (const e in el[i]){
                        console.log(e)
                        setActs(values => ({...values, [weekdays[i]]: <Activity act={el[i][e]} />}))
                    }
                }
            });

    }, [])

    return(
        <div>
            <div>
                <p>Monday</p>
                {weekacts["mon"]}
            </div>
            <div>
                <p>Tuesday</p>
                {weekacts["tue"]}
            </div>
            <div>
                <p>Wednesday</p>
                {weekacts["wed"]}
            </div>
            <div>
                <p>Thursday</p>
                {weekacts["thu"]}
            </div>
            <div>
                <p>Friday</p>
                {weekacts["fri"]}
            </div>
            <div>
                <p>Saturday</p>
                {weekacts["sat"]}
            </div>
            <div>
                <p>Sunday</p>
                {weekacts["sun"]}
            </div>
        </div>
    )
}

export default WeekView;