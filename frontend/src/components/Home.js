import React from "react";
import "..//Static/css/Map.css";
import map from "../Static/Images/map.png";
import "..//Static/css/Home.css";
import "..//Static/css/Plant.css"
import "..//Static/css/other.css";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const url = "https://www.youtube.com/embed/dQw4w9WgXcQ";
  let navigate= useNavigate();
  
  return (
    <>
      <div className="main-home">
        <div className="text-container">
          <h1>Krishi Unnati</h1>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore
            unde eum magnam commodi sequi explicabo libero temporibus nam vitae.
          </p>
          <div className="home-button">
            <div className="button1">
              <a href={url}>button1</a>
            </div>
            <div className="button2">
              <a href={url}>button2</a>
            </div>
          </div>
        </div>
        <div className="side container">
          <div className="ellipse">
            <div className="square">Chat with us</div>
            <div className="square2">
              Voice <br />
              Navigation
            </div>
          </div>
        </div>
      </div>

      {/* Plant Identification */}
      <div className="main-container-plant">
        <div className="left-container">
          <div className="square-plant"></div>
        </div>
        <div className="right-container">
          <h2> Plant Identification</h2>
          <p>
            lorem ipsum dolor sit amet consectetur adipisicing elit.
          </p>
            <div>
              <button id="plant-button" onClick={() => {
                navigate("/PlantID");
              }}>button1</button>
            </div>
        </div>
      </div>

      {/* Map */}
      <div className="map-main">
      <div className="main-container-map">
        <div className="map-text-container">
          <h1>Agricultural Map of India</h1>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Veniam
            exercitationem, incidunt inventore error pariatur necessitatibu
          </p>
        </div>
        <div className="map-container">
            <img src={map} alt="map" className="map-image"/>
        </div>
      </div>
    </div>

    {/* Other Section */}
      {/* database figure */}
      <div className="others">
          <div className="database-fig">
              <div className="database-fig-left">
                  <h1>Database Fig</h1>
                  <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam odit
                      perferendis corporis? sada sdad asd asd asd a
                  </p>
              </div>
              <div className="database-fig-right">
                  <div className="others-square"></div>
              </div>
          </div>
          {/* Weather/Crop Prediction */}
          <div className="weather-fig">
              <div className="weather-fig-left">
                  <div className="others-square"></div>
              </div>
              <div className="weather-fig-right">
                  <h1>Weather/Crop Prediction</h1>
                  <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam odit
                      perferendis corporis? sada sdad asd asd asd a
                  </p>
              </div>
          </div>

          {/* Govt Schemes */}
          <div className="govt-fig">
              <div className="govt-fig-left">
                  <h1>Govt Scheme</h1>
                  <p>
                      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam odit
                      perferendis corporis? sada sdad asd asd asd a
                  </p>
              </div>
              <div className="govt-fig-right">
                  <div className="others-square"></div>
              </div>
          </div>
      </div>


      
    </>
  );
};

export default Home;
