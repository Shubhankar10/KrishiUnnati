import React from "react";
import '../Static/css/plantID.css';
import Navbar from "./Navbar";
import UploadOverlay from "./UploadOverlay";
import { IoCloudUploadOutline } from "react-icons/io5";


const PlantID = () => {
    
    return (
      <div className="plantID">
            <Navbar />
            <div className="plant">
                <div className="plant-left">
                    <h1>Plant Identification</h1>
                    <p>
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam odit
                        perferendis corporis? sada sdad asd asd asd aLorem, ipsum dolor sit 
                        amet consectetur adipisicing elit. Quam odit perferendis corporis? 
                        sada sdad asd asd asd aLorem, ipsum dolor sit amet consectetur adi
                        pisicing elit. Quam odit perferendis corporis? sada sdad asd asd asd a
                    </p>
                </div>
                <div className="plant-right">
                    <div className="image-upload"></div>
                    <div className="upload-box" ><IoCloudUploadOutline size={'7em'} color={'darkgray'} background={'white'} /></div>
                    
                </div>
            </div>
            <UploadOverlay />
      </div>
    );
  };
  
  export default PlantID;