import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from '../../store';

interface AuthState {
  user: string | null;
  token: string | null;
  permissions: string[]; // Track user permissions
}

const initialState: AuthState = {
  user: null,
  token: null,
  permissions: [],
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, action: PayloadAction<{ user: string; token: string; permissions: string[] }>) => {
      state.user = action.payload.user;
      state.token = action.payload.token;
      state.permissions = action.payload.permissions;
    },
    logout: (state) => {
      state.user = null;
      state.token = null;
      state.permissions = [];
    },
  },
});

export const { login, logout } = authSlice.actions;
export const selectUser = (state: RootState) => state.auth.user;
export const selectPermissions = (state: RootState) => state.auth.permissions;
export default authSlice.reducer;
