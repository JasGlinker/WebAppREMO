import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity";



function DayView(){
    const [activities, setAct] = useState([])
    useEffect(() =>{
        fetch('/dayView', {method: "GET"})
        .then((res)=> res.json())
        .then((el)=>{
            //console.log(el)
            for (const a in el){
                console.log("Element from fetch:")
                console.log(el[a])
                setAct(values => [...values, <Activity act={el[a]}/>])
                //console.log(activities)
            }
        });

        },[]
    )


    //const activities = []
    //for(const act of tempActivities){
    //    activities.push(<Activity act={act}/>)
    //}
    console.log("temp Activities")
    console.log(activities)
    console.log(activities[0])
    return(
        <div>
            {activities}
        </div>

    );

}

export default DayView;