import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import CustomNavbar from '../navbar/Navbar';
import CustomButton from '../button/Button';
import TextContent from '../TextContent/TextContent';
import Features from '../Features/Features';
import Footer from '..//footer/Footer';
import Info from '../info/Info';
import TextInput from '../text/TextInput';
import PDFInput from '../pdf/PDFInput';
import URLInput from '../url/URLInput';
import { Container, Row, Col } from 'react-bootstrap';
import landing3 from '../images/landing3.jpg'; // Import the new background image
import './Landing.css';

const Landing = () => {
  const [activeComponent, setActiveComponent] = useState(null);
  const [isButtonClicked, setIsButtonClicked] = useState(false);

  const handlePDFClick = (componentName) => {
    setActiveComponent(componentName);
    setIsButtonClicked(true);
  };

  const handleURLClick = (componentName) => {
    setActiveComponent(componentName);
    setIsButtonClicked(true);
  };

  const handleTextClick = (componentName) => {
    setActiveComponent(componentName);
    setIsButtonClicked(false);
  };

  const renderComponent = () => {
    switch (activeComponent) {
      case 'PDF':
      case 'URL':
        return (
          <Container fluid>
            <Row className="justify-content-center">
              <Col xs={12} md={8} lg={6} style={{ marginTop: '20px', marginBottom: '30px' }}>
                {activeComponent === 'PDF' && <PDFInput />}
                {activeComponent === 'URL' && <URLInput />}
              </Col>
            </Row>
            {/* Add additional space between PDF/URL component and Info component */}
            <div style={{ marginBottom: '120px' }}></div>
            {isButtonClicked && <hr style={{ border: 'none', borderBottom: '1px solid white', width: '100%' }} />}
            {isButtonClicked && <Info />}
            <Footer />
          </Container>
        );
      case 'TEXT':
        return (
          <Container fluid>
            <Row className="justify-content-center">
              <Col xs={12} md={8} lg={6} style={{ marginTop: '20px', marginBottom: '30px' }}>
                <TextInput />
              </Col>
            </Row>
            <hr style={{ border: 'none', borderBottom: '1px solid white', width: '100%' }} />
            <Info />
            <Footer />
          </Container>
        );
      default:
        return (
          <>
            <TextContent />
            <CustomButton onPDFClick={handlePDFClick} onURLClick={handleURLClick} onTextClick={handleTextClick} />
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
          backgroundImage: `url(${landing3})`, // Set background image
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
