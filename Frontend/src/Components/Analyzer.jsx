import React, { useState } from 'react';

const Analyzer = () => {
  const [file, setFile] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleAnalyze = () => {
    if (file) {
      console.log('File uploaded:', file.name);
    }
    console.log('Title:', title);
    console.log('Description:', description);
  };

  return (
    <div className="flex items-center justify-center min-h-screen text-white bg-gray-900">
      <div className="w-full max-w-lg p-8 space-y-6 bg-gray-800 rounded-lg shadow-lg">
        <h1 className="mb-6 text-3xl font-bold text-center">Upload or Provide Details</h1>

        {/* File Upload Section */}
        <div className="flex flex-col items-center space-y-4">
          <label htmlFor="file-upload" className="w-full px-4 py-2 text-center bg-gray-700 border border-gray-600 rounded-lg cursor-pointer hover:bg-gray-600">
            <input
              id="file-upload"
              type="file"
              accept=".pdf,.doc,.docx,.txt"
              onChange={handleFileChange}
              className="hidden"
            />
            {file ? file.name : "Upload PDF or Document"}
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
              className="w-full px-3 py-2 mt-1 bg-gray-700 border border-gray-600 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
              placeholder="Enter document title"
            />
          </div>

          <div>
            <label className="block text-sm font-medium">Description</label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full px-3 py-2 mt-1 bg-gray-700 border border-gray-600 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
              placeholder="Enter document description"
              rows="4"
            />
          </div>
        </div>

        {/* Analyze Button */}
        <div className="text-center">
          <button
            onClick={handleAnalyze}
            className="w-full py-3 font-bold bg-indigo-600 rounded-lg hover:bg-indigo-500 active:bg-indigo-700"
          >
            Analyze
          </button>
        </div>
      </div>
    </div>
  );
};

export default Analyzer;
