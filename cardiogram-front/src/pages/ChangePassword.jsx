import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../assets/static/login.css';

const ChangePassword = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    old_password: '',
    new_password: ''
  });

  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    axios.post(
        'http://127.0.0.1:8000/api/auth/change-password/',
        {
          old_password: formData.old_password,
          new_password: formData.new_password
        },
        {
          withCredentials: true
        }
    )
    .then((res) => { navigate('/profile'); })
    .catch((err) => {
        setError('Ошибка смены пароля!');
        setLoading(false);
    });
  };

  return (
    <div className="login-page">
      <h2>Сменить пароль</h2>
      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="password"
          name="old_password"
          placeholder="Старый пароль"
          value={formData.old_password}
          onChange={handleChange}
          required
          className="login-input"
        />

        <input
          type="password"
          name="new_password"
          placeholder="Новый пароль"
          value={formData.new_password}
          onChange={handleChange}
          required
          className="login-input"
        />

        {error && <p className="login-error">{error}</p>}

        <button
          type="submit"
          disabled={loading}
          className="login-button"
        >
          {loading ? 'Загрузка...' : 'Сменить пароль'}
        </button>
      </form>

      <p className="login-register-prompt">
        <a href="/profile">← Вернуться в профиль</a>
      </p>
    </div>
  );
};

export default ChangePassword;