import React, { useState } from 'react';
import { Link } from 'react-router-dom'; // Import Link
import './Signup.css';

const Signup = ({ onSignup }) => {
  const [fullName, setFullName] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [emailErrorMsg, setEmailErrorMsg] = useState('');
  const [passwordErrorMsg, setPasswordErrorMsg] = useState('');
  const [repeatPasswordErrorMsg, setRepeatPasswordErrorMsg] = useState('');

  const handleSignup = (event) => {
    event.preventDefault();
    // Your signup logic here
    console.log('Signing up...');
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

    // Validate repeat password
    if (password !== repeatPassword) {
      setRepeatPasswordErrorMsg("Passwords do not match.");
      return;
    } else {
      setRepeatPasswordErrorMsg(""); // Clear error message
    }

    // Pass signup data to parent component if all validations pass
    onSignup({ fullName, username, email, password, repeatPassword });
  };

  return (
    <div className="wrapper">
      <form id="signupForm" onSubmit={handleSignup}>
        <h1>Sign Up</h1>
        <div className="input-box">
          <input type="text" placeholder="Full Name" required value={fullName} onChange={(e) => setFullName(e.target.value)} />
        </div>
        <div className="input-box">
          <input type="text" placeholder="Username" required value={username} onChange={(e) => setUsername(e.target.value)} />
        </div>
        <div className="input-box">
          <input type="email" placeholder="Email" required value={email} onChange={(e) => setEmail(e.target.value)} />
        </div>
        <div className="input-box">
          <input type="password" placeholder="Password" required value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <div className="input-box">
          <input type="password" placeholder="Repeat Password" required value={repeatPassword} onChange={(e) => setRepeatPassword(e.target.value)} />
        </div>
        <button type="submit" className="btn">Create Account</button>
        <div className="register-link">Already have an account? <Link to="/">Login</Link></div> {/* Change Link destination to "/login" */}
        <div className="register-link" id="emailerrormsg">{emailErrorMsg}</div>
        <div className="register-link" id="pswderrorMsg">{passwordErrorMsg}</div>
        <div className="register-link" id="repeatPswderrorMsg">{repeatPasswordErrorMsg}</div>
      </form>
    </div>
  );
};

export default Signup;
