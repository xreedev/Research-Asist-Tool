import React, { useState } from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';

function PDFInput() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    const uploadedFile = event.target.files[0];
    if (uploadedFile) {
      setFile(uploadedFile);
    }
  };

  const handleUploadClick = () => {
    const input = document.getElementById('pdfInput');
    input.click();
  };

  const handleSummaryRequest = () => {
    // Request summary functionality goes here
    console.log('Requesting summary for:', file.name);
    // Here you can implement the logic for handling the summary request
  };

  return (
    <div style={{ marginTop: '20px', marginBottom: '20px' }}>
      <Container fluid> {/* Change here to make the Container fluid */}
        <Row className="justify-content-center">
          <Col xs={12}>
            <Card style={{ minHeight: '230px' }}>
              <Card.Header style={{ fontWeight: 'bold' }}>Summarize</Card.Header>
              <Card.Body>
                <input type="file" accept=".pdf" style={{ display: 'none' }} id="pdfInput" onChange={handleFileChange} />
                <label htmlFor="pdfInput">
                  <Button variant="outline-secondary" onClick={handleUploadClick} style={{ color: 'black', fontWeight: '600' }}>Upload PDF</Button>
                </label>
                <div>{file && <p>{file.name}</p>}</div>
              </Card.Body>
              <Card.Footer style={{ paddingTop: '15px', paddingBottom: '15px' }}>
                <Button variant="dark" onClick={handleSummaryRequest}>Request For Summary</Button>
              </Card.Footer>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default PDFInput;
