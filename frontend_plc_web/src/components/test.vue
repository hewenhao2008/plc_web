<template>
  <div class="post">
    <div class="loading" v-if="loading">
      Loading...
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="post" class="content">
      <h2>{{ post.title }}</h2>
      <p>{{ post.body }}</p>
    </div>
  </div>
</template>

<script>
//  import axios from 'axios'
//  const instance = axios.create({
//    baseURL: 'http://1.yakumo.applinzi.com',
//    headers: {
//      // 跨域请求 这个配置不能少
//      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
//      'Accept': 'application/json'
//    }
//  })
//  console.log(instance)
  export default {
    data () {
      return {
        loading: false,
        post: null,
        error: null
      }
    },
    created () {
      // 组件创建完后获取数据，
      // 此时 data 已经被 observed 了
      this.fetchData()
    },
    watch: {
      // 如果路由有变化，会再次执行该方法
      '$route': 'fetchData'
    },
    methods: {
      fetchData () {
//        this.error = this.post = null
        this.loading = true
        // replace getPost with your data fetching util / API wrapper
        console.log('ajax')
        this.$axios.get('http://localhost:8000/api/test', {headers: {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}, auth: {'username': 'yakumo17s', 'password': 'touhou'}})
          .then(function (response) {
            this.loading = false
            console.log('s')
//            console.log(response)
//            this.post = response
          })
          .catch(function (error) {
//            this.loading = false
            console.log('e')
            console.log(error)
//            this.error = error.toString()
          })
      }
    }
  }
</script>
