import React from 'react';
import { User } from '../../types/userTypes';

interface UserItemProps {
  user: User;
}

const UserItem: React.FC<UserItemProps> = ({ user }) => {
  return (
    <li>{user.name} - {user.email}</li>
  );
};

export default UserItem;
