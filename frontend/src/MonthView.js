import React, {useState, useEffect} from "react";
import "./App.css";

import Week from "./week";

function MonthView(){
    const [weeks, setWeeks] = useState([]);
    useEffect(() => {
        fetch('/month', {method: "GET"})
            .then((res) => res.json())
            .then((el) => {
                console.log(el);
                //const comp = el.map(week => {
                //    console.log(week);
                //    return (<Week week={week}/>)
                //})
                for (let week = 0; week < el.length; week++){
                    console.log("week:", el[week])
//
                    setWeeks(values => [...values, <Week week={el[week]}/>])
                }
                //setWeeks(el)
                //console.log("monthview:", weeks)
            })

    }, []);


    //const [compWeeks, setCompWeeks] = useState([])
    //const tempweeks = weeks.map(week => <Week week={week}/>)
    //setWeeks(tempweeks)
    //console.log("Outside: ", weeks)
    return(
        <div className="Month">
            {weeks}
        </div>
    )
}

export default MonthView;