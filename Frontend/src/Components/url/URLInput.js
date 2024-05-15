import React, { useState } from 'react';
import { Container, Row, Col, Card, Form, Button } from 'react-bootstrap';
import URLOutput from '../output/urloutput/urloutput'; // Import the URLOutput component

function URLInput({ onSubmit }) {
  const [url, setUrl] = useState('');
  const [showSummary, setShowSummary] = useState(false); // State to manage whether to display the summary or not
  const [summarizedURL, setSummarizedURL] = useState('');
  const [pptDownloaded, setPptDownloaded] = useState(false); // State to track if PPT is downloaded
  const [audioDownloaded, setAudioDownloaded] = useState(false); // State to track if audio is downloaded

  const handleInputChange = (e) => {
    setUrl(e.target.value);
  };

  const handleSubmit = async () => {
    // Simulate getting summarized URL from the input URL
    const summarizedURL = await getSummarizedURLFromURL(url);
    setSummarizedURL(summarizedURL);
    setShowSummary(true); // Set showSummary to true when submitting the form
  };

  // This is a placeholder function to simulate fetching summarized URL
  const getSummarizedURLFromURL = async (inputURL) => {
    // You can replace this with your actual logic to get summarized URL from the input URL
    return `${inputURL}`;
  };

  const handlePPTDownload = async () => {
    // Download PPT
    console.log("Downloading PPT...");
    setPptDownloaded(true);
    const response = await fetch('http://localhost:5000/download_ppt');
    const blob = await response.blob();
    const url = window.URL.createObjectURL(new Blob([blob]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'new.pptx');
    document.body.appendChild(link);
    link.click();
  };
  
  const handleAudioDownload = async () => {
    // Download audio
    console.log("Downloading audio...");
    setAudioDownloaded(true);
    const response = await fetch('http://localhost:5000/download_audio');
    const blob = await response.blob();
    const url = window.URL.createObjectURL(new Blob([blob]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'audio.mp3');
    document.body.appendChild(link);
    link.click();
  };
  


  return (
    <div style={{ marginTop: '20px', marginBottom: '20px' }}>
      <Container fluid>
        {!showSummary ? ( // Render the URL input form if showSummary is false
          <Row className="justify-content-center">
            <Col xs={12}>
              <Card>
                <Card.Header style={{ fontWeight: 'bold' }}>Summarize URL</Card.Header>
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
                    <Button variant="dark" onClick={handleSubmit} style={{ marginTop: '30px' }}>Request For Summary</Button>
                  </Form>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        ) : ( // Render the URLOutput component if showSummary is true
          <Row className="justify-content-center">
            <Col xs={12}>
              <URLOutput url={url} /> {/* Pass url instead of summarizedURL */}
              {/* Add download buttons */}
              <Button variant="success" onClick={handlePPTDownload} style={{ margin: '10px' }}>Download PPT</Button>
              <Button variant="primary" onClick={handleAudioDownload} style={{ margin: '10px' }}>Download Audio</Button>
              {/* Display a message if PPT or audio is downloaded */}
              {pptDownloaded && <p>PPT downloaded successfully!</p>}
              {audioDownloaded && <p>Audio downloaded successfully!</p>}
            </Col>
          </Row>
        )}
      </Container>
    </div>
  );
}

export default URLInput;
