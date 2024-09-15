import React, { useState } from 'react';

const Chatbox = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');

  const handleSendMessage = () => {
    if (inputMessage.trim()) {
      setMessages([...messages, inputMessage]);
      setInputMessage('');
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen text-white bg-gray-900">
      <div className="w-full max-w-2xl p-6 bg-gray-800 rounded-lg shadow-lg">
        <h1 className="mb-6 text-3xl font-bold text-center">Chatbox</h1>

        {/* Chat Display Area */}
        <div className="p-4 mb-4 overflow-y-auto bg-gray-700 rounded-lg h-80">
          {messages.length > 0 ? (
            messages.map((msg, index) => (
              <div key={index} className="mb-2">
                <div className="max-w-xs p-2 break-words bg-indigo-600 rounded-lg">
                  {msg}
                </div>
              </div>
            ))
          ) : (
            <div className="text-center text-gray-400">No messages yet</div>
          )}
        </div>

        {/* Input Area */}
        <div className="flex items-center space-x-3">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder="Type a message..."
            className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
          <button
            onClick={handleSendMessage}
            className="px-4 py-2 font-bold bg-indigo-600 rounded-lg hover:bg-indigo-500 active:bg-indigo-700"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbox;
