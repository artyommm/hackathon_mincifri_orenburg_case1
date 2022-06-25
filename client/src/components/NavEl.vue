<template>
  <button type="button" :class="{
        'btn btn-secondary': !isActive,
        'btn btn-primary': isActive
      }">
      <slot></slot>
  </button>
</template>

<script>
export default {
  name: "NavEl",
  props: {
    isActive: {
      type: Boolean,
      required: true
    },
    classIcon: {
      type: String,
      required: true
    }
  },
}
</script>

<style  lang="css" scoped>
a {
  color: white;
  text-decoration: none;

}

</style>