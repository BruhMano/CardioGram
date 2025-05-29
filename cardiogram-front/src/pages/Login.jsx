import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../assets/static/login.css';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });

  const navigate = useNavigate();

  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    axios
      .post('http://127.0.0.1:8000/api/auth/login/', formData, {withCredentials: true})
      .then((res) => { navigate('/'); })
      .catch((err) => {
        setError('Ошибка входа. Неверные логин или пароль.');
        setLoading(false);
      });
  };

  return (
    <div className="login-page">
      <h2>Вход</h2>
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
          type="password"
          name="password"
          placeholder="Пароль"
          value={formData.password}
          onChange={handleChange}
          required
          className="login-input"
        />
        {error && <p className="login-error">{error}</p>}
        <button type="submit" disabled={loading} className="login-button">
          {loading ? 'Загрузка...' : 'Войти'}
        </button>
      </form>

      <p className="login-register-prompt">
        Нет аккаунта?{' '}
        <Link to="/signup">Зарегистрируйтесь</Link>
      </p>
    </div>
  );
};

export default Login;