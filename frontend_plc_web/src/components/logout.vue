<template>
  <div>
    aa
  </div>
</template>
<script>
  import auth from '@/utils/auth'
  import logout from '../router/logout'
  export default {
    create () {
      if (auth.loggedIn()) {
        auth.logout()
      }
      this.$router.push('/login')
    }
  }
</script>
