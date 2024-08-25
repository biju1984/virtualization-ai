import React from 'react';
import { Outlet } from 'react-router-dom';

const AuthLayout: React.FC = () => {
  return (
    <div className="flex justify-center items-center h-screen bg-blue-100">
      <div className="w-full max-w-md p-8 bg-white rounded shadow-md">
        <Outlet />
      </div>
    </div>
  );
};

export default AuthLayout;
