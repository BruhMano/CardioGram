import React from 'react';
import { useNavigate } from 'react-router-dom';
import style from '../assets/static/profile.module.css';
import axios from 'axios';

const ProfileButton = ({ icon, to, label }) => {
  const navigate = useNavigate();

  const handleClick = async () => {
    if (to === 'logout') {
      const isLogout = window.confirm("Вы уверены что хотите выйти из аккаунта?")
      if (isLogout) {
          try {
            await axios.post('http://127.0.0.1:8000/api/auth/logout/', {}, {
              withCredentials: true,
            });
            navigate('/');
          } catch (err) {
            console.error('Ошибка логаута:', err);
            alert('Не удалось выйти из аккаунта');
          }
      }
    }
    else if(to === 'change-password') {
        navigate('/change-password/');
    }
    else if(to === 'edit-profile') {
        navigate('/edit/');
    }
    else if(to === 'delete-profile'){
        const isDelete = window.confirm("Вы уверены что хотите удалить аккаунт? Это нельзя отменить!")
        if (isDelete) {
          axios.delete('http://127.0.0.1:8000/api/delete/', {withCredentials: true})
          .then((res) => {navigate('/');})
          .catch((err) => {console.error(err);})
        }
    }
  };

  return (
    <button className={style.button}>
      <img src={icon} onClick={handleClick} className={style.profileImg} />
    </button>
  );
};

export default ProfileButton;