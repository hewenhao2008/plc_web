<style>
  .layout-breadcrumb {
    padding: 10px 15px 0;
  }

  .layout-content {
    min-height: 200px;
    margin: 15px;
    overflow: hidden;
    background: #fff;
    border-radius: 4px;
  }

  .layout-content-main {
    padding: 10px;
  }
</style>
<template>
  <div>
    <div class="layout-breadcrumb">
      <Breadcrumb>
        <Breadcrumb-item href="/">首页</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="layout-content">
      <div class="layout-content-main">
        <div class="jumbotron">
          <h1 class="display-3 text-success">云 集</h1>
          <p class="lead">工业生产数据监控系统</p>
          <hr class="my-2">
          <p>随便写点。</p>
          <p class="lead">
            <a class="btn btn-outline-success btn-lg" href="#" role="button">Learn more</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
