import React from 'react';
import RegisterForm from '../features/auth/RegisterForm';

const RegisterPage: React.FC = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded shadow-md">
        <h2 className="text-2xl font-bold mb-6 text-center">Register</h2>
        <RegisterForm />
      </div>
    </div>
  );
};

export default RegisterPage;
