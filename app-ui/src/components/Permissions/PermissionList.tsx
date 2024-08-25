import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchPermissions, selectPermissions } from '../../features/roles/permissionSlice';
import PermissionItem from './PermissionItem';

const PermissionList: React.FC = () => {
  const dispatch = useDispatch();
  const permissions = useSelector(selectPermissions);

  useEffect(() => {
    dispatch(fetchPermissions());
  }, [dispatch]);

  return (
    <div>
      <h2>Permission List</h2>
      <ul>
        {permissions.map((permission) => (
          <PermissionItem key={permission.id} permission={permission} />
        ))}
      </ul>
    </div>
  );
};

export default PermissionList;
