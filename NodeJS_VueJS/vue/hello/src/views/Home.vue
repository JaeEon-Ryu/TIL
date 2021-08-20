<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">

    <span v-once>메시지: {{ msg }}</span>
    <input type="text" v-model="msg">
    <span v-html="msg"></span>  <span class="red">{{reversedMessage}}</span>
    <button :disabled="isButtonDisabled" @click="isButtonDisabled = !isButtonDisabled">disabledButton</button>

    <div>
      <a href="#" @click.prevent="aaa()">
        aaaaaaa <span @click.stop="bbb()">bbbbbbbb</span>
      </a>
    </div>

    <div :class="{red:isButtonDisabled}">REDDDDDDD</div>


    <todo-item v-for="item in groceryList"
      :todo="item"
      :key ="item.id">
    </todo-item>

    <todo-item :todo="groceryList[0]"></todo-item>
    <todo-item :todo="{id:9999,text:'999999'}"></todo-item>

    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TodoItem from '@/components/todo-item'

export default {
  name: 'Home',
  components: {
    TodoItem
  },

  created() {
    console.log(">>>>>>>", this._.random(30))
    this.fetchReplies();
    // this.$watch('ttt', this._.debounce(this.aaa, 1000))
    // this.$watch('ttt', this.aaa)
  },
  computed: {
    reversedMessage: function () {
      return this.msg.split('').reverse().join('')
    }
  },
  watch: {
    msg: function() {
      console.log("............", this.msg)
      this.reversedMessage = this.msg + "::"
    },
    reversedMessage: function() {
      console.log("tttttttttt")
    }
  },
  methods: {
    aaa(e) {
      console.log("aaaaaaaaaaaaaaaaaaa", e)
    },
    bbb() {
      console.log("bbbbbbbbbbbbbb")
    }
  },
  data() {
    return {
      jsonData: {msg: 'message', id: 123},
      ttt: 'ttt',
      msg: 'abcd',
      isButtonDisabled: false,
      replies: [],
      groceryList: [
        { id: 0, text: 'Vegetables' },
        { id: 1, text: 'Cheese' },
        { id: 2, text: 'Whatever else humans are supposed to eat' }
      ]
    }
  }

}
</script>

<style>
  .red { color: red; }
</style>