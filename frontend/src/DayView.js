import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity";



function DayView(){
    const [activities, setAct] = useState([])
    useEffect(() =>{
        fetch('/dayView', {method: "GET"})
        .then((res)=> res.json())
        .then((el)=>{
            for (const a in el){
                setAct(values => [...values, <Activity act={el[a]}/>])
            }
        });

        },[]
    )

    const body_dayview = new FormData()
    body_dayview.append('type', 'info')
    body_dayview.append('msg', 'frontend dayview build')
    fetch('/log', {method: 'POST', body: body_dayview})
        .catch(error => console.log(error))

    return(
        <div>
            {activities}
        </div>

    );

}

export default DayView;