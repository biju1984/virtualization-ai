
import React from 'react';
import { Api } from '../../types/projectTypes';

interface ApiItemProps {
  api: Api;
}

const ApiItem: React.FC<ApiItemProps> = ({ api }) => {
  return (
    <div className="api-item">
      <h3>{api.name}</h3>
      <p>{api.endpoint}</p>
      <p>{api.method}</p>
      <p>{api.description}</p>
    </div>
  );
};

export default ApiItem;

