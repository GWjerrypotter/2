import { login } from '@/api/index'
import { getToken, setToken, removeToken, getUsername, setUsername, removeUsername, setLoginInfo, getLoginInfo, removeLoginInfo } from '@/utils/auth'

const BASE = '@'
const user = {
    state: {
        logininfo: getLoginInfo(),
        token: getToken(),
        username: getUsername(),
        userinfo: undefined,
        user_name: '',
        dept: '',
        isLogin: undefined,
    },

    mutations: {
        SET_TOKEN: (state, token) => {
            state.token = token
        },
        SET_USERNAME: (state, username) => {
            state.username = username
        },
        SET_USER_NAME: (state, user_name) => {
            state.user_name = user_name
        },
        SET_DEPT: (state, dept) => {
            state.dept = dept
        },
        SET_USERINFO: (state, userinfo) => {
            state.userinfo = userinfo
        },
        SET_LOGININFO: (state, logininfo) => {
            state.logininfo = logininfo
        },
    },

    actions: {
        Login({ commit }, userInfo) {
            const username = userInfo.username.trim()
            return new Promise((resolve, reject) => {
                login(username, userInfo.password).then(response => {
                    const data = response
                    console.log(data)
                    setToken(data.token)
                    setUsername(username)
                    setLoginInfo(data)
                    commit('SET_TOKEN', data.token)
                    commit('SET_USERNAME', username)
                    commit('SET_LOGININFO', data)
                    commit('SET_DEPT', data.dept)
                    resolve()
                }).catch(error => {
                    console.log(error)
                    reject(error)
                })
            })
        },

        // 获取用户信息
        GetInfo({ commit, state }) {
            return new Promise((resolve, reject) => {
                getInfo(state.logininfo.user_id).then(response => {
                    const data = response
                    // console.log(data)
                    // if (data.department.length) {
                    //   // commit('SET_ROLES', data.department)
                    // } else {
                    //   reject('getInfo: roles must be a non-null array !')
                    // }
                    commit('SET_USERINFO', data)
                    commit('SET_USER_NAME', data.user_name)
                    commit('SET_DEPT', data.dept)
                    
                    // commit('SET_AVATAR', data.avatar)
                    resolve(response)
                }).catch(error => {
                    reject(error)
                })
            })
        },

        Logout({ commit }) {
            return new Promise((resolve) => {
                commit('SET_TOKEN', '')
                commit('SET_USERNAME', '')
                commit('SET_USERINFO', '')
                commit('SET_LOGININFO', '')
                commit('SET_DEPT', '')
                commit('SET_USER_NAME', '')
                removeToken()
                removeUsername()
                removeLoginInfo()
                resolve()
            })
        }
    }
}

export default user