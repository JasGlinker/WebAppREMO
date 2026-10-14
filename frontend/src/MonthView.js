import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity"

function MonthView(){
    const [acts, setActs] = useState([]);
    const [weeks, setWeeks] = useState({0:acts});
    useEffect(() => {
        fetch('/month', {method: "GET"})
            .then((res) => res.json())
            .then((el) => {
                //console.log(el);
                for (let week = 0; week < el.length; week++){
                    //console.log("week:", el[week])
                    for (let day = 0; day < el[week].length; day++){
                        //console.log("day:", el[week][day])
                        for (let act = 0; act < el[week][day].length; act++){
                            //console.log("act:", el[week][day][act])
                            setWeeks(values =>
                                ({...values,
                                    [week]: setActs(values =>
                                        ({...values, [day]: <Activity act={el[week][day][act]}/>}))}))

                        }
                    }
                }
                console.log("monthview:", weeks)
            })

    }, [weeks]);



    return(
        <div className="Month">
            <div className="Week">
                <div className="Day">
                    <p>Mo</p>

                </div>
            </div>

        </div>
    )
}

export default MonthView;