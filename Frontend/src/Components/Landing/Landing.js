import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import CustomNavbar from '../navbar/Navbar';
import URLInput from '../url/URLInput'; // Import the URLInput component
import TextOutput from '../output/textoutput/textoutput'; // Import the TextOutput component
import { Container, Row, Col } from 'react-bootstrap';
import landing3 from '../images/landing3.jpg'; // Import the new background image
import './Landing.css';
import CustomButton from '../button/Button';
import TextContent from '../TextContent/TextContent';
import Features from '../Features/Features';
import Footer from '..//footer/Footer';
import Info from '../info/Info';

const Landing = () => {
  const [activeComponent, setActiveComponent] = useState(null);
  const [isButtonClicked, setIsButtonClicked] = useState(false);
  const [showTextOutput, setShowTextOutput] = useState(false); // State for showing text output
  const [summarizedText, setSummarizedText] = useState(''); // State for summarized text

  const handleURLClick = (componentName) => {
    setActiveComponent(componentName);
    setIsButtonClicked(true);
  };

  const handleTextSubmit = (inputText) => {
    // Handle text submission logic here
    setSummarizedText(inputText);
    setShowTextOutput(true);
  };

  const renderComponent = () => {
    switch (activeComponent) {
      case 'URL':
        return (
          <Container fluid>
            <Row className="justify-content-center">
              <Col xs={12} md={8} lg={6} style={{ marginTop: '20px', marginBottom: '60px' }}>
                {activeComponent === 'URL' && <URLInput />}
              </Col>
            </Row>
            <div style={{ marginBottom: '120px' }}></div>
            {isButtonClicked && <hr style={{ border: 'none', borderBottom: '1px solid white', width: '100%' }} />}
            {isButtonClicked && <Info />}
            <Footer />
          </Container>
        );
      default:
        return (
          <>
            <TextContent />
            <CustomButton onURLClick={handleURLClick} />
            <Features />
            <Info />
            <Footer />
          </>
        );
    }
  };

  return (
    <>
      <CustomNavbar />
      <div
        style={{
          backgroundImage: `url(${landing3})`,
          color: 'white',
          paddingTop: '60px',
          minHeight: '100vh',
          overflowX: 'hidden',
          position: 'relative',
        }}
      >
        {renderComponent()}
      </div>
    </>
  );
};

export default Landing;
