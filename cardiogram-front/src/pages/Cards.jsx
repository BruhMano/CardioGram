import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../components/Header';
import CardBack from '../components/CardBack';
import LeftRightButtons from '../components/LeftRightButtons';
import bg from '../assets/static/card-pick-background2.png';
import axios from 'axios';
import styles from '../assets/static/card.module.css';

const Cards = () => {
  const { deckId } = useParams();
  const [cards, setCards] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/deck/${deckId}/`, { withCredentials: true })
      .then((res) => {
        setCards(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, [deckId]);

  const handleLeft = () => {
    if (currentIndex !== -1 && cards.length) {
      axios
        .post('http://127.0.0.1:8000/api/progress/', { card: cards[currentIndex].id }, { withCredentials: true })
        .then(() => {})
        .catch((err) => {
          console.error(err);
        });
    }

    if (currentIndex < cards.length - 1 && currentIndex !== -1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setCurrentIndex(-1);
    }
  };

  const handleRight = () => {
    if (currentIndex < cards.length - 1 && currentIndex !== -1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setCurrentIndex(-1);
    }
  };

  return (
    <div className={styles.cardPage} style={{ backgroundImage: `url(${bg})` }}>
      <Header />
      <LeftRightButtons leftFunc={handleLeft} rightFunc={handleRight} />
        {currentIndex !== -1 && cards.length ? (
          <CardBack
            title={cards[currentIndex]?.front_text}
            translation={cards[currentIndex]?.back_text}
            description={cards[currentIndex]?.example_usage}
            deckId = {cards[currentIndex]?.deck}
            showBack = {true}
            isSmall = {false}
          />
        ) : (
          <p>Карточки в колоде закончились! Можете уже пойти поучиться)</p>
        )}
      </div>
  );
};

export default Cards;