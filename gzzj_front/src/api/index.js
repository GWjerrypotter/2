import request from '@/utils/request'


export function login(username, password) {
  return request({
    url: '/login/',
    method: 'post',
    data: {
      username,
      password
    }
  })
};

export function getInfo(id) {
  return request({
    url: '/users/' + id + '/',
    method: 'get'
  })
};

export function getgzzjlist(params) {
  return request({
    url: "/gzzjlist/",
    method: 'get',
    params: { ordering: '-id', ...params }
  })
};

export function deletegzzj(para) {
  return request({
    url: '/gzzj/' + para,
    method: 'delete',
  })
};

export function addgzzj(para) {
  return request({
    url: '/gzzj/',
    method: 'post',
    data: para,
  })
};

export function editgzzj(id, data) {
  return request({
    url: '/gzzjupdate/' + id + '/',
    method: 'patch',
    data
  })
};

export function getuserlist(params) {
  return request({
    url: "/users/",
    method: 'get',
    params: {ordering: '-id', ...params }
  })
};

export function adduser(para) {
  return request({
    url: '/usersadd/',
    method: 'post',
    data: para,
  })
};

export function updateuser(id, data) {
  return request({
    url: '/usersupdate/' + id + '/',
    method: 'patch',
    data
  })
};

export function userpassword(id, data) {
  return request({
    url: '/userpassword/' + id + '/',
    method: 'patch',
    data
  })
};

export function deleteuser(para) {
  return request({
    url: '/users/' + para,
    method: 'delete',
  })
};