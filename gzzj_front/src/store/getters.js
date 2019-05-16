const getters = {
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  user_name: state => state.user.user_name,
  dept: state => state.user.dept,
  roles: state => state.user.roles,
  username: state => state.user.username,
  userinfo: state => state.user.userinfo,
  logininfo: state => state.user.logininfo,
  addRouters: state => state.permission.addRouters,
  permission_routers: state => state.permission.routers
}
export default getters
