import React from 'react'

const Dashboard = () => {
  return (
   <div class="w-full h-screen xx flex flex-col">
    <header class="mb-4 flex items-center justify-between py-4 md:py-8 bg-black  w-full">
     
     <a href="/" class="inline-flex items-center gap-2.5 text-2xl font-bold text-white md:text-3xl font-montserrat fd" aria-label="logo">
     <img class="w-8" src="./public/piller-r.png" alt="logo" />
      ADHIKAR
     </a>
    
     <nav class="hidden gap-12 lg:flex">
       {/* <a href="#" class="text-lg font-semibold text-green-400">Dashboard</a> */}
       {/* <a href="#" class="text-lg font-semibold text-gray-600 transition duration-100 hover:text-green-400 active:text-green-300">Features</a> */}
       {/* <a href="#" class="text-lg font-semibold text-gray-600 transition duration-100 hover:text-green-400 active:text-green-300">Pricing</a> */}
       {/* <a href="#" class="text-lg font-semibold text-gray-600 transition duration-100 hover:text-green-400 active:text-green-300">About</a> */}
     </nav>

     {/* <a href="#" class="hidden rounded-lg bg-black px-8 py-3 text-center text-sm font-semibold text-green-300 outline-none ring-indigo-300 transition duration-100 hover:outline-green-200 focus-visible:ring active:text-gray-700 md:text-base lg:inline-block">Get Started</a> */}

     <button type="button" class="inline-flex items-center gap-2 rounded-lg bg-black px-2.5 py-2 text-sm font-semibold text-green-200 ring-indigo-300  focus-visible:ring active:text-gray-700 md:text-base lg:hidden">
       <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
         <path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h6a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd" />
       </svg>
       Menu
     </button>
    
   </header>
    <div class="flex justify-center items-center gaa h-screen p-6 ">
        <div class="flex flex-col items-center w-[20vw] h-[65vh] border shadow-lg rounded-lg overflow-hidden da-1">
            <img src="./src/assets/t2.jpg" alt="Card Image" class="w-full h-[25vh] object-cover mb-4"/>
               <div class="p-4 flex-1">
               <h2 class="text-xl font-semibold mb-2 text-white">SETTLE</h2>
      <p class="text-white mb-4 ty"><b>Virtual Resolution:</b> Provides users with potential resolutions, enabling them to settle disputes outside of court.
      </p>
      <p class="text-white mb-4 ty"><b>Outcome Prediction:</b> Offers insights into likely case results, helping users make informed decisions.</p>
      <div class="w-full  flex justify-center ">
      <a class=" bg-green-900 rounded-[4px] font-nb-architekt uppercase bg-green-2 text-green-1 outline-none transition-all duration-300 ease-in-out focus-within:outline-offset-2  text-green-600 focus-within:outline-green-1 focus-within:brightness-150 hover:brightness-150 px-4 py-3 text-[14px] md:px-7 md:py-4 md:text-[18px]" 
              href="#">Comming Soon..
        </a>  
      </div>
    </div>
  </div>
        <div class="flex flex-col items-center w-[20vw] h-[65vh] border shadow-lg rounded-lg overflow-hidden da-2">
            <img src="./src/assets/t3.jpg" alt="Card Image" class="w-full h-[25vh] object-cover mb-4"/>
               <div class="p-4 flex-1">
               <h2 class="text-xl font-semibold mb-2 text-white">Know Your Case</h2>
      <p class="text-white mb-4 ty"><b>IP Section Expertise:</b> Analyzes various intellectual property sections and rules to classify the case accurately.</p>
      <p class="text-white mb-4 ty"><b>Case Understanding:</b> Helps users understand the nature of their case and the applicable legal sections.</p>
      <div class="w-full  flex justify-center ">
      <a class=" bg-green-900 rounded-[4px] font-nb-architekt uppercase bg-green-2 text-green-1 outline-none transition-all duration-300 ease-in-out focus-within:outline-offset-2  text-green-600 focus-within:outline-green-1 focus-within:brightness-150 hover:brightness-150 px-4 py-3 text-[14px] md:px-7 md:py-4 md:text-[18px]" 
              href="/know">Know
        </a>  
      </div>
    </div>
  </div>
        <div class="flex flex-col items-center w-[20vw] h-[65vh] border shadow-lg rounded-lg overflow-hidden da-3">
            <img src="./src/assets/t1.jpg" alt="Card Image" class="w-full h-[25vh] object-cover mb-4"/>
               <div class="p-4 flex-1">
               <h2 class="text-xl font-semibold mb-2 text-white">Analyze</h2>
      <p class="text-white mb-4 ty"><b>Judicial Assistance:</b> Supports judges by summarizing case details and relevant information to save time.</p>
      <p class="text-white mb-4 ty"><b>Efficiency Boost:</b> Enhances case management and decision-making through detailed document analysis.</p>
      <div class="w-full  flex justify-center ">
      <a class=" bg-green-900 rounded-[4px] font-nb-architekt uppercase bg-green-2 text-green-1 outline-none transition-all duration-300 ease-in-out focus-within:outline-offset-2  text-green-600 focus-within:outline-green-1 focus-within:brightness-150 hover:brightness-150 px-4 py-3 text-[14px] md:px-7 md:py-4 md:text-[18px]" 
              href="/analyze">Analyse
        </a>  
      </div>
    </div>
  </div>
        


        
        
       
      </div>
   </div>
  )
}

export default Dashboard