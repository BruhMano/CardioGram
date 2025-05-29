import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Decks from './pages/Decks';
import Cards from './pages/Cards';
import Learn from './pages/Learn';
import Profile from './pages/Profile';
import MyCards from './pages/MyCards';
import Login from './pages/Login';
import Signup from './pages/Signup';
import ChangePassword from './pages/ChangePassword';
import EditProfile from './pages/EditProfile';
import axios from 'axios';

const App = () => {
  axios.defaults.withCredentials = true;

  return (
    <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/decks" element={<Decks />} />
          <Route path="/deck/:deckId" element={<Cards />} />
          <Route path="/learn" element={<Learn />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/my-cards" element={<MyCards />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/change-password" element={<ChangePassword />} />
          <Route path="/edit" element={<EditProfile />} />
        </Routes>
    </Router>
  );
}


export default App;