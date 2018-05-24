import Api from '@/services/API'

export default {
  getAreas() {
    return Api().get('/api/areas/')
  },
  postArea(userAreas) {
    return Api().post('/api/areas/', userAreas)
  },
  deleteArea(id) {
    return Api().delete('/api/areas/' + id + '/')
  },
  updateArea(userAreas, id) {
    return Api().put('/api/areas/' + id + '/', userAreas)
  },
  getOneArea(id) {
    return Api().get('/api/areas/' + id + '/')
  },
  getVegetationFromPosition(lat, lng) {
    return Api().get('/api/vegetation/?lat=' + lat + '&lng=' + lng)
  }
}
