import React from 'react';
import { useSelector } from 'react-redux';
import { selectUser } from '../auth/authSlice';

const UserProfile: React.FC = () => {
  const user = useSelector(selectUser);

  if (!user) {
    return <div>No user logged in</div>;
  }

  return (
    <div>
      <h2>User Profile</h2>
      <p>Name: {user.name}</p>
      <p>Email: {user.email}</p>
      {/* Add fields to edit profile */}
    </div>
  );
};

export default UserProfile;
