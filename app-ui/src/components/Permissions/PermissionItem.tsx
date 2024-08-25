import React from 'react';
import { Permission } from '../../types/roleTypes';

interface PermissionItemProps {
  permission: Permission;
}

const PermissionItem: React.FC<PermissionItemProps> = ({ permission }) => {
  return (
    <li>{permission.name}</li>
  );
};

export default PermissionItem;
