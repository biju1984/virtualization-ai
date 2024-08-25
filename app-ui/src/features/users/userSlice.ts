import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { User } from "../../types/userTypes";
import { RootState } from "store/rootReducer";

interface UsersState {
  users: User[];
}

const initialState: UsersState = {
  users: [],
};

const userSlice = createSlice({
  name: "users",
  initialState,
  reducers: {
    setUsers: (state, action: PayloadAction<User[]>) => {
      state.users = action.payload;
    },
  },
});

export const { setUsers } = userSlice.actions;
export const selectUsers = (state: RootState) => state.users.users;

export const selectUserById = (userId: string) => (state: RootState) =>
  state.users.users.find((user) => user.id === userId);

export default userSlice.reducer;
