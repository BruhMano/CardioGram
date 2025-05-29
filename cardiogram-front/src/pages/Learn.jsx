import React, { useState, useEffect } from 'react';
import Header from '../components/Header';
import CardBack from '../components/CardBack';
import LeftRightButtons from '../components/LeftRightButtons';
import bg from '../assets/static/cards-background.png';
import axios from 'axios';
import styles from '../assets/static/card.module.css';

const Learn = () => {
  const [cards, setCards] = useState([]);
  const [card, setCard] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showBack, setShowBack] = useState(false);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/progress/', { withCredentials: true })
      .then((res) => {
        setCards(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);
  useEffect(() => {
    if (cards.length && currentIndex !== -1) {
      axios
        .get(`http://127.0.0.1:8000/api/card/${cards[currentIndex].card}/`, { withCredentials: true })
        .then((res) => {
          setCard(res.data);
          setShowBack(false);
        })
        .catch((err) => {
          console.error(err);
        });
    }
  }, [cards, currentIndex]);

  const handleLeft = () => {
    if (currentIndex !== -1) {
      axios
        .patch('http://127.0.0.1:8000/api/progress/right/', { card_id: cards[currentIndex].card }, { withCredentials: true })
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
    if (currentIndex !== -1) {
      axios
        .patch('http://127.0.0.1:8000/api/progress/wrong/', { card_id: cards[currentIndex].card }, { withCredentials: true })
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

  return (
    <div className={styles.cardPage} style={{ backgroundImage: `url(${bg})` }}>
      <Header />
      <LeftRightButtons
        leftFunc={showBack ? handleLeft: () => {setShowBack(true)}}
        rightFunc={showBack ? handleRight: () => {setShowBack(true)}}
      />
        {currentIndex !== -1 ? (
          <CardBack
            title={card?.front_text}
            translation={card?.back_text}
            description={card?.example_usage}
            showBack={showBack}
            isSmall = {false}
            deckId = {card?.deck}
          />
        ) : (
          <p>Карточки закончились! Можете набрать новых или отдохнуть)</p>
        )}
      </div>
  );
};

export default Learn;