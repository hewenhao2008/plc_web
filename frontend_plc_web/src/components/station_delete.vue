<template>
  <Modal v-model="showDelete" width="360" :mask-closable="false" :closable="false">
    <p slot="header" style="color:#f60;text-align:center">
      <Icon type="information-circled"></Icon>
      <span>删除确认</span>
    </p>
    <div style="text-align:center">
      <p>是否继续删除？</p>
    </div>
    <div slot="footer">
      <Button type="error" size="large" long :loading="loading" @click="deleteSubmit">删除</Button>
    </div>
  </Modal>
</template>

<script>
  import Station from '../models/actions/station'

  export default {
    data () {
      return {
        loading: false
      }
    },
    props: [
      'showDelete',
      'id'
    ],
    methods: {
      deleteSubmit () {
        this.loading = true
        new Station()
          .DELETE({
            data: {
              id: this.id
            }
          })
          .then((res) => {
            this.loading = false
            if (res.data['ok'] === 1) {
              this.$Message.success(res.data['msg'])
            } else {
              this.$Message.error(res.data['msg'])
            }
            this.$emit('close')
          })
      },
      close () {
        this.$emit('close')
      }
    }
  }
</script>
