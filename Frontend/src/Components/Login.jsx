import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { imp } from '../../data/data.js';
import leftImage from '../assets/ascii-column-left.png';
import rightImage from '../assets/ascii-column-right.png';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(imp[0].domain + '/auth/login', {
        email,
        password,
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log('Login successful:', response.data);
    } catch (err) {
      if (err.response && err.response.data) {
        setError(`Login failed: ${err.response.data.message || 'Please try again.'}`);
      } else {
        setError('Login failed. Please try again.');
      }
      console.error('Login error:', err.response ? err.response.data : err);
    }
  };

  return (
    <main className="relative flex items-center w-full h-screen justify-evenly bg-custom-black">
      <div className="fixed top-0 left-0 w-1/3 h-full" style={{marginTop:'2%', marginLeft: '25%' }}>
        <img src={leftImage} alt="Left" className="object-cover " />
      </div>
      
      <div className="relative flex-1 max-w-md mx-auto space-y-6 text-white border-4 border-custom-signup-border bg-custom-black sm:max-w-md" style={{ fontFamily: '"Source Code Pro", monospace', fontWeight: 500 }}>
        <div className="p-4 py-2 bg-custom-black sm:rounded-lg">
          <div className="mb-6 border-b">
            <div className="space-y-2">
              <h3 className="w-full mb-4 text-xl font-medium text-white sm:text-3xl">// Login</h3>
            </div>
          </div>
          {error && <p className="text-center text-red-500">{error}</p>}
          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="font-medium uppercase">Email</label>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full px-3 py-2 mt-2 text-gray-500 bg-transparent border rounded-lg shadow-sm outline-none border-custom-signup-border focus:border-custom-green focus:ring-2 focus:ring-custom-green focus:ring-opacity-50 focus:outline-none caret-custom-green broad-caret"
              />
            </div>
            <div>
              <label className="font-medium uppercase">Password</label>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-3 py-2 mt-2 text-gray-500 bg-transparent border rounded-lg shadow-sm outline-none border-custom-signup-border focus:border-custom-green focus:ring-2 focus:ring-custom-green focus:ring-opacity-50 focus:outline-none caret-custom-green broad-caret"
              />
            </div>
            <button
              type="submit"
              className="w-full px-4 py-2 font-medium text-black duration-150 bg-gray-300 rounded-lg hover:bg-gray-400 active:bg-gray-500"
            >
              Login
            </button>
            <div className="mt-2 text-center">
              <p>
                Don't have an Account?{' '}
                <Link to="/register" className="font-medium underline hover:text-indigo-500">
                  SignUp
                </Link>
              </p>
            </div>
          </form>
        </div>
      </div>

      <div className="fixed top-0 right-0 w-1/3 h-full" style={{marginTop:'2%',  marginLeft: '5%' }}>
        <img src={rightImage} alt="Right" className="object-cover " />
      </div>
    </main>
  );
};

export default Login;
