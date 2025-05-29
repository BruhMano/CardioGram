import React from 'react';
import im1 from '../assets/static/im1.png';
import im2 from '../assets/static/im2.png';
import im3 from '../assets/static/im3.png';
import im4 from '../assets/static/im4.png';
import styles from '../assets/static/home.module.css';

const HowItWorks = () => {
  return (
    <section className={styles.howItWorks}>
      <h2>Как это работает?</h2>
      <div className={styles.guideLine}>
        <p className={styles.guideText}>
          1. Набери себе карточек со словами для изучения из тематических колод
        </p>
        <img src={im1} alt="" />
      </div>
      <div className={styles.guideLine}>
        <img src={im2} alt="" />
        <p className={styles.guideText}>
          2. Мы покажем тебе одну сторону карточки, а ты попытайся вспомнить,
          что на обратной стороне
        </p>
      </div>
      <div className={styles.guideLine}>
        <p className={styles.guideText}>
          3. Кликни на карточку и узнай правильный ответ
        </p>
        <img src={im3} alt="" />
      </div>
      <div className={styles.guideLine}>
        <img src={im4} alt="" />
        <div className={styles.guideText}>
          <p>4. Проверь себя</p>
          <div className={styles.checkList}>
            <p>4.1. Нажми на правую сторону экрана, если все правильно вспомнил</p>
            <p>4.2. Нажми на левую сторону экрана, если ошибся</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;