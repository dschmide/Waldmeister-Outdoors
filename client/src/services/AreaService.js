import Api from '@/services/Api'

export default {
  getAreas(userAreas) {
    return Api().get('/api/areas/')


  },
  postArea(userAreas) {
    return Api().post('/api/areas/', userAreas)


  }
}


/* Example
AuthenticationService.register({
	email: 'testmail@gmail'
})
*/
