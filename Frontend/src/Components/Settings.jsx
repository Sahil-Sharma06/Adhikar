import React, { useState } from 'react';

const SettingsPage = () => {
  const [isEditingName, setIsEditingName] = useState(false);
  const [isEditingPassword, setIsEditingPassword] = useState(false);
  const [isEditingLanguage, setIsEditingLanguage] = useState(false);

  const [name, setName] = useState('John Doe');
  const [password, setPassword] = useState('********');
  const [language, setLanguage] = useState('English');
  const [email] = useState('sahilsharma123@gmail.com'); // Fixed, can't be edited

  return (
    <div className="flex min-h-screen text-white bg-gray-900">
      
      {/* Sidebar */}
      <aside className="w-64 p-6 bg-gray-800">
        <nav className="space-y-4">
          <h2 className="text-2xl font-bold text-indigo-400">Menu</h2>
          <ul>
            <li className="px-4 py-2 font-semibold bg-indigo-600 rounded-lg">
              <a href="#settings" className="block">Settings</a>
            </li>
          </ul>
        </nav>
      </aside>

      {/* Settings Page Content */}
      <main className="flex-1 p-8">
        <h1 className="mb-8 text-4xl font-bold text-indigo-400">Settings</h1>
        
        {/* Name Setting */}
        <div className="flex items-center justify-between pb-4 mb-4 border-b border-gray-700">
          <div className="flex-1">
            <strong>Name:</strong> {isEditingName ? (
              <input 
                type="text" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
                className="px-2 py-1 ml-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
            ) : (
              <span className="ml-2">{name}</span>
            )}
          </div>
          <button
            onClick={() => setIsEditingName(!isEditingName)}
            className="px-4 py-2 font-bold bg-indigo-600 rounded-lg hover:bg-indigo-500 active:bg-indigo-700"
          >
            {isEditingName ? 'Save' : 'Edit'}
          </button>
        </div>

        {/* Password Setting */}
        <div className="flex items-center justify-between pb-4 mb-4 border-b border-gray-700">
          <div className="flex-1">
            <strong>Password:</strong> {isEditingPassword ? (
              <input 
                type="password" 
                value={password} 
                onChange={(e) => setPassword(e.target.value)} 
                className="px-2 py-1 ml-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
              />
            ) : (
              <span className="ml-2">{password}</span>
            )}
          </div>
          <button
            onClick={() => setIsEditingPassword(!isEditingPassword)}
            className="px-4 py-2 font-bold bg-indigo-600 rounded-lg hover:bg-indigo-500 active:bg-indigo-700"
          >
            {isEditingPassword ? 'Save' : 'Edit'}
          </button>
        </div>

        {/* Language Preference */}
        <div className="flex items-center justify-between pb-4 mb-4 border-b border-gray-700">
          <div className="flex-1">
            <strong>Language Preference:</strong> {isEditingLanguage ? (
              <select
                value={language}
                onChange={(e) => setLanguage(e.target.value)}
                className="px-2 py-1 ml-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
              >
                <option>English</option>
                <option>Hindi</option>
                <option>Bengali</option>
                <option>Tamil</option>
                <option>Telugu</option>
              </select>
            ) : (
              <span className="ml-2">{language}</span>
            )}
          </div>
          <button
            onClick={() => setIsEditingLanguage(!isEditingLanguage)}
            className="px-4 py-2 font-bold bg-indigo-600 rounded-lg hover:bg-indigo-500 active:bg-indigo-700"
          >
            {isEditingLanguage ? 'Save' : 'Edit'}
          </button>
        </div>

        {/* Email (Fixed) */}
        <div className="flex items-center justify-between pb-4 mb-4">
          <div className="flex-1">
            <strong>Email:</strong>
            <span className="ml-2">{email}</span>
          </div>
          <button
            disabled
            className="px-4 py-2 font-bold text-gray-400 bg-gray-700 rounded-lg cursor-not-allowed"
          >
            Fixed
          </button>
        </div>
      </main>
    </div>
  );
};

export default SettingsPage;
