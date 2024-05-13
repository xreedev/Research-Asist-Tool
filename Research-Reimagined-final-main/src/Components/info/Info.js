import React from 'react';
import './Info.css'; // Import the CSS file

function Info() {
  return (
    <div className="container-fluid" style={{ paddingTop: '30px' }}> {/* Change container to container-fluid */}
      <div className="row">
        <div className="col-lg-4 mb-4 mr-lg-3">
          <h2>About Us</h2>
          <p>
            <strong>Research Reimagined</strong> was founded in 2024 with the aim of simplifying the comprehension of scientific articles, it utilizes cutting-edge AI technology to condense lengthy texts, enabling users to grasp their essence without delving into the entire content
          </p>
        </div>
        <div className="col-lg-4 pl-lg-4">
          <h2>Contact Info</h2>
          <p>
            <strong>Email:</strong> researchreimagined@gmail.com <br />
            <strong>Phone:</strong> +91 8943750702
          </p>
        </div>
        <div className="col-lg-4">
          <h2>Important Links</h2>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            <li><a href="#" className="link-no-decoration">Privacy Policy</a></li>
            <li><a href="#" className="link-no-decoration">Terms of Service</a></li>
            <li><a href="#" className="link-no-decoration">Log In</a></li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Info;
