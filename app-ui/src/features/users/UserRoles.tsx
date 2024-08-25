import React from 'react';
import { useSelector } from 'react-redux';
import { selectRoles } from '../roles/roleSlice';

interface UserRolesProps {
  userId: string;
}

const UserRoles: React.FC<UserRolesProps> = ({ userId }) => {
  const roles = useSelector(selectRoles);

  const handleRoleChange = (roleId: string) => {
    // Handle role assignment
  };

  return (
    <div>
      <h3>Assign Roles</h3>
      <ul>
        {roles.map((role) => (
          <li key={role.id}>
            <input
              type="checkbox"
              onChange={() => handleRoleChange(role.id)}
            />
            {role.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserRoles;
