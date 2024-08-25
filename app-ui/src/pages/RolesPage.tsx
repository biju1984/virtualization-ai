import React from 'react';
import RoleList from '../components/RoleList/RoleList';

const RolesPage: React.FC = () => {
  return (
    <div className="p-8 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Roles</h1>
      <RoleList />
    </div>
  );
};

export default RolesPage;
