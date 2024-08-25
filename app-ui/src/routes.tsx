import React from "react";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import AuthLayout from "./layouts/AuthLayout";
import AdminLayout from "./layouts/AdminLayout";

import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import UsersPage from "./pages/UsersPage";
import RolesPage from "./pages/RolesPage";
import PermissionsPage from "./pages/PermissionsPage";
import AdminDashboard from "./pages/AdminDashboard";
import DashboardPage from "./pages/DashboardPage";
import ProjectDetailsPage from "./pages/ProjectDetailsPage";
import useAuth from './hooks/useAuth';

// Private Route component to restrict access based on authentication
const PrivateRoute = ({ children }: { children: JSX.Element }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
};

// Admin Route component to restrict access based on role
const AdminRoute = ({ children }: { children: JSX.Element }) => {
  const { user, permissions } = useAuth();
  const isAdmin = user && permissions.includes("admin");
  return isAdmin ? children : <Navigate to="/" />;
};

const AppRoutes: React.FC = () => {
  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route path="/" element={<MainLayout />}>
          <Route path="login" element={<LoginPage />} />
          <Route path="register" element={<RegisterPage />} />
        </Route>

        {/* Private Routes */}
        <Route
          path="/admin"
          element={
            <PrivateRoute>
              <AdminLayout />
            </PrivateRoute>
          }
        >
          <Route
            path="dashboard"
            element={
              <AdminRoute>
                <AdminDashboard />
              </AdminRoute>
            }
          />
          <Route
            path="users"
            element={
              <AdminRoute>
                <UsersPage />
              </AdminRoute>
            }
          />
          <Route
            path="roles"
            element={
              <AdminRoute>
                <RolesPage />
              </AdminRoute>
            }
          />
          <Route
            path="permissions"
            element={
              <AdminRoute>
                <PermissionsPage />
              </AdminRoute>
            }
          />
        </Route>

        {/* Project Management Routes */}
        <Route
          path="/projects"
          element={
            <PrivateRoute>
              <MainLayout />
            </PrivateRoute>
          }
        >
          <Route
            path=""
            element={
              <PrivateRoute>
                <DashboardPage />
              </PrivateRoute>
            }
          />
          <Route
            path=":projectId"
            element={
              <PrivateRoute>
                <ProjectDetailsPage />
              </PrivateRoute>
            }
          />
        </Route>
      </Routes>
    </Router>
  );
};

export default AppRoutes;
