import React from 'react';
import { Card, Row, Col } from 'react-bootstrap';

const TeamMemberCard = ({ name }) => {
  const loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod felis id tortor vehicula fringilla. Nullam vel justo ut libero vehicula suscipit. Nam vel nisi nec turpis malesuada interdum. Proin convallis felis eget nulla convallis varius. In in quam vitae sapien tincidunt convallis ac a nunc. Aliquam luctus tortor eget ligula ultricies bibendum.";

  return (
    <Col className="mb-4">
      <Card className="bg-black text-white" style={{ background: 'black', color: 'white' }}>
        <Card.Body>
          <h4 className="mt-4" style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>{name}</h4>
          <p>{loremIpsum}</p>
        </Card.Body>
      </Card>
    </Col>
  );
};

export default TeamMemberCard;
