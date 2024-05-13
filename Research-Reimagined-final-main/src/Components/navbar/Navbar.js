import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link, useLocation } from 'react-router-dom'; // Import useHistory
import './Navbar.css';

function CustomNavbar({ textColor, bgColor }) {
  const location = useLocation();

  const handleLogout = () => {
    // Perform logout actions here
    // For now, just redirect to the login page
    window.location.href = "/"; // Redirect to the login page
  };

  return (
    <Navbar style={{ backgroundColor: bgColor }} variant="dark" className="custom-navbar" expand="lg" fixed="top">
      <Container fluid>
        <Navbar.Brand as={Link} to="/" href="#home" style={{ color: textColor }}>Research Reimagined</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ms-auto me-3">
            <Nav.Link as={Link} to="/about-us" className="nav-link me-3" style={{ color: textColor }}>About Us</Nav.Link>
            <Nav.Link onClick={handleLogout} className="nav-link me-3" style={{ color: textColor }}>Log Out</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default CustomNavbar;
