import Api from 'services/api';

export interface LoginResponse {
  user: string;
  token: string;
  permissions: string[];
}

export const loginUser = async (username: string, password: string): Promise<LoginResponse> => {
    const response = await Api.post<LoginResponse>('user/login', { username, password });
    return response.data; // Return the actual data, not the whole AxiosResponse object
  };
