import React from 'react';

const AdminDashboard: React.FC = () => {
  return (
    <div className="p-8 bg-gray-100">
      <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="p-4 bg-white rounded shadow-md">
          <h2 className="text-xl font-bold">Manage Users</h2>
          <p>View, add, edit, and delete users.</p>
        </div>
        <div className="p-4 bg-white rounded shadow-md">
          <h2 className="text-xl font-bold">Manage Roles</h2>
          <p>View, add, edit, and delete roles.</p>
        </div>
        <div className="p-4 bg-white rounded shadow-md">
          <h2 className="text-xl font-bold">Manage Permissions</h2>
          <p>View, add, edit, and delete permissions.</p>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
