import React from 'react';
import { useForm } from 'react-hook-form';

interface RegisterFormData {
  name: string;
  email: string;
  password: string;
}

const RegisterForm: React.FC = () => {
  const { register, handleSubmit } = useForm<RegisterFormData>();

  const onSubmit = (data: RegisterFormData) => {
    // Call register API and handle user registration
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>
        Name:
        <input {...register('name', { required: true })} />
      </label>
      <label>
        Email:
        <input {...register('email', { required: true })} />
      </label>
      <label>
        Password:
        <input type="password" {...register('password', { required: true })} />
      </label>
      <button type="submit">Register</button>
    </form>
  );
};

export default RegisterForm;
