import React, { useState, useEffect } from 'react'
import { get_selected_flightAsync, selectedFlight, saveSelectedFlight } from "../app/flightSlice";
import { useSelector, useDispatch } from "react-redux";
import Table from 'react-bootstrap/Table';
import { Link } from "react-router-dom";
import { selectLog } from "../app/loggedSlice";

const MyFlight = () => {
    const dispatch = useDispatch();
    const myFlight = useSelector(selectedFlight);
    const [search, setSearch] = useState("");
    const log = useSelector(selectLog);

    useEffect(() => {
        dispatch(get_selected_flightAsync())
    }, [])

    const saveFlight = (flight) => {
        let yourFlight = {
            id:flight.id,
            Airline_Companie_Name:flight.Airline_Companie.Name,
            Origin_Countrie:flight.Origin_Countrie.Name,
            Destination_Countrie:flight.Destination_Countrie.Name,
            Departure_Time:flight.Departure_Time,
            Landing_Time:flight.Landing_Time,
            Remaining_Tickets:flight.Remaining_Tickets,
            Price:flight.Price
          }
        dispatch(saveSelectedFlight(yourFlight))
    }

    return (
        <div>
            <br /><br />
            {log === false && <h4 style={{ textAlign: "center" }}> you must Login to booking a flight </h4>}
            <br /><br />
            Search by AirLine Companie: <input onChange={(e) => setSearch(e.target.value)} />
            <br />We have {myFlight.length} flight as you requested
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
                        <th>price</th>
                        <th>  </th>
                    </tr>
                </thead>
                {myFlight
                    .filter((x) =>
                        x.Airline_Companie.Name.includes(search))
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
                                <td>{flight.Price}$</td>
                                <td>
                                {!log ? (
                                    <button onClick={() =>saveFlight(flight)}>
                                        <Link to="/Login">Booking</Link>
                                    </button>
                                ) : (
                                    <button onClick={() =>saveFlight(flight)}>
                                        <Link to={"/booking"}>Booking</Link>
                                    </button>
                                )}
                                </td>
                            </tr>
                        </tbody>
                    ))}
            </Table>
            <br/><br/><br/><br/>
        </div>
    )
}

export default MyFlight