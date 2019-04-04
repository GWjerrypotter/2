const getters = {
  token: state => state.user.token,
  avatar: state => state.user.avatar,
  user_name: state => state.user.user_name,
  username: state => state.user.username,
  userinfo: state => state.user.userinfo,
  logininfo: state => state.user.logininfo,
}
export default getters
