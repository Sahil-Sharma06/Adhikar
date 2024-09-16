import React, { useState } from 'react';
import leftImage from '../assets/ascii-column-left.png';
import rightImage from '../assets/ascii-column-right.png';
import bgImage from '../assets/BG.png'; // Import your background image
import '../index.css';

const KnowMore = () => {
  const [isFocused, setIsFocused] = useState(false); // Track input focus state

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
        {/* Title - Positioned at the Top */}
        <h1 className="mb-6 text-3xl text-center text-white border-b-2 w-svh">Know About the Case</h1>

        {/* Add margin to move the content down */}
        <div className="flex flex-col items-center justify-center w-full mt-8 space-y-6">
          {/* Case Input */}
          <div className="flex items-center w-full mb-4">
            <h2 className="mr-2 text-white">Case:</h2>
            <input
              type="text"
              className={`bg-black text-gray-400 flex-grow p-2 border-4 rounded focus:border-custom-green focus:ring-2 focus:ring-custom-green focus:ring-opacity-50 focus:outline-none caret-custom-green broad-caret ${
                isFocused ? 'border-custom-green' : 'border-custom-signup-border'
              }`}
              placeholder="Enter case name"
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
            />
          </div>

          {/* Know Button */}
          <button className="w-[300px] p-2 text-black bg-gray-300 rounded mb-12 ml-10">Know</button>

          {/* Act and Details Container */}
          <div className="flex flex-col w-full space-y-4 text-white">
            {/* Act Field */}
            <div className="flex items-start w-full">
              <h3 className="mr-7">Act:</h3>
              <p
                className="flex-grow p-2 ml-4 border-2 rounded border-custom-green bg-custom-black"
                style={{ overflow: 'auto', textOverflow: 'ellipsis' }}
              >
                Indian Penal Code (IPC)
              </p>
            </div>

            {/* Details of the Act Field */}
            <div className="flex items-start w-full">
              <h3 className="mr-4">Details:</h3>
              <p
                className="flex-grow p-2 border-2 rounded h-4/5 border-custom-green bg-custom-black"
                style={{ overflow: 'auto', textOverflow: 'ellipsis' }}
              >
                The Indian Penal Code (IPC) is the official criminal code of India. It is a comprehensive code intended to cover all substantive aspects of criminal law. Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem dolore a dolores, nesciunt, ab eius vel incidunt dolor voluptatum non necessitatibus velit possimus? Lorem ipsum, dolor sit amet consectetur adipisicing elit. Veritatis quam voluptatem perspiciatis velit id incidunt excepturi? Aut, distinctio eos numquam vero incidunt velit reprehenderit nesciunt eaque atque autem, fugiat nobis ducimus voluptatibus beatae tempora?Lorem, ipsum dolor sit amet consectetur adipisicing elit. Accusantium ex necessitatibus possimus? Quaerat tempora laboriosam vitae quisquam, velit ex culpa, quae perferendis atque qui accusamus, esse saepe aperiam excepturi. Sequi quam incidunt pariatur vitae commodi, tenetur esse temporibus, velit aperiam eum fuga voluptatibus dolore ullam tempora itaque laboriosam? Labore repellendus porro aspernatur vero reiciendis accusantium hic, fuga quidem eveniet, et illo quae architecto nobis reprehenderit culpa non!
              </p>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default KnowMore;
