import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity";
import Menu from "./menu";



function DayView(){
    const [activities, setAct] = useState([])
    useEffect(() =>{
        fetch('/dayView', {method: "GET"})
        .then((res)=> res.json())
        .then((el)=>{
            for (const a in el){
                setAct(values => [...values, <Activity act={el[a]} scope="day"/>])
            }
        });

        },[]
    )

    const weekstr = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    const todaydate = new Date()
    const todaystr = todaydate.toLocaleDateString()
    const todayday = weekstr[todaydate.getDay()]

    const body_dayview = new FormData()
    body_dayview.append('type', 'info')
    body_dayview.append('msg', 'frontend dayview build')
    fetch('/log', {method: 'POST', body: body_dayview})
        .catch(error => console.log(error))

    return(
        <>
            <Menu/>
            <div className="DayView">
                <p className='HeadlineDay'>{todayday + ' ' + todaystr}</p>
                {activities}
            </div>
        </>
    );

}

export default DayView;