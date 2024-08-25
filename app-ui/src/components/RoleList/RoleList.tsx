import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { setRoles, selectRoles } from "../../features/roles/roleSlice";
import RoleItem from "./RoleItem";
import { Role } from "types/roleTypes";

const RoleList: React.FC = () => {
  const dispatch = useDispatch();
  const roles = useSelector(selectRoles);

  useEffect(() => {
    // Mock fetching roles data
    const rolesData = [
      {
        id: "1",
        name: "Admin",
        permissions: ["create", "read", "update", "delete"],
      },
      { id: "2", name: "User", permissions: ["read"] },
    ];
    dispatch(setRoles(rolesData));
  }, [dispatch]);

  return (
    <div>
      <h2>Role List</h2>
      <ul>
        {roles.map((role: Role) => (
          <RoleItem key={role.id} role={role} />
        ))}
      </ul>
    </div>
  );
};

export default RoleList;
