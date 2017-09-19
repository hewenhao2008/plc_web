import REST from '@/utils/rest'
import consts from '@/utils/consts'
import restHelpers from '@/utils/helpers/restHelpers'
import storage from '@/utils/helpers/storageLite'

export default class extends REST {
  constructor () {
    super()
    this.addHeaders({
      'Authorization': 'Token ' + storage.get('token')
    })
    this.baseURL = consts.API_URL
    this.errorHandler = restHelpers.errorHandler
    this.path = 'plc'
  }
}
