import React from 'react';
import styles from '../assets/static/home.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.refreshIconDiv}>
        <button className={styles.refreshIcon}>&#8635;</button>
      </div>
      <p className={styles.footerText}>
        Ec/\N 4т0-т0 HE P4б0T4ET 0cT4BbTe >|{'<'}4/\0bY 3AECb:
        <br />
        <a href="https://github.com/BruhMano/CardioGram/issues ">
          https://github.com/BruhMano/CardioGram/issues
        </a>
      </p>
    </footer>
  );
};

export default Footer;