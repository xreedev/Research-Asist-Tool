import React, { useState } from 'react';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';

function URLInput({ onSubmit }) {
  const [url, setUrl] = useState('');

  const handleInputChange = (e) => {
    setUrl(e.target.value);
  };

  const handleSubmit = () => {
    onSubmit(url);
    // Additional logic can be added here if needed
  };

  return (
    <div style={{ marginTop: '20px', marginBottom: '20px' }}> {/* Add margin top and bottom to the whole component */}
      <Container fluid>
        <Row className="justify-content-center">
          <Col xs={12}>
            <Card>
              <Card.Header style={{ fontWeight: 'bold' }}>Summarize</Card.Header>
              <Card.Body>
                <Form>
                  <Form.Group controlId="urlInput">
                    <Form.Label style={{ fontWeight: '600' }}>Enter Input URL:</Form.Label>
                    <Form.Control
                      type="text"
                      value={url}
                      onChange={handleInputChange}
                      placeholder="e.g., http://www.example.com"
                    />
                  </Form.Group>
                  <Button variant="dark" onClick={handleSubmit} style={{ marginTop: '20px' }}>Request For Summary</Button>
                </Form>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default URLInput;
