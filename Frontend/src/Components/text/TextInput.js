import React, { useState } from 'react';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';
import TextOutput from '../output/textoutput/textoutput'; // Import the TextOutput component

function TextInput({ onSubmit }) {
  const [textInput, setTextInput] = useState('');
  const [showSummary, setShowSummary] = useState(false); // State to manage whether to display the summary or not

  const handleInputChange = (event) => {
    setTextInput(event.target.value);
  };

  const handleSubmit = () => {
    onSubmit(textInput);
    setShowSummary(true); // Set showSummary to true when submitting the form
    // You can add any further logic here, like clearing the input field
  };

  return (
    <Container fluid>
      <Row className="justify-content-center">
        <Col xs={12}>
          <Card>
            <Card.Header style={{ fontWeight: 'bold' }}>Summarize</Card.Header>
            <Card.Body>
              <Form>
                <Form.Group controlId="textInput">
                  <Form.Label style={{ fontWeight: '600' }}>Enter The Input Text :</Form.Label> {/* Adjust font weight */}
                  <Form.Control 
                    as="textarea"
                    value={textInput} 
                    onChange={handleInputChange} 
                    style={{ 
                      resize: 'none',
                      height: '200px' // Increase the height
                    }}
                  />
                </Form.Group>
                <Button variant="dark" onClick={handleSubmit} style={{ marginTop: '20px' }}>Request for Summary</Button>
              </Form>
            </Card.Body>
          </Card>
        </Col>
      </Row>
      {/* Conditionally render the TextOutput component based on showSummary state */}
      {showSummary && (
        <Row className="justify-content-center">
          <Col xs={12}>
            <TextOutput summarizedText={textInput} />
          </Col>
        </Row>
      )}
    </Container>
  );
}

export default TextInput;
