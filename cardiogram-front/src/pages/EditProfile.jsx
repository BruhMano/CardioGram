import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../assets/static/login.css';
import Header from '../components/Header';

const Register = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: '',
    first_name: '',
    last_name: '',
    email: '',
  });

   useEffect(() => {

    axios
      .get('http://127.0.0.1:8000/api/profile/', {withCredentials:true})
      .then(res => {setFormData(res.data[0]); console.log(res.data[0])})
      .catch(err => console.error(err.response?.data || err.message));
  }, []);

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
     .post('http://127.0.0.1:8000/api/auth/edit/', {
        username: formData.username,
        email: formData.email,
        first_name: formData.first_name,
        last_name: formData.last_name
     }, {
         withCredentials: true
     })
     .then((res) => { navigate('/'); })
     .catch((err) => {
        setError('Ошибка обновления данных. Попробуйте снова.');
        setLoading(false);
     });
  };

  return (
    <div className="login-page">
      <Header />
      <h2>Изменить профиль</h2>
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

        {error && <p className="login-error">{error}</p>}

        <button type="submit" className="login-button" disabled={loading}>
          {loading ? 'Загрузка...' : 'Редактировать'}
        </button>
      </form>
    </div>
  );
};

export default Register;