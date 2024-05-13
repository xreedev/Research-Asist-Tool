import React from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './TextContent.css'; // Import custom CSS file

function TextContent() {
  return (
    <Container fluid className="py-3 text-center text-content">
      <Row>
        <Col>
          <h1 className='header-content'>Welcome to Research Reimagined</h1>
          <p className="lead">Discover innovative solutions for your research needs.</p>
          <p>Learn more about us <a href="#about-us">here</a>.</p>
        </Col>
      </Row>
      <Row>
        <Col>
          <p className="choose-format">Choose A Format For Uploading</p> {/* Apply custom class */}
        </Col>
      </Row>
    </Container>
  );
}

export default TextContent;
