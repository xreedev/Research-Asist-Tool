import React from 'react';
import './Footer.css'; // Import custom CSS file
import { Container } from 'react-bootstrap';

function Footer() {
  return (
    <footer className="footer">
      <Container fluid>
        <span className="text-muted">© 2024 Research Reimagined. All rights reserved.</span>
      </Container>
    </footer>
  );
}

export default Footer;
