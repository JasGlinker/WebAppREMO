import React, { useState, useEffect } from "react";

function CategorySelect() {
    // Get category list from backend
    // for each category listed add a select option
    // plus new category option with different link (maybe later)
    const ex = ["Work", "University", "Lifestyle"];
    const options = []
    for (const elem of ex){
        options.push(<option value={elem}>{elem}</option>)
    }
    return (
        <select name="category">
            {options}
        </select>
    );
}

function DaysCheck({dayNbr, daystr, change_handler, data}){
    const name = "days["+ dayNbr +"]"
    return(
        <label>
              <input type="checkbox"
                 name={name}
                 checked={data.days[dayNbr]}
                 onChange={change_handler}
              /> {daystr}
          </label>
    );
}

function Form(){
    const [data, setdata] = useState({
        name: "",
        start_time: 0,
        days: {0: false, 1:false, 2:false, 3:false, 4:false, 5:false, 6:false},
        esc_steps: 0,
        category: "",
    });

    const change_handler = (e) => {
        console.timeStamp()
        const target = e.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;
        setdata(values => ({...values, [name]: {
            switch(name) {
                case "days[0]":
                    {}
                    break;
                case
                    "days[1]"
                :
                    data.days[1] = value;
                    break;
                case
                    "days[2]"
                :
                    data.days[2] = value;
                    break;
                case
                    "days[3]"
                :
                    data.days[3] = value;
                    break;
                case
                    "days[4]"
                :
                    data.days[4] = value;
                    break;
                case
                    "days[5]"
                :
                    data.days[5] = value;
                    break;
                case
                    "days[6]"
                :
                    const day = 6;

                    //data.days[6] = value;
                    break;
                default:
                    value
                }
                break;
            }));
        }
        console.log(target, value, name);
        console.log(data)
        console.log(data.days);

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
          <DaysCheck dayNbr={"0"} daystr={"Monday"} change_handler={change_handler} data={data}/>
          <DaysCheck dayNbr={"1"} daystr={"Tuesday"} change_handler={change_handler} data={data}/>
          <DaysCheck dayNbr={"2"} daystr={"Wednesday"} change_handler={change_handler} data={data}/>
          <DaysCheck dayNbr={"3"} daystr={"Thursday"} change_handler={change_handler} data={data}/>
          <DaysCheck dayNbr={"4"} daystr={"Friday"} change_handler={change_handler} data={data}/>
          <DaysCheck dayNbr={"5"} daystr={"Saturday"} change_handler={change_handler} data={data}/>
          <DaysCheck dayNbr={"6"} daystr={"Sunday"} change_handler={change_handler} data={data}/>

          <input type="range"
                 name="esc_steps"
                 value={data.esc_steps}
                 onChange={change_handler}
                 min="1"
                 max="5"
                 step="1"
          />
          <CategorySelect/>
      </form>
    );
}



export default Form;