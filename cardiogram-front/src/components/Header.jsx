import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import profile from '../assets/static/profile.png';
import styles from '../assets/static/home.module.css';
import axios from 'axios';

const Header = () => {
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

  return (
    <header className={styles.header}>
      <Link to="/">
        <div className={styles.logo}>Cardiogram</div>
      </Link>
      <nav className={styles.nav}>
        {isAuthorized ? (
          <Link to="/learn">Учиться</Link>
          ) : ""}
        <Link to="/decks">Колоды</Link>
        {isAuthorized === null ? null : isAuthorized ? (
          <Link to="/profile">
            <button className={styles.button} type="button">
              <img src={profile} alt="Профиль" className={styles.profileImg} />
            </button>
          </Link>
        ) : (
          <Link to="/login">
            <button className={styles.loginButton} type="button">
              Войти
            </button>
          </Link>
        )}
      </nav>
    </header>
  );
};

export default Header;