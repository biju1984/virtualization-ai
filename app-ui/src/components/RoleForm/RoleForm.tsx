import React from 'react';
import { useForm } from 'react-hook-form';
import { Role } from '../../types/roleTypes';

interface RoleFormProps {
  onSubmit: (data: Role) => void;
  defaultValues?: Partial<Role>;
}

const RoleForm: React.FC<RoleFormProps> = ({ onSubmit, defaultValues }) => {
  const { register, handleSubmit } = useForm<Role>({
    defaultValues,
  });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>
        Role Name:
        <input {...register('name', { required: true })} />
      </label>
      {/* Additional fields for permissions */}
      <button type="submit">Submit</button>
    </form>
  );
};

export default RoleForm;
