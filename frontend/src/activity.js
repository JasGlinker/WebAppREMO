import React, {useState, useEffect} from "react";
import "./App.css";


function Activity({act}){

    const name = act['act_name']
    const time = act['start_time']
    const [done, setDone] = useState(false)
    function handleDone(){
        setDone(!done)
        if (done){
            const body = new FormData()
            body.append('type', 'info')
            body.append('act', JSON.stringify(act))
            body.append('msg', 'act ' + act['act_id'] + ' marked done')
            fetch('/log', {method: 'POST', body: body})
                .catch(error => {
                    console.log(error)
            })
        }
    }
    const body_act = new FormData()
    body_act.append('type', 'info')
    body_act.append('msg', 'frontend act initiated')
    fetch('/log', {method: 'POST', body: body_act})
        .catch(error => console.log(error))

    return(
        <div>
            <button onClick={handleDone}></button>
            <p className={done ? 'crossed':''}>{name}</p>
            <p className={done ? 'crossed':''}>{time}</p>
        </div>
    )
}

export default Activity