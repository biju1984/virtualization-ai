import React from 'react';
import { Outlet } from 'react-router-dom';

const AdminLayout: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-gray-800 text-white p-4">
        <h1>Admin Dashboard</h1>
      </header>
      <main className="flex-grow p-4 bg-gray-100">
        <Outlet />
      </main>
      <footer className="bg-gray-800 text-white p-4">
        <p>&copy; 2024 Virtualization AI - Admin Panel</p>
      </footer>
    </div>
  );
};

export default AdminLayout;
