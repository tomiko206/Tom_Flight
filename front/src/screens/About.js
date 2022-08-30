import React from 'react'
import './About.css'
import { selectLog } from "../app/loggedSlice";
import { useSelector } from 'react-redux';
import { selectSuperUser, selectStaff } from "../app/userSlice";
import { ContactUs } from '../components/ContactUs ';

const About = () => {
    const log = useSelector(selectLog);
    const staff = useSelector(selectStaff);
    const superUser = useSelector(selectSuperUser);
    

    return (
        <div>
            <h1> Hello everyone !!</h1>
            <br ></br>
            <p>
                my name is Tom Eliyahu and I 28 years old. <br />
                I am a Junior Full stack developer . I am studying at John bryce College Full Stack python Course. <br />
                In this project i present a flight management system. <br />
            </p>
            <br ></br>
            
            {log === true && staff === false && superUser === false &&
                <p className='contact'>
                    want to become airline company?<br />
                </p>}
            <p className='contact'>Contact </p>
            <ContactUs />
        </div>
    )
}

export default About
