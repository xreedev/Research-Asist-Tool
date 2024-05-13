import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import './Features.css'; // Import custom CSS file

const Features = () => {
  return (
    <Container fluid className="mt-5 mb-5 container-border"> {/* Change 'Container' to 'Container fluid' */}
      <h2 className="mb-5">What can you do with the summarizing tool ?</h2>
      <Row xs={1} md={2} lg={3} className="g-4"> 
        <FeatureCard
          title="Summarization"
          description="Simplify scientific papers by replacing complex terms with easier meanings, making them more accessible and understandable."
        />
        <FeatureCard
          title="Powerpoint Content Generation"
          description="Automatically generate presentation content from the summarized scientific paper, streamlining the process of creating presentations."
        />
        <FeatureCard
          title="Text-to-Speech Conversion"
          description="Convert the summarized content into an audio file, enhancing accessibility by catering to users with different learning preferences."
        />
      </Row>
    </Container>
  );
}

const FeatureCard = ({ title, description }) => {
  return (
    <Col>
      <Card className="feature-card">
        <Card.Body>
          <Card.Title>{title}</Card.Title>
          <Card.Text>{description}</Card.Text>
        </Card.Body>
      </Card>
    </Col>
  );
}

export default Features;
