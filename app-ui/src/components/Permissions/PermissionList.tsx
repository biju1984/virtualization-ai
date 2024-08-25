import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { setPermissions, selectPermissions } from '../../features/roles/permissionSlice';
import PermissionItem from './PermissionItem';
import { Permission } from '../../types/roleTypes';

const PermissionList: React.FC = () => {
  const dispatch = useDispatch();
  const permissions = useSelector(selectPermissions) as Permission[];

  useEffect(() => {
    const permissionsData: Permission[] = [
      { id: '1', name: 'Read', description: 'Allows read access' },
      { id: '2', name: 'Write', description: 'Allows write access' },
    ];
    dispatch(setPermissions(permissionsData));
  }, [dispatch]);

  return (
    <div>
      <h2>Permission List</h2>
      <ul>
        {permissions.map((permission: Permission) => (
          <PermissionItem key={permission.id} permission={permission} />
        ))}
      </ul>
    </div>
  );
};

export default PermissionList;
