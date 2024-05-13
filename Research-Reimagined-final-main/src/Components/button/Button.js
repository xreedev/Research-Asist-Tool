import React from 'react';
import Button from 'react-bootstrap/Button';
import './Button.css';

function CustomButton({ onPDFClick, onURLClick, onTextClick }) {

  const handlePDFClick = () => {
    if (onPDFClick) {
      onPDFClick('PDF'); // Call onPDFClick prop function with "PDF"
    }
  };

  const handleURLClick = () => {
    if (onURLClick) {
      onURLClick('URL'); // Call onURLClick prop function with "URL"
    }
  };

  const handleTextClick = () => {
    if (onTextClick) {
      onTextClick('TEXT'); // Call onTextClick prop function with "TEXT"
    }
  };

  return (
    <div className="container-fluid mt-4"> {/* Changed 'container' to 'container-fluid' */}
      <div className="row justify-content-center align-items-center">
        <div className="col-sm-12 col-md-4 mb-3 d-grid gap-2">
          <Button variant="dark" className="custom-button mb-2" onClick={handlePDFClick}>
            PDF
          </Button>
        </div>
        <div className="col-sm-12 col-md-4 mb-3 d-grid gap-2">
          <Button variant="dark" className="custom-button mb-2" onClick={handleURLClick}>
            URL
          </Button>
        </div>
        <div className="col-sm-12 col-md-4 mb-3 d-grid gap-2">
          <Button variant="dark" className="custom-button mb-2" onClick={handleTextClick}>
            TEXT
          </Button>
        </div>
      </div>
    </div>
  );
}

export default CustomButton;
