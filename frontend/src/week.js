import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity"

function Week({week}){
    console.log("WEEK", week)
    //const [weekacts, setActs] = useState({
    //    mon: [],
    //    tue: [],
    //    wed: [],
    //    thu: [],
    //    fri: [],
    //    sat: [],
    //    sun: []
    //})
    const weekacts = {
        mon: [],
        tue: [],
        wed: [],
        thu: [],
        fri: [],
        sat: [],
        sun: []
    }
    const weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    for (let i = 0; i < 7; i++){
        for (const act in week[i]){
            console.log("WEEK ACT IN FOR", week[i][act])
            //setActs(values => ({...values, [weekdays[i]]: <Activity act={act}/>}))
            weekacts[weekdays[i]].push(<Activity act={week[i][act]}/>)
        }
    }
    console.log("WEEK ACTS:", weekacts)
    console.log("WEEK ACTS TUE:", weekacts["tue"])
    return(
        <>
            <div className="DayActs Mon">
                {weekacts["mon"]}
            </div>
            <div className="DayActs Tue">
                {weekacts["tue"]}
            </div>
            <div className="DayActs Wed">
                {weekacts["wed"]}
            </div>
            <div className="DayActs Thu">
                {weekacts["thu"]}
            </div>
            <div className="DayActs Fri">
                {weekacts["fri"]}
            </div>
            <div className="DayActs Sat">
                {weekacts["sat"]}
            </div>
            <div className="DayActs Sun">
                {weekacts["sun"]}
            </div>
        </>
    )
}

export default Week;