import { useSelector } from 'react-redux';
import { selectUser, selectPermissions } from '../features/auth/authSlice';

const useAuth = () => {
  const user = useSelector(selectUser);
  const permissions = useSelector(selectPermissions);
  const isAuthenticated = Boolean(user);

  return { user, permissions, isAuthenticated };
};

export default useAuth;
