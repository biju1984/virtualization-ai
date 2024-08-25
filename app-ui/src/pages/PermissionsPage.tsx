import React from 'react';
import PermissionList from '../components/Permissions/PermissionList';

const PermissionsPage: React.FC = () => {
  return (
    <div className="p-8 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Permissions</h1>
      <PermissionList />
    </div>
  );
};

export default PermissionsPage;
