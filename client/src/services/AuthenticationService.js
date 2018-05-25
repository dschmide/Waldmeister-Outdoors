import Api from '@/services/API'

export default {
  register(credentials) {
    return Api().post('/auth/users/create/', credentials)
  },
  login(credentials) {
    return Api().post('/auth/jwt/create/', credentials)
  },
}
