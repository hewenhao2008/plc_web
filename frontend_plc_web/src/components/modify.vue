<template>
  <!-- Modal begin-->
  <div class="modal fade" id="upload" tabindex="-1" role="dialog" aria-labelledby="new">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
            aria-hidden="true">&times;</span>
          </button>
          <h4 class="modal-title" id="myModalLabel1">上传到服务器</h4>
        </div>
        <div class="modal-body">
          <li>
            <label><span>选择站：</span></label>
            <select name="select" id="station">
              <option v-bind:value="sta.id" v-for="sta in station">{{sta.station_name}}</option>
            </select>
          </li>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal">取消</button>
          <button type="button" class="btn btn-primary btn-sm" v-on:click="upload()">上传</button>
        </div>
      </div>
    </div>
  </div>
  <!--Modal end-->
</template>
