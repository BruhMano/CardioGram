import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../assets/static/login.css';

const Register = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: '',
    first_name: '',
    last_name: '',
    email: '',
    password: '',
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

     axios
     .post('http://127.0.0.1:8000/api/auth/register/', {
        username: formData.username,
        email: formData.email,
        password: formData.password,
        first_name: formData.first_name,
        last_name: formData.last_name
     }, {
         withCredentials: true
     })
     .then((res) => { navigate('/'); })
     .catch((err) => {
        setError('Ошибка регистрации. Попробуйте снова.');
        setLoading(false);
     });
  };

  return (
    <div className="login-page">
      <h2>Регистрация</h2>
      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="text"
          name="username"
          placeholder="Логин"
          value={formData.username}
          onChange={handleChange}
          required
          className="login-input"
        />

        <input
          type="text"
          name="first_name"
          placeholder="Имя"
          value={formData.first_name}
          onChange={handleChange}
          required
          className="login-input"
        />

        <input
          type="text"
          name="last_name"
          placeholder="Фамилия"
          value={formData.last_name}
          onChange={handleChange}
          required
          className="login-input"
        />

        <input
          type="email"
          name="email"
          placeholder="Эл. почта"
          value={formData.email}
          onChange={handleChange}
          required
          className="login-input"
        />

        <input
          type="password"
          name="password"
          placeholder="Пароль"
          value={formData.password}
          onChange={handleChange}
          required
          className="login-input"
        />

        {error && <p className="login-error">{error}</p>}

        <button type="submit" className="login-button" disabled={loading}>
          {loading ? 'Загрузка...' : 'Зарегистрироваться'}
        </button>
      </form>

      <p className="register-prompt">
        Уже есть аккаунт?{' '}
        <a href="/login">Войдите</a>
      </p>
    </div>
  );
};

export default Register;