import React from 'react';
import { Outlet } from 'react-router-dom';

const MainLayout: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-blue-600 text-white p-4">
        <h1>Virtualization AI</h1>
      </header>
      <main className="p-4">
        <Outlet />
      </main>
      <footer className="bg-blue-600 text-white p-4 mt-auto">
        <p>&copy; 2024 Virtualization AI</p>
      </footer>
    </div>
  );
};

export default MainLayout;
