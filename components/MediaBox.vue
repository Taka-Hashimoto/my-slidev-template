<script setup lang="ts">
withDefaults(defineProps<{ src?: string; alt?: string; caption?: string; height?: string }>(), { alt: '', height: '100%' })
</script>
<template>
  <figure class="plain-media" :style="{ height }">
    <img v-if="src" :src="src" :alt="alt" />
    <div v-else class="plain-placeholder"><span>{{ alt || '図・写真を配置' }}</span></div>
    <figcaption v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>
