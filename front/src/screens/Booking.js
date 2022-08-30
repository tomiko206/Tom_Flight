import React, { useState } from 'react'
import { useDispatch, useSelector } from "react-redux";
import { selectYourFlight } from "../app/flightSlice";
import Table from 'react-bootstrap/Table';
import { selectUserName } from "../app/userSlice";
import { addCustomersAsync } from "../app/customersSlice";
// import { addTicketsAsync } from "../app/ticketsSlice";
import jwt_decode from "jwt-decode";
import { Link } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import { saveNewTickets } from '../app/ticketsSlice';

const Booking = () => {
  const dispatch = useDispatch();
  const yourFlight = useSelector(selectYourFlight);
  const userName = useSelector(selectUserName);
  // const myCustomers = useSelector(selectCustomers);

  const [First_Name, setFirst_name] = useState("")
  const [Last_Name, setLast_name] = useState("")
  const [Address, setAddress] = useState("")
  const [Phone_No, setPhone_No] = useState("")
  const [Tickets, setTickets] = useState(0)
  // const [success, setSucsess] = useState(false)
  // const [customer, setCustomer] = useState("")
  const addCustomer = (First_Name, Last_Name, Address, Phone_No, Tickets) => {
    let access = localStorage.getItem("access");
    let user = jwt_decode(access).user_id;
    const newCustomer = {
      First_Name: First_Name,
      Last_Name: Last_Name,
      Address: Address,
      Phone_No: Phone_No,
      user: jwt_decode(access).user_id
    }
    dispatch(addCustomersAsync(newCustomer))
    let newTickets = {
      flight_id: yourFlight.id,
      number_of_tickets: Tickets,
      user: user
    }
    dispatch(saveNewTickets(newTickets))
  }

  // const addTickets = () => {
  //   let access = localStorage.getItem("access");
  //   let user = jwt_decode(access).user_id;
  //   console.log(myCustomers)
  //   let  customer_id=myCustomers.length > 0 && myCustomers
  //   .filter((x)=> x.user.id === user)
  //   .map(custo=>custo.id)
  //   console.log(customer_id)
  //   const newTickets = {
  //   customer_id: customer_id[0],
  //   flight_id: yourFlight.id,
  //   number_of_tickets: tickets,
  //   user: user
  // }
  // useEffect(() => {
  //   dispatch(getCustomersAsync());
  // }, []);

  return (
    <div>
      <br /><br />
      <h3>Hey {userName} Just a few more details to complete buying tickets</h3>
      <Table striped bordered hover variant="dark">
        <thead>
          <tr>
            <th>AirLine</th>
            <th>origin countrie</th>
            <th>destination countrie</th>
            <th>departure time</th>
            <th>landing time</th>
            <th>remaining tickets</th>
            <th>price</th>
          </tr>
        </thead>
        <tbody >
          <tr>
            <td>{yourFlight.Airline_Companie} </td>
            <td>{yourFlight.Origin_Countrie}</td>
            <td>{yourFlight.Destination_Countrie}</td>
            <td>{yourFlight.Departure_Time}</td>
            <td>{yourFlight.Landing_Time}</td>
            <td>{yourFlight.Remaining_Tickets}</td>
            <td>{yourFlight.Price}</td>
          </tr>
        </tbody>
      </Table>
      <br /><br />
      <h3>Personal Information</h3>
      {/* {success === true && (myCustomers.length > 0 && myCustomers
        .filter((x) =>
          x.user.id === userID)
        .map((customer, i) => (
          <div key={i}>
            First Name:  <input onChange={(e) => setFirst_name(e.target.value)} value={customer.first_name}></input> <br />
            Last Name:&nbsp;<input onChange={(e) => setLast_name(e.target.value)} value={customer.last_name}></input> <br />
            Address:    &nbsp;&nbsp;&nbsp; <input onChange={(e) => setAddress(e.target.value)} value={customer.address}></input> <br />
            Phone: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input onChange={(e) => setPhone_No(e.target.value)} value={customer.phone_No}></input> <br />
            Credit card: <input onChange={(e) => setCredit_card_No(e.target.value)} value={customer.credit_card_No}></input> <br />
            <button onClick={() => addCustomer(first_name, last_name, address, phone_No, credit_card_No)}>Submit</button>
          </div>
        )))} */}

      <div>
        First Name:  <input onChange={(e) => setFirst_name(e.target.value)}></input> <br />
        Last Name:&nbsp;<input onChange={(e) => setLast_name(e.target.value)}></input> <br />
        Address:    &nbsp;&nbsp;&nbsp; <input onChange={(e) => setAddress(e.target.value)}></input> <br />
        Phone:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
          required onChange={(e) => setPhone_No(e.target.value)}></input> <br />
        Number of passengers: <input type="number" min={1} max={5} onChange={(e) => setTickets(e.target.value)}></input> <br />
        <Button variant="primary" onClick={() =>
          addCustomer(First_Name, Last_Name, Address, Phone_No, Tickets)}
        >
          <Link to="/payment">Submit</Link>
        </Button>
      </div>
      <br /><br />
    </div>
  )
}

export default Booking