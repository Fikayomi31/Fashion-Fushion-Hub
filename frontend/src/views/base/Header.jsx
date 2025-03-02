import React from "react";
import { useAuthStore } from "../../store/auth";
import FFH_logo from '../../assets/header/FFH_logo.webp'
import { Link } from "react-router-dom";



function Header() {
    const isLoggedIn = useAuthStore((state) => state.isLoggedIn);
    const user = useAuthStore((state) => state.user);

    

    return (
        <div>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container">
                    <a className=" navbar-brand" href="#">
                        <img style={{ width: 40, height: 40, borderRadius: 50 }} src={FFH_logo} alt="" />
                    </a>
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle='collapse'
                        data-bs-target='#navbarSupportedContent'
                        aria-controls="navbaSupportedContent"
                        aria-expanded='false'
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon" />
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle"
                                    href="#"
                                    id='navbarDropdown'
                                    role="button"
                                    data-bs-toggle='dropdown'
                                    aria-expanded='false'
                                >
                                    Page
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li><a className="dropdown-item" href="#">About Us</a></li>
                                    <li><a className="dropdown-item" href="#">Contact Us</a></li>
                                    <li><a className="dropdown-item" href="#">Blog </a></li>
                                    <li><a className="dropdown-item" href="#">Changelog</a></li>
                                    <li><a className="dropdown-item" href="#">Terms & Condition</a></li>
                                    <li><a className="dropdown-item" href="#">Cookie Policy</a></li>
                                </ul>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" >
                                    Account
                                </a>
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <li><a className="dropdown-item" href="#">Profile</a> </li>
                                    <li><a className="dropdown-item" href="#">Orders</a> </li>
                                    <li><a className="dropdown-item" href="#">Address</a> </li>
                                    <li><a className="dropdown-item" href="#">Wishlist</a> </li>
                                    <li><a className="dropdown-item" href="#">Message</a> </li>
                                    <li><a className="dropdown-item" href="#">Notification</a> </li>
                                    <li><a className="dropdown-item" href="#">Settings</a> </li>
                                </ul>
                            </li>
                        </ul>
                        <form className="d-flex">
                            <input className="form-control me-2"
                                type="search"
                                placeholder="Search"
                                aria-label="Search"
                            />
                            <button className="btn btn-outline-success me-2" type="submit">
                                Search
                            </button>
                        </form>
                        {isLoggedIn()
                            ?
                            <>
                                <Link className="btn btn-primary me-2" to='/dashboard'>Dashboard</Link>
                                <Link className="btn btn-primary me-2" to="/logout">Logout</Link>
                            </>
                            :
                            <>
                                <Link className="btn btn-primary me-2" to="/login">Login</Link>
                                <Link className="btn btn-primary me-2" to="/register">Register</Link>

                            </>
                        }
                        
                        <button className="btn btn-danger" type="submit">
                            <i className="fas fa-shopping-cart" />{" "}
                            <span id="cart-total-items">4</span>
                        </button>
                    </div>


                </div>

            </nav>
        </div>
    )

}

export default Header