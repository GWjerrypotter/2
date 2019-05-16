from users.models import Users


def jwt_response_payload_handler(token, Users=None, request=None):
    """为返回的结果添加用户相关信息"""

    return {
        'token': token,
        'user_id': Users.id,
        'username': Users.username,
        'user_name': Users.user_name,
        'dept': Users.dept.dept,
        'dept_id': Users.dept.id,
        'is_manager': Users.is_manager,
    }
