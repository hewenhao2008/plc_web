<!--<template>-->
<!--<div id="app">-->
<!--<img src="./assets/logo.png">-->
<!--<router-view></router-view>-->
<!--</div>-->
<!--</template>-->

<template>
  <div id="app">
    <!--<Affix>-->
    <header-view></header-view>
    <!--</Affix>-->

    <!--<br><br><br>-->
    <!--<Affix :offset-top="50">-->
    <router-view></router-view>
    <!--</Affix>-->
    <!--<layout></layout>-->

    <!--<footer-view></footer-view>-->

  </div>
</template>

<script>
  import siderbar from './components/sidebar.vue'
  import login from './components/login.vue'
  import footer from './components/footer.vue'
  import header from './components/new_header.vue'
  import layout from './components/layout.vue'

  export default {
    components: {
      'sidebar': siderbar,
      'login': login,
      'footer-view': footer,
      'header-view': header,
      'layout': layout
    }
  }
</script>


<!--<script>-->
<!--export default {-->
<!--name: 'app'-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--font-family: 'Avenir', Helvetica, Arial, sans-serif;-->
<!-- -webkit-font-smoothing: antialiased;-->
<!-- -moz-osx-font-smoothing: grayscale;-->
<!--text-align: center;-->
<!--color: #2c3e50;-->
<!--margin-top: 60px;-->
<!--}-->
<!--</style>-->
