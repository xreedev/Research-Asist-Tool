import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';

function URLOutput({ summarizedURL }) {
  return (
    <Container fluid>
      <Row className="justify-content-center">
        <Col xs={12}>
          <Card style={{ height: '400px' }}>
            <Card.Header style={{ fontWeight: 'bold' }}>Summary</Card.Header>
            <Card.Body style={{ maxHeight: '350px', overflowY: 'auto' }}>
              <p>{summarizedURL}</p>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default URLOutput;
