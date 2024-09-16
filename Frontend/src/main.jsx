import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {
  createBrowserRouter,
  RouterProvider,
  Route,
  createRoutesFromElements,
} from "react-router-dom";

import Homepage from './page/Homepage.jsx';
import Login from './Components/Login.jsx';
import Signup from './Components/Signup.jsx';
import Analyzer from './Components/Analyzer.jsx';
import Chatbox from './Components/Chatbox.jsx';
import Settings from './Components/Settings.jsx';
import KnowMore from './Components/KnowMore.jsx';

const router= createBrowserRouter(
  createRoutesFromElements(
    <Route path='/' element={<App/>}>
      <Route path='' element={<Homepage/>}/>
      <Route path='/login' element={<Login/>}/>
      <Route path='/register' element={<Signup/>}/>
      <Route path='/analyze' element={<Analyzer/>}/>
      <Route path='/chat' element={<Chatbox/>}/>
      <Route path='/setting' element={<Settings/>}/>
      <Route path='/know' element={<KnowMore/>}/>
    </Route>
  )
)

createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
