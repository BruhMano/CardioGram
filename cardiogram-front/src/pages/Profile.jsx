import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Header from '../components/Header';
import CardBack from '../components/CardBack';
import ProfileButton from '../components/ProfileButton';
import style from '../assets/static/profile.module.css';
import logout from '../assets/static/logout.png';
import changePassword from '../assets/static/change-password.png';
import editProfile from '../assets/static/edit-account.png';
import deleteProfile from '../assets/static/delete-account.png';

const Profile = () => {
  const [userData, setUserData] = useState({
    username: '',
    first_name: '',
    last_name: '',
    email: '',
  });

  const [progress, setProgress] = useState();
  const [totalAttempts, setTotalAttempts] = useState(0);
  const [totalSuccess, setTotalSuccess] = useState(0);
  const [cards, setCards] = useState([]);

  useEffect(() => {

    axios
      .get('http://127.0.0.1:8000/api/profile/', {withCredentials:true})
      .then(res => setUserData(res.data[0]))
      .catch(err => console.error(err.response?.data || err.message));

    axios
      .get('http://127.0.0.1:8000/api/progress/', { withCredentials: true })
      .then((res) => {
        setProgress(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  useEffect(() => {
    if (progress) {
      const totalAttempts = progress.reduce((sum, item) => sum + item.attempts, 0);
      const totalSuccess = progress.reduce((sum, item) => sum + item.successful_attempts, 0);

      setTotalAttempts(totalAttempts);
      setTotalSuccess(totalSuccess);

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
    <div className={style.profilePage}>
      <Header />

      <div className={style.profile}>
        <div className={style.info}>
          <div className={style.row}>
            <div className={style.personal}>
              <p><b>Имя пользователя:</b> {userData.username}</p>
              <p><b>Имя:</b> {userData.first_name}</p>
              <p><b>Фамилия:</b> {userData.last_name}</p>
              <p><b>Почта:</b> {userData.email}</p>
            </div>
            <div className={style.progress}>
              <b>Карточек на изучении</b><br />
              {progress?.length}
            </div>
          </div>

          <div className={style.row}>
            <div className={style.progress}>
              <b>Прогресс изучения</b><br />
              {Math.round((totalAttempts ? (totalSuccess/ totalAttempts):0)*100)}%
            </div>
            <Link to="/my-cards/">
              <div className={style.myCards}>
                  <b>Мои карточки</b><br />
                  <div className={style.cards}>
                    {cards.slice(0,3).map((card) => (
                      <CardBack
                        title={card?.front_text}
                        translation={card?.back_text}
                        description={card?.example_usage}
                        deck = {card?.deck}
                        showBack = {true}
                        isSmall = {true}
                      />
                    ))}
              </div>
            </div>
            </Link>
          </div>
        </div>

        <div className={style.buttons}>
          <ProfileButton icon={logout} to="logout" label="Выйти" />
          <ProfileButton icon={changePassword} to="change-password" label="Сменить пароль" />
          <ProfileButton icon={editProfile} to="edit-profile" label="Редактировать аккаунт" />
          <ProfileButton icon={deleteProfile} to="delete-profile" label="Удалить аккаунт" />
        </div>
      </div>
    </div>
  );
};

export default Profile;