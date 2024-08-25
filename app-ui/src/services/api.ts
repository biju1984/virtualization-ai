import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api',
});

export const fetchProjects = () => api.get('/projects');

export const createProject = (project: any) => api.post('/projects', project);

export default api;
