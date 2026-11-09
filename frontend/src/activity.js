import React, {useState, useEffect} from "react";
import "./App.css";


function Activity({act, scope}){

    let category = ''
    const name = act['act_name']
    const time = act['start_time']
    if (act['category'] === 1){
        category = 'work'
    } else if(act['category'] === 2){
        category = 'uni'
    } else if(act['category'] === 3){
        category = 'lifestyle'
    }

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

    if (scope === "day"){
        return(
            <div className={"dayAct " + category}>
                <button className="actbtn" onClick={handleDone}></button>
                <p className={done ? 'crossed time':'time'}>{time}</p>
                <p className={done ? 'crossed name':'name'}>{name}</p>
            </div>
        )
    } else if(scope === "week"){
        return(
            <div className={"weekDayAct " + category}>
                <button className="actbtn" onClick={handleDone}></button>
                <p className={done ? 'crossed time':'time'}>{time}</p>
                <p className={done ? 'crossed name':'name'}>{name}</p>
            </div>
        )
    } else if(scope === "month"){
        return(
            <div className={"monthWeekDayAct " + category}>
                <p className={done ? 'crossed name':'name'}>{name}</p>
            </div>
        )
    }
}

export default Activity