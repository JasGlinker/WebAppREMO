import {useState} from "react";
import {useNavigate} from "react-router-dom";
import "./App.css";



function Menu(){
    const [dropdown, setdropdown] = useState(false)
    function dropdownHandler() {
        setdropdown(!dropdown)
    }


    return(
        <div className="Banner">
            <div className="Dropdown">
                <button className='menu dropdown' onClick={dropdownHandler}>
                <i className="fa-solid fa-bars fa-2xl"></i>
                </button>
                <div className={dropdown ? 'menu-content' : 'menu-content hidden'}>
                    <a href="/">Day View</a>
                    <a href="/week">Week View</a>
                    <a href="/month">Month View</a>
                    <a href="/create">New</a>
                </div>
            </div>
            <p className="AppHeadline">REMO App</p>
        </div>



    )

}

export default Menu