import Api from '@/services/API'

export default {
  getAreas() {
    return Api().get('/api/areas/')
  },
  postArea(userAreas) {
    return Api().post('/api/areas/', userAreas)
  },
  deleteArea(id) {
    return Api().delete('/api/areas/' + id)
  },
  updateArea(userAreas, id) {
    return Api().update('/api/areas/' + id, userAreas)
  }
}


/* Example
AuthenticationService.register({
	email: 'testmail@gmail'
})
*/
