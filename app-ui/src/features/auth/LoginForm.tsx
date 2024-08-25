import React from 'react';
import { useForm } from 'react-hook-form';
import { useDispatch } from 'react-redux';
import { login } from './authSlice';

interface LoginFormData {
  email: string;
  password: string;
}

const LoginForm: React.FC = () => {
  const { register, handleSubmit } = useForm<LoginFormData>();
  const dispatch = useDispatch();

  const onSubmit = (data: LoginFormData) => {
    // Call login API and dispatch login action
    dispatch(login({ user: data.email, token: 'fake-jwt-token', permissions: [] }));
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>
        Email:
        <input {...register('email', { required: true })} />
      </label>
      <label>
        Password:
        <input type="password" {...register('password', { required: true })} />
      </label>
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
