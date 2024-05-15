import React, { useState, useRef, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Import Link
import './login.css';

const LoginForm = ({ onLoginSuccess }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailErrorMsg, setEmailErrorMsg] = useState('');
  const [passwordErrorMsg, setPasswordErrorMsg] = useState('');
  const emailInputRef = useRef(null); // Create a ref for the email input

  useEffect(() => {
    // Focus on the email input when the component mounts
    emailInputRef.current.focus();
  }, []); // Empty dependency array to run the effect only once

  const handleLogin = (event) => {
    event.preventDefault(); // Prevent form submission

    // Validate email
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email)) {
      setEmailErrorMsg("Please enter a valid email.");
      return;
    } else {
      setEmailErrorMsg(""); // Clear error message
    }

    // Validate password
    if (password.length < 6) {
      setPasswordErrorMsg("Password must be at least 6 characters.");
      return;
    } else {
      setPasswordErrorMsg(""); // Clear error message
    }

    // Call onLoginSuccess if email and password are valid
    onLoginSuccess();
  };

  return (
    <div className="wrapper">
      <form id="loginForm" onSubmit={handleLogin}>
        <h1>Login</h1>
        <div className="input-box">
          <input
            type="text"
            placeholder="Email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            ref={emailInputRef} // Set ref to the email input
          />
          <i className='bx bx-envelope'></i>
        </div>
        <div className="input-box">
          <input
            type="password"
            placeholder="Password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <i className='bx bxs-lock-alt'></i>
        </div>
        <div className="remember-forgot">
          <label>
            <input type="checkbox" />
            Remember me
          </label>

        </div>
        <button type="submit" className="btn">Login</button>
        <div className="register-link" id="emailerrormsg">{emailErrorMsg}</div>
        <div className="register-link" id="pswderrorMsg">{passwordErrorMsg}</div>

      </form>
    </div>
  );
};

export default LoginForm;
