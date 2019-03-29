import request from '@/utils/request'

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

export function getuserlist() {
  return request({
    url: "/users/?page_size=10",
    method: 'get',
  })
};

// export function checkgzzj(para) {
//   return request({
//     url: '/gzzjlist/' + para,
//     method: 'get',
//   })
// };