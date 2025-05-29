import React, { useState, useEffect } from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import Header from '../components/Header';
import CardBack from '../components/CardBack';
import style from '../assets/static/card.module.css';
import axios from 'axios';

const MyCards = () => {
    const [progress, setProgress] = useState([]);
    const [cards, setCards] = useState([]);

    useEffect(() => {
        axios
          .get('http://127.0.0.1:8000/api/progress/', { withCredentials: true })
          .then((res) => {
            setProgress(res.data);
            console.log(progress);
          })
          .catch((err) => {
            console.error(err);
          });
    }, []);

    useEffect(() => {
      if (progress.length) {
        progress.forEach(progressRecord => {
          axios
            .get(`http://127.0.0.1:8000/api/card/${progressRecord.card}/`, { withCredentials: true })
            .then((res) => {
              setCards(prev => [...prev, res.data]);
            })
            .catch((err) => {
              console.error(err);
            });
        });
      }
    }, [progress]);

  return (
    <div className={style.cardPage}>
      <Header />
      <Swiper
        slidesPerView={3}
        centeredSlides={true}
        spaceBetween={30}
        grabCursor={true}
        loop={true}
        className="swiper"
      >
        {cards.map(card => (
          <SwiperSlide>
            <CardBack
                title={card?.front_text}
                translation={card?.back_text}
                description={card?.example_usage}
                deckId = {card?.deck}
                showBack = {true}
                isSmall = {false}
            />
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};

export default MyCards;