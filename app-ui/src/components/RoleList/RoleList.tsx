import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchRoles, selectRoles } from '../../features/roles/roleSlice';
import RoleItem from './RoleItem';

const RoleList: React.FC = () => {
  const dispatch = useDispatch();
  const roles = useSelector(selectRoles);

  useEffect(() => {
    dispatch(fetchRoles());
  }, [dispatch]);

  return (
    <div>
      <h2>Role List</h2>
      <ul>
        {roles.map((role) => (
          <RoleItem key={role.id} role={role} />
        ))}
      </ul>
    </div>
  );
};

export default RoleList;
