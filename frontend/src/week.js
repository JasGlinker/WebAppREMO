import React, {useState, useEffect} from "react";
import "./App.css";
import Activity from "./activity"

function Week({week, scope, startday}){
    console.log("WEEK", week)
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
            weekacts[weekdays[i]].push(<Activity act={week[i][act]} scope={scope}/>)
        }
    }

    const dateweek = new Date(startday)
    console.log('dateweek startday', dateweek)
    const thismonth = new Date().getMonth()
    console.log('thismonth', thismonth)
    const tueDate = new Date()
    tueDate.setDate(dateweek.getDate() + 1)
    const wedDate = new Date()
    wedDate.setDate(dateweek.getDate() + 2)
    const thuDate = new Date()
    thuDate.setDate(dateweek.getDate() + 3)
    const friDate = new Date()
    friDate.setDate(dateweek.getDate() + 4)
    const satDate = new Date()
    satDate.setDate(dateweek.getDate() + 5)
    const sunDate = new Date()
    sunDate.setDate(dateweek.getDate() + 6)

    const body_startday = new FormData()
    body_startday.append('type', 'debug')
    body_startday.append('msg', 'frontend startday week:' + startday)
    fetch('/log', {method: 'POST', body: body_startday})
        .catch(error => console.log(error))

    const body_week = new FormData()
    body_week.append('type', 'info')
    body_week.append('msg', 'frontend week build')
    fetch('/log', {method: 'POST', body: body_week})
        .catch(error => console.log(error))

    if (scope === "month"){
        return(
            <>
                <div className="DayActs Mon">
                    <p className={dateweek.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {dateweek.getDate()}
                    </p>
                    {weekacts["mon"]}
                </div>
                <div className="DayActs Tue">
                    <p className={tueDate.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {tueDate.getDate()}
                    </p>
                    {weekacts["tue"]}
                </div>
                <div className="DayActs Wed">
                    <p className={wedDate.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {wedDate.getDate()}
                    </p>
                    {weekacts["wed"]}
                </div>
                <div className="DayActs Thu">
                    <p className={thuDate.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {thuDate.getDate()}
                    </p>
                    {weekacts["thu"]}
                </div>
                <div className="DayActs Fri">
                    <p className={friDate.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {friDate.getDate()}
                    </p>
                    {weekacts["fri"]}
                </div>
                <div className="DayActs Sat">
                    <p className={satDate.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {satDate.getDate()}
                    </p>
                    {weekacts["sat"]}
                </div>
                <div className="DayActs Sun">
                    <p className={sunDate.getMonth() === thismonth ? 'daynmbr currentMonth': 'daynmbr differentMonth'}>
                        {sunDate.getDate()}
                    </p>
                    {weekacts["sun"]}
                </div>
            </>
        )
    } else{
        return(
            <>
                <p className="WeekHeader">{'Mon ' + dateweek.toLocaleDateString()}</p>
                <div className="DayActs Mon">
                    {weekacts["mon"]}
                </div>
                <p className="WeekHeader">{'Tue ' + tueDate.toLocaleDateString()}</p>
                <div className="DayActs Tue">
                    {weekacts["tue"]}
                </div>
                <p className="WeekHeader">{'Wed ' + wedDate.toLocaleDateString()}</p>
                <div className="DayActs Wed">
                    {weekacts["wed"]}
                </div>
                <p className="WeekHeader">{'Thu ' + thuDate.toLocaleDateString()}</p>
                <div className="DayActs Thu">
                    {weekacts["thu"]}
                </div>
                <p className="WeekHeader">{'Fri ' + friDate.toLocaleDateString()}</p>
                <div className="DayActs Fri">
                    {weekacts["fri"]}
                </div>
                <p className="WeekHeader">{'Sat ' + satDate.toLocaleDateString()}</p>
                <div className="DayActs Sat">
                    {weekacts["sat"]}
                </div>
                <p className="WeekHeader">{'Sun ' + sunDate.toLocaleDateString()}</p>
                <div className="DayActs Sun">
                    {weekacts["sun"]}
                </div>
            </>
        )
    }


}

export default Week;