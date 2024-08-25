import React from 'react';
import { Role } from '../../types/roleTypes';

interface RoleItemProps {
  role: Role;
}

const RoleItem: React.FC<RoleItemProps> = ({ role }) => {
  return (
    <li>{role.name}</li>
  );
};

export default RoleItem;
