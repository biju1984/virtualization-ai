
import { Project, Api } from '../types/projectTypes';

let mockProjects: Project[] = [
  {
    id: '1',
    name: 'Visa Installment Service',
    description: 'Mock APIs for Visa Installment Service',
    apis: [
      { id: '1', name: 'Get Installments', endpoint: '/installments', method: 'GET', description: 'Retrieve installment details' },
      { id: '2', name: 'Create Installment', endpoint: '/installments', method: 'POST', description: 'Create a new installment' },
    ],
  },
  // Add more mock projects here
];

export const getProjects = async (): Promise<Project[]> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(mockProjects);
    }, 500);
  });
};

export const getProjectById = async (id: string): Promise<Project | null> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const project = mockProjects.find((p) => p.id === id);
      resolve(project || null);
    }, 500);
  });
};

export const saveApiToProject = async (projectId: string, api: Api): Promise<void> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const projectIndex = mockProjects.findIndex((p) => p.id === projectId);
      if (projectIndex >= 0) {
        mockProjects[projectIndex].apis.push({ ...api, id: `${mockProjects[projectIndex].apis.length + 1}` });
      }
      resolve();
    }, 500);
  });
};

