import React, { useState } from 'react';
import { Api } from '../../types/projectTypes';

interface ApiFormProps {
  onSave: (api: Api) => void;
}

const ApiForm: React.FC<ApiFormProps> = ({ onSave }) => {
  const [api, setApi] = useState<Api>({
    id: '',
    name: '',
    endpoint: '',
    method: 'GET',
    description: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    setApi({
      ...api,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSave(api);
    setApi({ id: '', name: '', endpoint: '', method: 'GET', description: '' });
  };

  return (
    <form onSubmit={handleSubmit} className="api-form">
      <input
        type="text"
        name="name"
        value={api.name}
        onChange={handleChange}
        placeholder="API Name"
        required
      />
      <input
        type="text"
        name="endpoint"
        value={api.endpoint}
        onChange={handleChange}
        placeholder="Endpoint"
        required
      />
      <select name="method" value={api.method} onChange={handleChange}>
        <option value="GET">GET</option>
        <option value="POST">POST</option>
        <option value="PUT">PUT</option>
        <option value="DELETE">DELETE</option>
      </select>
      <textarea
        name="description"
        value={api.description}
        onChange={handleChange}
        placeholder="Description"
      />
      <button type="submit">Save API</button>
    </form>
  );
};

export default ApiForm;
