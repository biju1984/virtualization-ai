import api from './api';
import { Role } from '../types/roleTypes';

export const fetchRoles = async (): Promise<Role[]> => {
  const response = await api.get('/roles');
  return response.data;
};

export const createRole = async (role: Role): Promise<Role> => {
  const response = await api.post('/roles', role);
  return response.data;
};

export const updateRole = async (id: string, role: Partial<Role>): Promise<Role> => {
  const response = await api.put(`/roles/${id}`, role);
  return response.data;
};

export const deleteRole = async (id: string): Promise<void> => {
  await api.delete(`/roles/${id}`);
};
