import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';
import CustomNavbar from '../navbar/Navbar';
import Info from '../info/Info';
import Footer from '../footer/Footer';
import './About.css'; // Import local CSS file for About component styling
import Aboutbg from '../images/Aboutbg.jpg'; // Import the background image
import TeamMemberCard from './TeamMemberCard'; // Import the TeamMemberCard component

const About = () => {
  const sections = [
    {
      title: "Our Mission",
      content: "At Research Reimagined, our mission is to democratize knowledge by providing concise, easy-to-understand summaries of scientific papers and articles. We believe that everyone should have access to the latest research findings, regardless of their background or expertise."
    },
    {
      title: "How It Works",
      content: "Using cutting-edge natural language processing technology, our app analyzes scientific texts and generates clear and concise summaries. Whether you're a student, researcher, or simply curious about the latest discoveries, Scientific Summarizer is your gateway to understanding complex scientific concepts without the jargon."
    },
    {
      title: "Meet the Team",
      content: (
        <Row>
          <TeamMemberCard name="Sreedev T S" />
          <TeamMemberCard name="Sharon T Saju" />
          <TeamMemberCard name="Jafar N" />
        </Row>
      )
    },
    {
      title: "Contact Us",
      content: "Have questions or feedback? We'd love to hear from you! Reach out to us at researchreimagined@gmail.com and let us know how we can improve your experience with our app."
    }
  ];

  return (
    <>
      <CustomNavbar textColor="white" bgColor="transparent" />{/* Pass the background color and text color as props */}
      <div className="about-bg" style={{ backgroundImage: `url(${Aboutbg})`, backgroundSize: 'cover' }}> {/* Use a custom class for the background */}
        <Container fluid style={{ background: 'none' }}>
          <Row className="justify-content-center">
            <Col md={10}>
              <Card className="bg-transparent text-black rounded-lg shadow-lg">
                <Card.Body>
                  {/* Render the parent card with the "About Us" heading */}
                  <Card className="bg-transparent text-white mb-4">
                    <Card.Body>
                      <h4 className="mt-4 text-center" style={{ fontSize: '2rem', fontWeight: 'bold' }}>About Us</h4> {/* Increase font size and font weight */}
                      {sections.map((section, index) => (
                        <Card key={index} className={index % 2 === 0 ? "bg-black text-white mb-4 border-0" : "bg-black text-white mb-4 border-0"} style={{ background: 'black', color: 'white', border: 'none' }}>
                          <Card.Body>
                            <h4 className="mt-4" style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>{section.title}</h4> {/* Increase font size and font weight */}
                            <div>{section.content}</div>
                          </Card.Body>
                        </Card>
                      ))}
                    </Card.Body>
                  </Card>
                </Card.Body>
              </Card>
            </Col>
          </Row>
          <Info />
        </Container>
      </div>
      <Footer />
    </>
  );
};

export default About;
