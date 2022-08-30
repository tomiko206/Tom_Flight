import React from 'react';
import '../App.css';
import './HeroSection.css';

const HeroSection = () => {
  return (
    <div className='hero-container'>
      <img src='/static/elal.jpg' alt='air_plane' style={{height:"103%"}}></img>
      <br></br>
      <br></br>
      <h1>Tom's Flight</h1>
      <h1>Come Fly With Us</h1>
    </div>
  );
}

export default HeroSection;
