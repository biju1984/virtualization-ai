
import React from 'react';
import ApiItem from './ApiItem';
import { Api } from '../../types/projectTypes';

interface ApiListProps {
  apis: Api[];
}

const ApiList: React.FC<ApiListProps> = ({ apis }) => {
  return (
    <div className="api-list">
      <h2>APIs</h2>
      {apis.map(api => (
        <ApiItem key={api.id} api={api} />
      ))}
    </div>
  );
};

export default ApiList;

