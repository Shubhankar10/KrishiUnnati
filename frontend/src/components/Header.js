import React from "react";
import logo from '../Static/Images/logo.png';
import '../Static/css/Header.css';
const Header = () => {
    const url = 'https://www.google.com/';
    return (
        <>
      <nav className="main-nav">
        <div className="logo">
            <img src={logo} alt="logo" />
        </div>

        <div className="menu-link">
            <ul>
                <li><a href={url}>Home</a></li>
                <li><a href={url}>Plant Identification</a></li>
                <li><a href={url}>Govt Scheme</a></li>
                <li><a href={url}>Map data</a></li>
            </ul>
        </div>
        <div className="login-signup">
            <ul>
                <li className="primary"><a href={url}>Login</a></li>
                <li className="secondary"><a href={url}>Signup</a></li>
            </ul>
        </div>
      </nav>
    </>
    );
}

export default Header;