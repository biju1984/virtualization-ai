
import React from 'react';
import { Link } from 'react-router-dom';
import { Project } from '../../types/projectTypes';

interface ProjectCardProps {
  project: Project;
}

const ProjectCard: React.FC<ProjectCardProps> = ({ project }) => {
  return (
    <div className="project-card">
      <h3>{project.name}</h3>
      <p>{project.description}</p>
      <Link to={`/projects/${project.id}`}>View Project</Link>
    </div>
  );
};

export default ProjectCard;

