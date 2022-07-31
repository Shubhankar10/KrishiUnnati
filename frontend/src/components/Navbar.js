import React from "react";
import '../Static/css/navbar.css';
import logo from '../Static/Images/logo.png';
import { GiHamburgerMenu } from "react-icons/gi";

const Navbar = () => {
    const url = 'https://www.google.com/';
    return (
    <> 
      <nav className="nav">
        <div className="sidebar">
          <button><GiHamburgerMenu size={'3em'} /></button>
        </div>
        <div className="imglogo">
            <img src={logo} alt="logo" />
        </div>
        <div className="user-icon">
           <a href=""></a>
        </div>
        
      </nav>
    </>
    );
}

export default Navbar;
