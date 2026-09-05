import React, { useState, useEffect } from "react";

function CategorySelect({change_handler}) {
    // Get category list from backend
    // for each category listed add a select option
    // plus new category option with different link (maybe later)
    const ex = ["Work", "University", "Lifestyle"];
    const options = []
    for (const elem of ex){
        options.push(<option value={elem}>{elem}</option>)
    }
    return (
        <select name="category" onChange={change_handler}>
            {options}
        </select>
    );
}

function DaysCheck({dayNbr, daystr, change_handler, days}){
    const name = "days["+ dayNbr +"]"
    return(
        <label>
              <input type="checkbox"
                 name={name}
                 checked={days.dayNbr}
                 onChange={change_handler}
              /> {daystr}
          </label>
    );
}




function Form(){
    const [days, setdays] = useState({0: false, 1:false, 2: false, 3:false, 4:false, 5:false, 6:false})
    const [data, setdata] = useState({
        name: "",
        start_time: 0,
        esc_steps: 0,
        category: "",
    });

    const change_handler = (e) => {
        console.timeStamp()
        const target = e.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;
        if (name.includes("days")){
            setdays(values => ({...values, [name.substring(5, 6)]: value}));
            console.log("days state", days);
        } else{
            setdata(values => ({...values, [name]: value}));
        }
        console.log(target, value, name);
        console.log(data)

    }
    function submit_handler(data){

    }

    return(
       <form onSubmit={submit_handler}>
          <input type="text"
                 name="name"
                 placeholder="Name"
                 value={data.name}
                 onChange={change_handler}
          />
          <input type="time"
                 name="start_time"
                 placeholder="09:00"
                 value={data.start_time}
                 onChange={change_handler}
          />
          <DaysCheck dayNbr={"0"} daystr={"Monday"} change_handler={change_handler} days={days}/>
          <DaysCheck dayNbr={"1"} daystr={"Tuesday"} change_handler={change_handler} days={days}/>
          <DaysCheck dayNbr={"2"} daystr={"Wednesday"} change_handler={change_handler} days={days}/>
          <DaysCheck dayNbr={"3"} daystr={"Thursday"} change_handler={change_handler} days={days}/>
          <DaysCheck dayNbr={"4"} daystr={"Friday"} change_handler={change_handler} days={days}/>
          <DaysCheck dayNbr={"5"} daystr={"Saturday"} change_handler={change_handler} days={days}/>
          <DaysCheck dayNbr={"6"} daystr={"Sunday"} change_handler={change_handler} days={days}/>

          <input type="range"
                 name="esc_steps"
                 value={data.esc_steps}
                 onChange={change_handler}
                 min="1"
                 max="5"
                 step="1"
          />
          <CategorySelect change_handler={change_handler}/>
          <button type="submit"> submit </button>
      </form>
    );
}



export default Form;