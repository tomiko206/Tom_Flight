import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  selectTickets,
    // addTicketsAsync,
  deleteTicketsAsync,
  getTicketsAsync,
} from "../app/ticketsSlice";
import '../App.css'
import Table from 'react-bootstrap/Table';

const Tickets = () => {
  const myTickets = useSelector(selectTickets);
  const dispatch = useDispatch();
  const [search, setSearch] = useState("");
  useEffect(() => {
    dispatch(getTicketsAsync());
  }, []);

  return (
    <div>
      <br /><br /><br /><br />
      Search by name: <input onChange={(e) => setSearch(e.target.value)} />
      <br /><br />We have {myTickets.length} customers that have Tickets in my site
      <br /><br /><br /><br />
      <Table striped bordered hover variant="dark">
      <thead>
        <tr>
          <th>ID</th>
          {/* <th>Customer Name</th> */}
          <th>AirLine</th>
          <th>Origin Countrie</th>
          <th>Destination Countrie</th>
          <th>Departure Time</th>
          <th>Landing Time</th>
          <th>Tickets</th>
          <th></th>
          
        </tr>
      </thead>
      {myTickets.length >0 && myTickets
      // .filter((x) =>
      // x.user.username.includes(search))
      .map((tickets,i) => (
      <tbody key={i}>
        <tr>
          <td>{tickets.id}</td>
          {/* <td>{tickets.user.username}</td> */}
          <td>{tickets.Flight.Airline_Companie.Name}</td>
          <td>{tickets.Flight.Origin_Countrie.Name}</td>
          <td>{tickets.Flight.Destination_Countrie.Name}</td>
          <td>{tickets.Flight.Departure_Time.split("").filter((s, i) => i <= 15)}</td>
          <td>{tickets.Flight.Landing_Time.split("").filter((s, i) => i <= 15)}</td>
          <td>{tickets.number_of_tickets}</td>


          <td>
          <button onClick={() => dispatch(deleteTicketsAsync({ id: tickets.id }))} >
              Delete</button>
          </td>
        </tr>
      </tbody>
      ))}
    </Table>
    </div>
  );
};

export default Tickets;