import axios from 'axios'
import store from '@/store/store'


export default () => {
  var service = {
    baseURL: '/WaldmeisterMap/',
    headers: {}
  }
  console.log(store.state.token)
  if (store.state.token !== null) {
    service.headers.Authorization = `JWT ${store.state.token}`;
  }
  return axios.create(service);
}
