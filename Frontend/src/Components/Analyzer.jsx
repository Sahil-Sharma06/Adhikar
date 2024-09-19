import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import bgImage from '../assets/BG.png';

const Analyzer = () => {
  const [file, setFile] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const navigate = useNavigate(); // Initialize navigate
  const [responseMessage, setResponseMessage] = useState(''); // State to hold the response message
  const [errorMessage, setErrorMessage] = useState(''); // State to hold any error message

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleAnalyze = async () => {
    // Combine title and description
    const data = {
      text: `${title} - ${description}`,
    };

    try {
      // Send POST request to the /features/analyze endpoint
      const response = await fetch('http://localhost:8000/features/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      // Parse the response
      const result = await response.json();

      if (response.ok) {
        setResponseMessage(result.message); // Display response message if request was successful
        setErrorMessage('');
        console.log('Title:', title);
        console.log('Description:', description);

        // Redirect to /display after successful analysis
        navigate('/display');
      } else {
        setErrorMessage('Error analyzing text. Please try again.');
      }
    } catch (error) {
      setErrorMessage('Failed to reach the server. Please try again later.');
    }
  };

  return (
    <div
      className="flex items-center justify-center min-h-screen text-white bg-gray-900"
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
      }}
    >
      <div className="w-full max-w-lg p-8 space-y-6 bg-custom-black rounded-lg shadow-lg">
        <h1 className="mb-6 text-3xl font-bold text-center">Upload or Provide Details</h1>

        {/* File Upload Section */}
        <div className="flex flex-col items-center space-y-4">
          <label
            htmlFor="file-upload"
            className="w-full px-4 py-2 text-center text-black bg-gray-400 border border-custom-signup-border rounded-lg cursor-pointer hover:bg-gray-600"
          >
            <input
              id="file-upload"
              type="file"
              accept=".pdf,.doc,.docx,.txt"
              onChange={handleFileChange}
              className="hidden"
            />
            {file ? file.name : 'Upload PDF or Document'}
          </label>
        </div>

        {/* Alternative Title and Description Input */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium">Title</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-3 py-2 mt-1 bg-black border text-gray-500 border-gray-600 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-custom-green"
              placeholder="Enter document title"
            />
          </div>

          <div>
            <label className="block text-sm font-medium">Description</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full px-3 py-2 mt-1 bg-black text-gray-500 border border-gray-600 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-custom-green"
              placeholder="Enter document description"
              rows="4"
            />
          </div>
        </div>

        <div className="text-center">
          <button
            onClick={handleAnalyze}
            className="w-full py-3 font-bold bg-gray-400 rounded-lg hover:bg-gray-600 text-black active:bg-indigo-700"
          >
            Analyze
          </button>
        </div>

        {/* Display the response or error message */}
        {responseMessage && (
          <div className="mt-6 p-4 text-black bg-green-300 rounded-lg">
            <p>{responseMessage}</p>
          </div>
        )}
        {errorMessage && (
          <div className="mt-6 p-4 text-black bg-red-300 rounded-lg">
            <p>{errorMessage}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Analyzer;