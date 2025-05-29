import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import styles from '../assets/static/home.module.css';

const LearnButton = () => {
  const [isAuthorized, setIsAuthorized] = useState(null);
  const [isPicked, setIsPicked] = useState(null);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/progress/', { withCredentials: true })
      .then((res) => {
        setIsAuthorized(true);
        setIsPicked(res.data.length > 0);
      })
      .catch(() => {
        setIsAuthorized(false);
        setIsPicked(false);
      });
  }, []);

  return (
    <div className={styles.startBtnDiv}>
      <button className={styles.startBtn}>
        <Link to={isAuthorized ? (isPicked ? '/learn/' : '/cards/') : '/login/'}>
          Вперёд к знаниям!
        </Link>
      </button>
    </div>
  );
};

export default LearnButton;