import React, { useEffect, useState } from 'react';
import { useParams, Navigate } from 'react-router-dom';
import ApiList from './ApiList';
import { getProjectById } from '../../services/projectService';
import { Project } from '../../types/projectTypes';

const ProjectDetails: React.FC = () => {
  const { projectId } = useParams<{ projectId: string }>();
  const [project, setProject] = useState<Project | null>(null);

  useEffect(() => {
    if (!projectId) {
      // If projectId is undefined, you could redirect to a different page or handle it as needed
      return;
    }

    const fetchProject = async () => {
      const projectData = await getProjectById(projectId);
      setProject(projectData);
    };

    fetchProject();
  }, [projectId]);

  if (!project) {
    // Handle loading or error state
    return <div>Loading...</div>;
  }

  return (
    <div className="project-details">
      <h1>{project.name}</h1>
      <p>{project.description}</p>
      <ApiList apis={project.apis} />
    </div>
  );
};

export default ProjectDetails;
