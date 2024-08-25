
export interface Api {
  id: string;
  name: string;
  endpoint: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  description?: string;
}

export interface Project {
  id: string;
  name: string;
  description: string;
  apis: Api[];
}

