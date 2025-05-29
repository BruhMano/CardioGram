import React, { useState, useEffect } from 'react';
import Header from './Header';
import axios from 'axios';
import styles from '../assets/static/home.module.css';

const Hero = () => {
  const [decks, setDecks] = useState([]);

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
    <section className={styles.hero}>
      <Header />
      <h1>CardioGram</h1>
      <p>увлекательная игра для запоминания английских слов с помощью карточек</p>

      <div id="myCarousel" className={`${styles.carousel} carousel slide`} data-bs-ride="carousel" data-bs-interval="3000">
        <div className="carousel-inner">
          {decks.map((deck, index) => (
            <div
              className={`carousel-item${index === 0 ? ' active' : ''}`}
              key={deck.id}
            >
              <img src={deck.cover} alt={deck.id} />
            </div>
          ))}
        </div>
      </div>

      <p className={styles.subtext}>
        каждая колода превращает обучение в захватывающий и эффективный процесс
      </p>
    </section>
  );
};

export default Hero;