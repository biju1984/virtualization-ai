import React from 'react';
import UserList from '../components/UserList/UserList';

const UsersPage: React.FC = () => {
  return (
    <div className="p-8 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Users</h1>
      <UserList />
    </div>
  );
};

export default UsersPage;
