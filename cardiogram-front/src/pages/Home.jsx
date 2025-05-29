import React from 'react';
import HeroSection from '../components/Hero';
import LearnButton from '../components/LearnButton';
import HowItWorks from '../components/HowItWorks';
import Footer from '../components/Footer';
import styles from '../assets/static/home.module.css';

const Home = () => {
  return (
    <div className={styles.home}>
      <HeroSection />
      <LearnButton />
      <HowItWorks />
      <Footer />
    </div>
  );
};

export default Home;