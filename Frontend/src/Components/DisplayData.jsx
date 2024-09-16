import React, { useState } from 'react';
import bgImage from '../assets/BG.png'; // Import your background image
import '../index.css';
import Markdown from 'react-markdown'

const KnowMore = () => {
  const [isFocused, setIsFocused] = useState(false); // Track input focus state
  const [caseName, setCaseName] = useState(''); // Store case name input
  const [act, setAct] = useState(''); // Store Act data
  const [details, setDetails] = useState(''); // Store Details data
  const [isLoading, setIsLoading] = useState(false); // Track loading state
  const [errorMessage, setErrorMessage] = useState(''); // Store any error message

  const handleKnowClick = async () => {
    setIsLoading(true);
    setErrorMessage(''); // Clear any previous errors
    try {
      const response = await fetch('http://localhost:8000/features/knowlaw', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          text: caseName, // Send the case name input as part of the POST request body
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setAct(data.Law); // Assuming the response has 'act' field
        setDetails(data.Explanation); // Assuming the response has 'details' field
      } else {
        setErrorMessage('Failed to fetch data. Please try again.');
      }
    } catch (error) {
      setErrorMessage('An error occurred. Please check your connection.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main
      className="relative flex items-center w-screen h-lvh justify-evenly bg-custom-black"
      style={{
        backgroundImage: `url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
      }}
    >
      {/* Center Content */}
      <div
        className={`flex flex-col items-center justify-start w-[50%] h-[80%] p-6 space-y-6 border-4 relative ${
          isFocused ? 'border-custom-green' : 'border-custom-signup-border'
        } mb-20`}
        style={{ marginTop: '10%' }} // Ensure top margin to push down the container
      >
        {/* Title */}
        <h1 className="mb-6 text-3xl text-center text-white border-b-2 w-lvh">Analysis of the Case</h1>

        <div className="flex flex-col items-center justify-center w-full mt-8 space-y-6">

          {/* Error message */}
          {errorMessage && <p className="text-red-500">{errorMessage}</p>}

          {/* Act and Details always visible */}
          <div className="flex flex-col w-full space-y-4 text-white">
            {/* Act Field */}
            <div className="flex items-start w-full">
              <h3 className="mr-7">Act:</h3>
              <p
                className="flex-grow p-2 ml-4 border-2 rounded border-custom-green bg-custom-black"
                style={{ overflow: 'auto', textOverflow: 'ellipsis' }}
              >
                {act || 'No Act available'}
              </p>
            </div>

            {/* Details of the Act Field */}
            <div className="flex items-start w-full">
              <h3 className="mr-4">Details:</h3>
              <p
                className="flex-grow p-2 border-2 rounded h-4/5 border-custom-green bg-custom-black"
                style={{ overflow: 'auto', textOverflow: 'ellipsis' }}
              >
                <Markdown>
                {details || 'No details available'}
                </Markdown>
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default KnowMore;

















