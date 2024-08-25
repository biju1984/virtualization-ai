import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import LoginPage from './pages/LoginPage';
import ProjectPage from './pages/ProjectPage';
import MainLayout from './layouts/MainLayout';

const AppRoutes = () => (
  <Router>
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/projects/:id" element={<ProjectPage />} />
      </Route>
    </Routes>
  </Router>
);

export default AppRoutes;
