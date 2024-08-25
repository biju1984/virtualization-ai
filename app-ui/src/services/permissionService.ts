import api from './api';
import { Permission } from '../types/roleTypes';

export const fetchPermissions = async (): Promise<Permission[]> => {
  const response = await api.get('/permissions');
  return response.data;
};

export const createPermission = async (permission: Permission): Promise<Permission> => {
  const response = await api.post('/permissions', permission);
  return response.data;
};

export const updatePermission = async (id: string, permission: Partial<Permission>): Promise<Permission> => {
  const response = await api.put(`/permissions/${id}`, permission);
  return response.data;
};

export const deletePermission = async (id: string): Promise<void> => {
  await api.delete(`/permissions/${id}`);
};
