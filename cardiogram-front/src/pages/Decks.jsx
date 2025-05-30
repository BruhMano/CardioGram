import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import axios from 'axios';
import { Link } from 'react-router-dom';
import style from '../assets/static/decks.module.css';

function Decks() {

  const [decks, setDecks] = useState([]);
  const [isAuthorized, setIsAuthorized] = useState(null);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/progress/', { withCredentials: true })
      .then((res) => {
        setIsAuthorized(true);
      })
      .catch(() => {
        setIsAuthorized(false);
      });
  }, []);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/deck/')
      .then((res) => {
        setDecks(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  return (
    <div className={style.home}>
      <Header />
      {decks.map((deck, index) => (
        <div className={style.deck} key={deck.id}>
          <Link to={isAuthorized ? `/deck/${deck.id}/`: '/'} >
            <img src={deck.cover} alt={deck.title} />
          </Link>
          <div className={style.desc}>
            <p>{deck.name}</p>
            <p>{deck.description}</p>
          </div>
        </div>
          ))}
    </div>
  );
}

export default Decks;