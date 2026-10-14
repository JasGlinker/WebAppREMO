import React, {useState, useEffect} from "react";
import "./App.css";


function Activity({act}){
    //console.log("Act in activity:")
    //console.log(act)

    const name = act['act_name']
    const time = act['start_time']
    const [done, setDone] = useState(false)
    function handleDone(){
        setDone(!done)
    }
    //console.log(name)
    return(
        <div>
            <button onClick={handleDone}></button>
            <p className={done ? 'crossed':''}>{name}</p>
            <p className={done ? 'crossed':''}>{time}</p>
        </div>
    )
}

export default Activity