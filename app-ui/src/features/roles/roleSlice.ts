import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Role } from '../../types/roleTypes';
import { RootState } from 'store/rootReducer';

interface RolesState {
  roles: Role[];
  loading: boolean;
}

const initialState: RolesState = {
  roles: [],
  loading: false,
};

const roleSlice = createSlice({
  name: 'roles',
  initialState,
  reducers: {
    setRoles: (state, action: PayloadAction<Role[]>) => {
      state.roles = action.payload;
      state.loading = false;
    },
    addRole: (state, action: PayloadAction<Role>) => {
      state.roles.push(action.payload);
    },
    removeRole: (state, action: PayloadAction<string>) => {
      state.roles = state.roles.filter(role => role.id !== action.payload);
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    },
  },
});

export const { setRoles, addRole, removeRole, setLoading } = roleSlice.actions;
export const selectRoles = (state: RootState) => state.roles.roles;
export const selectLoading = (state: RootState) => state.roles.loading;
export default roleSlice.reducer;
