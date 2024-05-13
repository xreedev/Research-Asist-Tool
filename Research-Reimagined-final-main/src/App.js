import React, { useState } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import LoginForm from './Components/login/login';
import Landing from './Components/Landing/Landing';
import About from './Components/About/About';
import CustomNavbar from './Components/navbar/Navbar'; // Import the CustomNavbar component

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLoginSuccess = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
  };

  return (
    <Routes>
      <Route
        path="/"
        element={
          <>
            {/* Always render Navbar */}
            {isLoggedIn ? <Navigate to="/home" /> : <LoginForm onLoginSuccess={handleLoginSuccess} />} {/* Render LoginForm only when not logged in */}
          </>
        }
      />
      <Route path="/home" element={isLoggedIn ? <Landing /> : <Navigate to="/" />} />
      <Route path="/about-us" element={<About />} />
    </Routes>
  );
}

export default App;
