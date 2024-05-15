import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col, Card } from 'react-bootstrap';

function URLOutput({ url }) {
  const [summarizedData, setSummarizedData] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchSummarizedData = async () => {
      setLoading(true);
      try {
        const response = await axios.post('http://localhost:5000/summarize', { url: url });
        setSummarizedData(response.data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching data');
        setLoading(false);
      }
    };
    
    fetchSummarizedData();
  }, [url]);

  return (
    <Container fluid>
      <Row className="justify-content-center">
        <Col xs={12}>
          <Card style={{ height: '400px' }}>
            <Card.Header style={{ fontWeight: 'bold' }}>Summary</Card.Header>
            <Card.Body style={{ maxHeight: '350px', overflowY: 'auto' }}>
              {loading && <p>Loading...</p>}
              {error && <p>{error}</p>}
              {Object.keys(summarizedData).map((key, index) => (
                <div key={index}>
                  <h2>{key}</h2>
                  <p>{summarizedData[key]}</p>
                </div>
              ))}
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}

export default URLOutput;
