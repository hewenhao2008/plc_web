<template>
  <img :src="url" :alt="alt" />
</template>

<script>
  import md5 from 'md5'

  export default {
    name: 'gravatar-img',

    props: {
      email: {
        type: String
      },

      hash: {
        type: String,
        default: ''
      },

      size: {
        type: String,
        default: 40
      },

      defaultImg: {
        type: String,
        default: 'retro'
      },

      rating: {
        type: String,
        default: 'g'
      },

      alt: {
        type: String,
        default: 'Avatar'
      }
    },

    computed: {
      url () {
        const img = [
//          '//cn.gravatar.com/avatar/',
          '//cdn.v2ex.com/gravatar/',
          this.hash || md5(this.email.trim().toLowerCase()),
          `?s=${this.size}`,
          `&d=${this.defaultImg}`,
          `&r=${this.rating}`
        ]

        return img.join('')
      }
    }
  }
</script>
