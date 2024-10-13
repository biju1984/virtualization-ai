from app.models.user import User
from app.models.project import Project


def can_access_project(user: User, project: Project) -> bool:
    """
    Check if the user has access to the specified project.

    Parameters:
    - user (User): The user object of the current authenticated user.
    - project (Project): The project object to check access against.

    Returns:
    - bool: True if the user can access the project, False otherwise.
    """

    # Super Admins can access all projects
    if user.role.name == "super_admin":
        return True

    # Admins can access all projects
    if user.role.name == "admin":
        return True

    # Regular users can only access their own projects
    if user.id == project.user_id:
        return True

    # Implement additional custom logic if necessary
    # For example, checking specific permissions
    if "view_project" in [perm.name for perm in user.role.permissions]:
        return True

    # If none of the above conditions are met, deny access
    return False
