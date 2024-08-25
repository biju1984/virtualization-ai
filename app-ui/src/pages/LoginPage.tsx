import React from 'react';
import LoginForm from '../features/auth/LoginForm';

const LoginPage: React.FC = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 bg-white rounded shadow-md">
        <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>
        <LoginForm />
      </div>
    </div>
  );
};

export default LoginPage;
