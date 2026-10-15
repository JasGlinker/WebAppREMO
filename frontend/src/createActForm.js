import React, { useState, useEffect } from "react";
import {useNavigate} from "react-router-dom";
import "./App.css";

function CategorySelect({cat, change_handler}) {
    // plus new category option with different link (maybe later)
    const options = []
    // for each category listed add a select option
    for (const elem of cat){
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
        date: "",
        wdh: false
    });

    const [cat, setCat] = useState([]);
    useEffect(()=>{
        console.log("useEffect used")
        fetch("/data")
            .then((res) => res.json())
            .then((el) => {
                console.log("fetch response in use effect")
                for (const e in el){
                    console.log(el[e])
                    setCat(values => [...values, el[e]])
                }
                console.log(el);
                console.log("inside cat");

            });
    }, [])



    const change_handler = (e) => {
        const target = e.target;
        const value = target.type === 'checkbox' ? target.checked : target.value;
        const name = target.name;
        if (name.includes("days")){
            setdays(values => ({...values, [name.substring(5, 6)]: value}));
            console.log("days state", days);
        } else{
            setdata(values => ({...values, [name]: value}));
        }
        console.timeStamp();
        console.log(target, value, name);
        console.log(data);

    }

    const navigate = useNavigate()
    const submit_handler = (e) => {
        e.preventDefault();
        console.log(data);
        console.log("submit clicked");
        if (!data.name || !data.start_time){
            alert("new activity needs to have a name and time")
        }
        else{
            const formData = new FormData();
            for (const el in data){
                formData.append(el, data[el]);
            }
            for (const el in days){
                formData.append(el, days[el]);
            }
            console.log(formData)

            fetch("/create", {method: "POST", body: formData})
                .catch(error => {
                    alert("error submitting");
                    console.log(error);})
            navigate("/")
        }

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
          <input type="checkbox"
                 name="wdh"
                 value={data.wdh}
                 onChange={change_handler}
          />
          <div id = "DayChecks" className={data.wdh ? '':'hidden'}>
              <DaysCheck dayNbr={"0"} daystr={"Monday"} change_handler={change_handler} days={days}/>
              <DaysCheck dayNbr={"1"} daystr={"Tuesday"} change_handler={change_handler} days={days}/>
              <DaysCheck dayNbr={"2"} daystr={"Wednesday"} change_handler={change_handler} days={days}/>
              <DaysCheck dayNbr={"3"} daystr={"Thursday"} change_handler={change_handler} days={days}/>
              <DaysCheck dayNbr={"4"} daystr={"Friday"} change_handler={change_handler} days={days}/>
              <DaysCheck dayNbr={"5"} daystr={"Saturday"} change_handler={change_handler} days={days}/>
              <DaysCheck dayNbr={"6"} daystr={"Sunday"} change_handler={change_handler} days={days}/>
          </div>

          <input type="date"
                 name="date"
                 value={data.date}
                 onChange={change_handler}
                 className={data.wdh ? 'hidden':''}
          />
          <input type="range"
                 name="esc_steps"
                 value={data.esc_steps}
                 onChange={change_handler}
                 min="1"
                 max="5"
                 step="1"
          />
          <CategorySelect cat={cat} change_handler={change_handler}/>
          <button type="submit" onClick={submit_handler}> submit </button>
      </form>
    );
}



export default Form;