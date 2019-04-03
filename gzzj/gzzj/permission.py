# from rest_framework.permissions import BasePermission
#
#
# class MyPermission(BasePermission):
#     message = '管理员才能访问'
#
#     def has_permission(self, request, view):
#         """
#         自定义权限只有管理员才能访问
#         """
#         # 因为在进行权限判断之前已经做了认证判断，所以这里可以直接拿到request.user
#         if request.user and request.user.groups.values()[0]['name'] == '超级管理员':  # 如果是管理员
#             return True
#         else:
#             return False
