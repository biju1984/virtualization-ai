
import React, { useEffect, useState } from 'react';
import ProjectCard from './ProjectCard';
import { getProjects } from '../../services/projectService';
import { Project } from '../../types/projectTypes';

const ProjectList: React.FC = () => {
  const [projects, setProjects] = useState<Project[]>([]);

  useEffect(() => {
    const fetchProjects = async () => {
      const projectData = await getProjects();
      setProjects(projectData);
    };
    fetchProjects();
  }, []);

  return (
    <div className="project-list">
      {projects.map((project) => (
        <ProjectCard key={project.id} project={project} />
      ))}
    </div>
  );
};

export default ProjectList;

