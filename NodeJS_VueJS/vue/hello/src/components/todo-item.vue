<template>
<div>
    <li>TTT : {{todo.text}} </li>
</div>
</template>

<script>
export default {
    name:'todo-item',
    props:{
        todo:{
            type:Object,
            default(){
                return {
                    id:-1,
                    text:'default todo'
                }
            },
            required:true
        }
    }
}
</script>