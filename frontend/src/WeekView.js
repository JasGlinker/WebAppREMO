import React, {useState, useEffect} from "react";
import "./App.css";
import Week from "./week";
import Menu from "./menu";

function WeekView(){
    const [week, setWeek] = useState();
    useEffect(() => {
        fetch('/weekView', {method: "GET"})
            .then((res) => res.json())
            .then((el)=> {
                setWeek(<Week week={el['acts']} scope="week" startday={el['date']}/>)
            });

    }, [])

    const body_Weekview = new FormData()
    body_Weekview.append('type', 'info')
    body_Weekview.append('msg', 'Frontend Weekview build')
    fetch('/log', {method: 'POST', body: body_Weekview})
        .catch(error => console.log(error))

    return(
        <>
            <Menu/>
            <div className="WeekActs">
                {week}
            </div>
        </>


    )
}

export default WeekView;