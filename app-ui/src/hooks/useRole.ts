import { useSelector } from 'react-redux';
import { selectRoles } from '../features/roles/roleSlice';
import { selectPermissions } from '../features/roles/permissionSlice';

const useRole = () => {
  const roles = useSelector(selectRoles);
  const permissions = useSelector(selectPermissions);

  return { roles, permissions };
};

export default useRole;
