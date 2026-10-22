import {useState} from "react";
import {useNavigate} from "react-router-dom";




function Menu(){
    const navigate = useNavigate()
    const [dropdown, setdropdown] = useState(false)
    function dropdownHandler() {
        setdropdown(!dropdown)
    }

    function linkhandler(e){
        const target = e.target
        console.log('element name', target.name)
        navigate(target.name)
    }

    return(
        <div>
            <button className='menu dropdown' onClick={dropdownHandler}>
            ---
            </button>
            <ul className={dropdown ? '' : 'hidden'}>
                <li>
                    <button name='/' onClick={linkhandler}>Day View</button>
                </li>
                <li>
                    <button name='/week' onClick={linkhandler}>Week View</button>
                </li>
                <li>
                    <button name='/month' onClick={linkhandler}>Month View</button>
                </li>
                <li>
                    <button name='/create' onClick={linkhandler}>New</button>
                </li>
            </ul>
        </div>


    )

}

export default Menu