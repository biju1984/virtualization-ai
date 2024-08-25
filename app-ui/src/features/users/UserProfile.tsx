import { useSelector } from 'react-redux';
import { selectUserById } from '../../features/users/userSlice';
import { User } from '../../types/userTypes';

const UserProfile: React.FC<{ userId: string }> = ({ userId }) => {
  const user = useSelector(selectUserById(userId)) as User | null;

  if (!user) {
    return <div>No user logged in</div>;
  }

  return (
    <div>
      <h1>{user.name}</h1>
      <p>Email: {user.email}</p>
      {/* Other user details */}
    </div>
  );
};
