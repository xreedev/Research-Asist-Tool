import React, { useState } from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import PDFOutput from '../output/pdfoutput/pdfoutput'; // Import the PDFOutput component

function PDFInput() {
  const [file, setFile] = useState(null);
  const [showSummary, setShowSummary] = useState(false); // State to manage whether to display the summary or not
  const [summarizedText, setSummarizedText] = useState('');

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
    // Simulate summary request functionality
    const summary = "";
    setSummarizedText(summary);
    setShowSummary(true); // Set showSummary to true when summary is available
  };

  return (
    <div style={{ marginTop: '20px', marginBottom: '20px' }}>
      <Container fluid>
        {!showSummary ? ( // Render the PDF input form if showSummary is false
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
        ) : ( // Render the PDFOutput component if showSummary is true
          <Row className="justify-content-center">
            <Col xs={12}>
              <PDFOutput summarizedText={summarizedText} />
            </Col>
          </Row>
        )}
      </Container>
    </div>
  );
}

export default PDFInput;
