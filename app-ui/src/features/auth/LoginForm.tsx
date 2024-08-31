import React from "react";
import { useForm } from "react-hook-form";
import { useDispatch } from "react-redux";
import { login } from "./authSlice";
import { useAppDispatch } from "hooks/useAppDispatch";

interface LoginFormData {
  email: string;
  password: string;
}

const LoginForm: React.FC = () => {
  const { register, handleSubmit } = useForm<LoginFormData>();
  const dispatch = useAppDispatch();

  const onSubmit = (data: LoginFormData) => {
    dispatch(login({ username: data.email, password: data.password }));
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>
        Email:
        <input {...register("email", { required: true })} />
      </label>
      <label>
        Password:
        <input type="password" {...register("password", { required: true })} />
      </label>
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;
