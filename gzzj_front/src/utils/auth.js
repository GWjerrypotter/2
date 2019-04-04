import Cookies from 'js-cookie'

const TokenKey = 'token'

export function getToken() {
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

export function getUsername() {
  return Cookies.get('username')
}

export function setUsername(username) {
  return Cookies.set('username', username)
}

export function removeUsername() {
  return Cookies.remove('username')
}

export function getLoginInfo() {
  let li = null
  if (Cookies.get('li') !== undefined) {
    li = JSON.parse(Cookies.get('li'))
  }
  return li
}

export function setLoginInfo(info) {
  return Cookies.set('li', info)
}

export function removeLoginInfo() {
  return Cookies.remove('li')
}