<template>
  <div class="embed-container"><iframe width="500" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" title="Waldmeister Vegetationskarte" src="https://geodata4edu.hsr.ch/portal/apps/Embed/index.html?webmap=a1eb017351124f28ab070ea0cf81377f&amp;extent=8.6832,47.4249,8.7673,47.4565&amp;zoom=true&amp;scale=true&amp;disable_scroll=false&amp;theme=light"></iframe></div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Map'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>.embed-container {position: relative; padding-bottom: 80%; height: 0; max-width: 100%;} .embed-container iframe, .embed-container object, .embed-container iframe{position: absolute; top: 0; left: 0; width: 100%; height: 100%;} small{position: absolute; z-index: 40; bottom: 0; margin-bottom: -15px;}</style>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
