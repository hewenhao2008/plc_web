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
      <Button type="error" size="large" :loading="loading" @click="deleteSubmit">删除</Button>
      <Button size="large" @click="close">取消</Button>
    </div>
  </Modal>
</template>

<script>
  import Query from '../models/actions/query_group'

  export default {
    data () {
      return {
        loading: false
      }
    },
    props: [
      'showDelete',
      'query_id',
      'variable_id'
    ],
    methods: {
      deleteSubmit () {
        this.loading = true
        new Query()
          .DELETE({
            data: {
              id: this.id,
              variable_id: this.variable_id
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
