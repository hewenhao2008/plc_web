<template>
  <Modal v-model="showUpload" title="应用修改" width="360" :mask-closable="false" :closable="false">

    <div>
      <p>请选择需要应用修改的站点</p>
    <Select transfer v-model="station_id" style="width:100px" placeholder="选择站点"
            filterable>
      <Option v-for="station in stations" :value="station.id" :key="station.id">{{ station.station_name }}</Option>
    </Select>
      </div>

    <div slot="footer">
      <Button type="primary" :loading="loading" @click="upload">确认</Button>
      <Button type="ghost" @click="close" style="margin-left: 8px">关闭</Button>
    </div>
  </Modal>
</template>

<script>
  import Station from '@/models/actions/station'

  export default {
    data () {
      return {
        loading: false,
        station_id: ''
      }
    },
    props: [
      'showUpload',
      'stations'
    ],
    methods: {
      upload () {
        this.loading = true
        new Station()
          .PUT({
            data: {
              id: this.station_id,
              modification: 1
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
