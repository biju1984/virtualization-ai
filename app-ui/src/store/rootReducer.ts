import { combineReducers } from '@reduxjs/toolkit';
import authReducer from '../features/auth/authSlice';
import userReducer from '../features/users/userSlice';
import roleReducer from '../features/roles/roleSlice';
import permissionReducer from '../features/roles/permissionSlice'; // Ensure this import is correct

const rootReducer = combineReducers({
  auth: authReducer,
  users: userReducer,
  roles: roleReducer,
  permissions: permissionReducer,
});

export type RootState = ReturnType<typeof rootReducer>;
export default rootReducer;
