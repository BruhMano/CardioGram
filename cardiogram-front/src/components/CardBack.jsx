import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styles from '../assets/static/card.module.css';

const CardBack = ({ title, translation, description, showBack, isSmall, deckId }) => {

  const [deckImg, setDeckImg] = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/deck/')
      .then((res) => {
        setDeckImg(res.data.find(deck => deck.id === deckId)?.cover);
      })
      .catch((err) => {
        console.error(err);
      });
  }, [deckId]);

  return (
    <div className={`${styles.cardSpace} ${isSmall ? styles.small:''}`}>
      {showBack ?
        (<div className={`${styles.cardBack} ${isSmall ? styles.small:''}`}>
            <div>
              <p className={styles.title}>{title}</p>
              <p className={styles.subtitle}>{translation}</p>
            </div>
            <div className={`${styles.image} ${isSmall ? styles.small:''}`} style = {{backgroundImage: `url(${deckImg})`}}></div>
            <div>
              <p className={`${styles.desc} ${isSmall ? styles.small:''}`}>{description}</p>
            </div>
        </div>)
        :
        (<div class={styles.cardFront}>{title}</div>)
      }
    </div>
  );
};

export default CardBack;