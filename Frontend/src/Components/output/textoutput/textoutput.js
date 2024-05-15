import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';

function TextOutput({ summarizedText }) {
  return (
    <Container fluid>
      <Row className="justify-content-center">
        <Col xs={12}>
          <Card style={{ height: '400px' }}> {/* Set the desired height */}
            <Card.Header style={{ fontWeight: 'bold' }}>Summary</Card.Header>
            <Card.Body style={{ maxHeight: '350px', overflowY: 'auto' }}> {/* Adjust maxHeight and overflowY as per your requirement */}
              {/* Display the summarized text */}
              <p>{summarizedText}</p>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default TextOutput;
