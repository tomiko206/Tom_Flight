import React, { useEffect} from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  selectFlight,
  deleteFlightAsync,
  getFlightAsync,
} from "../app/flightSlice";
import '../App.css'
import Table from 'react-bootstrap/Table';

const Flight = () => {
  const myFlight = useSelector(selectFlight);
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getFlightAsync());
  }, []);

  return (
    <div>
      <br /><br /><br /><br />
      <br />We have {myFlight.length} Flight in my site
      <br /> <br />

      <Table striped bordered hover variant="dark">
        <thead>
          <tr>
            <th>ID</th>
            <th>AirLine</th>
            <th>origin countrie</th>
            <th>destination countrie</th>
            <th>departure time</th>
            <th>landing time</th>
            <th>remaining tickets</th>
            <th>Status</th>
            <th>price</th>
            <th> </th>
          </tr>
        </thead>
        {myFlight.length >0 && myFlight
          // .filter((x) =>
          // x.origin_countrie.includes(search))
          .map((flight, i) => (
            <tbody key={i}>
              <tr>
                <td>{flight.id}</td>
                <td>{flight.Airline_Companie.Name} </td>
                <td>{flight.Origin_Countrie.Name}</td>
                <td>{flight.Destination_Countrie.Name}</td>
                <td>{flight.Departure_Time.split("").filter((s, i) => i <= 15)}</td>
                <td>{flight.Landing_Time.split("").filter((s, i) => i <= 15)}</td>
                <td>{flight.Remaining_Tickets}</td>
                <td>{flight.status ? "available" : "unavailable"}</td>
                <td>{flight.Price}$</td>
                <td>
                  <button onClick={() => dispatch(deleteFlightAsync({ id: flight.id }))} >
                    Delete</button>
                </td>
              </tr>
            </tbody>
          ))}
      </Table>
    </div>
  );
};

export default Flight;