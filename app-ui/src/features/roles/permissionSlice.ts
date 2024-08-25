import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Permission } from '../../types/roleTypes';
import { RootState } from 'store/rootReducer';

interface PermissionsState {
  permissions: Permission[];
  loading: boolean;
}

const initialState: PermissionsState = {
  permissions: [],
  loading: false,
};

const permissionSlice = createSlice({
  name: 'permissions',
  initialState,
  reducers: {
    setPermissions: (state, action: PayloadAction<Permission[]>) => {
      state.permissions = action.payload;
    },
    addPermission: (state, action: PayloadAction<Permission>) => {
      state.permissions.push(action.payload);
    },
    removePermission: (state, action: PayloadAction<string>) => {
      state.permissions = state.permissions.filter(permission => permission.id !== action.payload);
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    },
  },
});

export const { setPermissions, addPermission, removePermission, setLoading } = permissionSlice.actions;
export const selectPermissions = (state: RootState) => state.permissions.permissions;
export const selectLoading = (state: RootState) => state.permissions.loading;
export default permissionSlice.reducer;
