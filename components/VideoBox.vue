<script setup lang="ts">
withDefaults(defineProps<{
  src?: string
  poster?: string
  label?: string
  caption?: string
  autoplay?: boolean
}>(), { label: '動画を配置', autoplay: false })
</script>

<template>
  <figure class="plain-video">
    <SlidevVideo v-if="src" controls muted loop playsinline
      :autoplay="autoplay" autoreset="slide" :poster="poster" :printPoster="poster"
      :aria-label="label">
      <source :src="src" type="video/mp4" />
    </SlidevVideo>
    <div v-else class="plain-placeholder"><span>{{ label }}</span></div>
    <figcaption v-if="caption">{{ caption }}</figcaption>
  </figure>
</template>
