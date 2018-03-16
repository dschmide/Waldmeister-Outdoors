
import Api from '@/services/Api'

export default {
	register (credentials) {
		//todo login
		//try
		return Api().post('/auth/users/create/', credentials)

		//noerror: login

	},
	login (credentials) {
		return Api().post('/auth/jwt/create/', credentials)
	},

	// redirect () {
	// 	return Api().get('redirect/')
	// }
}


/* Example
AuthenticationService.register({
	email: 'testmail@gmail'
})
*/