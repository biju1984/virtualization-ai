import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import UserItem from "./UserItem";
import { User } from "types/userTypes";
import { setUsers, selectUsers } from "../../features/users/userSlice";

const UserList: React.FC = () => {
  const dispatch = useDispatch();
  const users = useSelector(selectUsers);

  useEffect(() => {
    // Mock fetching users data
    const usersData = [
      { id: "1", name: "John Doe", email: "john@example.com", roleIds: ["1"] },
      {
        id: "2",
        name: "Jane Smith",
        email: "jane@example.com",
        roleIds: ["2"],
      },
    ];
    dispatch(setUsers(usersData));
  }, [dispatch]);

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map((user: User) => (
          <UserItem key={user.id} user={user} />
        ))}
      </ul>
    </div>
  );
};

export default UserList;
